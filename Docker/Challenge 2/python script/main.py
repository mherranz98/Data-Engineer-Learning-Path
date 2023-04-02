import logging

from utils.Kafka import Kafka
from utils.Mongo import Mongo
from utils.Postgres import Postgres

# Set logging parameters for future monitoring, debugging or error-handling
logging.basicConfig(level=logging.INFO,
                    filename="challenge2.log",
                    filemode="w")

# ---------------------------------------------------------------------------------
# ------------------------------- MAIN PROGRAM ------------------------------------
# ---------------------------------------------------------------------------------


def main():

    # Connect to Kafka to consume latest messages and auto-commit offsets
    topic = 'topic_quotes'
    bootstrap_server = 'localhost:9092'
    kafka_consumer = Kafka.connectKafka(
        topic=topic, bootstrap_servers=bootstrap_server)

    # Connect to MongoDB with server configuration with authentication requirements
    host = "localhost"
    port = 27017  # Listener internal/external to Docker (9092/29092)
    username = "mchi"
    password = "mchi1234"
    database_name = "simpsons"

    # Connect to MongoDB
    mongoClient = Mongo.connectMongoDB(
        host=host, port=port, username=username, password=password)

    # Create MongoDB collection and database
    db_name = "simpson_db"
    collection_name = "quotes"
    collection = Mongo.createMongoCollection(
        mongoClient, db_name, collection_name)

    # Connect to Postgres with same authentication of Mongo and create table (schema on-write)
    port_postgres = "5432"
    table_name = "quotes"
    table_schema = """ quote_id SERIAL PRIMARY KEY,
	quotes VARCHAR(500),
	charact VARCHAR(500),
	imag VARCHAR(500)
        """
    # Create Postgres table in public part
    connection = Postgres.connectPostgreSQL(host=host, port=port_postgres, database=database_name,
                                            username=username, password=password)
    Postgres.createTablePostgreSQL(connection, table_name=table_name,
                                   table_schema=table_schema)

    # Insert messages in stream while connected to kafka bootstrap server (kafka_consumer)
    for msg in kafka_consumer:
        if msg.offset % 2 != 0:  # for every message we get two entries: content + metadata
            Mongo.writeKafkaMessageToMongo(msg, collection)
            Postgres.writeKafkaMessageToPostgreSQL(msg, connection)
        else:
            pass

    connection["cursor"].close()


if __name__ == "__main__":
    main()
