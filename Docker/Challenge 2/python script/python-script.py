import logging
from kafka import KafkaConsumer
from pymongo import MongoClient
from string import Template
from psycopg2 import connect as Psycopg2Client
import json

# Set logging parameters for future monitoring, debugging or error-handling
logging.basicConfig(level=logging.INFO,
                    filename="challenge2.log",
                    filemode="w")

# ---------------------------------------------------------------------------------
# --------------------------- FUNCTION DEFINITION ---------------------------------
# ---------------------------------------------------------------------------------


def connectKafka(topic: str, bootstrap_servers: str) -> KafkaConsumer:
    """Connect to Kafka Listener

    Args:
        - topic: Kakfa topic to read from
        - bootstrap_servers: host:port pair address of Kafka brokers

    Returns:
        - kafka.KafkaConsumer instance from which to consume messages
    """
    try:
        kafka_consumer = KafkaConsumer(
            topic, bootstrap_servers=bootstrap_servers)
        logging.info("Connected to Kafka listener")
        return kafka_consumer
    except:
        logging.error("Unable to connect to Kafka listener")


def connectMongoDB(host: str, port: int, username: str, password: str) -> MongoClient:
    """Connect to Mongo DB
    Args:
        - host:
        - port:
        - username:
        - password:

    Returns:
        - pymongo.MongoClient instance to connect to MongoDB
    """
    try:
        client = MongoClient(host=host, port=port,
                             username=username, password=password)
        logging.info("Connected to MongoDB")
        return client
    except:
        logging.error("Unable to connect to MongoDB")


def createMongoCollection(client: MongoClient, db_name: str, collection_name: str):
    """Create database and collection in MongoDB

    Note: These will not be created until first message is inserted

    Args:
        - client: instance of Mongo library to interact with MongoDB
        - db_name: name of the MongoDB database
        - collection_name: name of the MongoDB collection

    Returns:
        - collection: instance from which to consume messages
    """
    try:
        db = client[db_name]
        collection = db[collection_name]
        logging.info("Collection and Database created")
        return collection
    except:
        logging.error("Unable to create Mongo database and collection")


def writeKafkaMessageToMongo(message, collection):
    """ Insert a single message into a MongoDB collection

    Args:
        - message: message from Kafka consumer instance
        - collection: MongoDB collection instance to write to
    """
    try:
        decoded_msg = json.loads(message.value.decode("utf-8"))
        collection.insert_one(decoded_msg)
        logging.info("Quote successfully inserted in MongoDB")
    except:
        logging.error("Unable to insert the message to Mongo database")


def connectPostgreSQL(host: str, port: str, database: str, username: str, password: str) -> dict:
    """Connect to PostgreSQL database

    Args:
        - host:
        - port:
        - database: name of the database to connecto to (defined in docker-compose file in our case)
        - username:
        - password:

    Returns:
        - dict { str : psycopg2.client, str : psycopg2.client.cursor } instance to connect to MongoDB
    """
    try:
        connection = Psycopg2Client(host=host, port=port, database=database,
                                    user=username, password=password)
        cursor = connection.cursor()
        logging.info("Connected to PostgreSQL")
        return {"connection": connection, "cursor": cursor}
    except:
        logging.error("Unable to connect to PostgreSQL")


def createTablePostgreSQL(PostgresClient: Psycopg2Client, table_name: str, table_schema: str):
    """Create a table in PostgreSQL if not exists in the database to which we are connected

    Note: a schema must be provided as SQL databases are schema on-write

    Args:
        - PostgresClient: Psycopg2Client client instance to connect to Postgres database
        - table_name: name of table we want to create
        - table_schema: schema of the table we want to create
    """
    query = "CREATE TABLE IF NOT EXISTS public.{0} ({1})".format(
        table_name, table_schema)
    try:
        PostgresClient["cursor"].execute(query)
        PostgresClient["connection"].commit()
        logging.info("Table created")
    except:
        logging.error("Unable to create table")


def writeKafkaMessageToPostgreSQL(message, PostgresClient):
    """Insert a single record into Postgres database

    Args:
        - message: message from Kafka consumer instance
        - PostgresClient: Psycopg2Client client instance to connect to Postgres database
    """
    decoded_msg = json.loads(message.value.decode("utf-8"))
    template = Template(
        """INSERT INTO public.quotes(quotes, charact, imag) VALUES ('$quote' , '$charact' , '$imag')""")
    query = template.substitute(
        quote=decoded_msg['quote'].replace("'", "`"), charact=decoded_msg['character'], imag=decoded_msg['image'])
    try:
        PostgresClient["cursor"].execute(query)
        PostgresClient["connection"].commit()
        logging.info("Quote successfully inserted in Postgres DB")
    except:
        logging.error("Unable to insert the message to PostgreSQL database")


# ---------------------------------------------------------------------------------
# ------------------------------- MAIN PROGRAM ------------------------------------
# ---------------------------------------------------------------------------------

def main():
    # Connect to Kafka to consume latest messages and auto-commit offsets
    topic = 'topic_quotes'
    bootstrap_server = 'localhost:9092'
    kafka_consumer = connectKafka(
        topic, bootstrap_servers=bootstrap_server)

    # Connect to MongoDB with server configuration with authentication requirements
    host = "localhost"
    port = 27017  # Listener internal/external to Docker (9092/29092)
    username = "mchi"
    password = "mchi1234"
    database_name = "simpsons"

    # Connect to Postgres with same authentication of Mongo and create table (schema on-write)
    port_postgres = "5432"
    table_name = "quotes"
    table_schema = """ quote_id SERIAL PRIMARY KEY,
	quotes VARCHAR(500),
	charact VARCHAR(500),
	imag VARCHAR(500)
        """

    # Connect to MongoDB
    mongoClient = connectMongoDB(
        host=host, port=port, username=username, password=password)

    # Create MongoDB collection and database
    db_name = "simpson_db"
    collection_name = "quotes"
    collection = createMongoCollection(mongoClient, db_name, collection_name)

    # Create Postgres table in public part
    connection = connectPostgreSQL(host=host, port=port_postgres, database=database_name,
                                   username=username, password=password)
    createTablePostgreSQL(connection, table_name=table_name,
                          table_schema=table_schema)

    # Insert messages in stream while connected to kafka bootstrap server (kafka_consumer)
      for msg in kafka_consumer:
           if msg.offset % 2 != 0:  # for every message we get two entries: content + metadata
                writeKafkaMessageToMongo(msg, collection)
                writeKafkaMessageToPostgreSQL(msg, connection)
            else:
                pass

    connection["cursor"].close()


if __name__ == "__main__":
    main()
