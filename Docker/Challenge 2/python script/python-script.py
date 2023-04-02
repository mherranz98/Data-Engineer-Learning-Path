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


def connectKafka(topic, bootstrap_servers):
    """Function to connect to Kafka Listener"""
    try:
        kafka_consumer = KafkaConsumer(
            topic, bootstrap_servers=bootstrap_servers)
        logging.info("Connected to Kafka listener")
        return kafka_consumer
    except:
        logging.error("Unable to connect to Kafka listener")


def connectMongoDB(host, port, username, password):
    """Function to connect to Mongo DB"""
    try:
        client = MongoClient(host=host, port=port,
                             username=username, password=password)
        logging.info("Connected to MongoDB")
        return client
    except:
        logging.error("Unable to connect to MongoDB")


def connectPostgreSQL(host, port, database, username, password):
    """Function to connect to PostgreSQL"""
    try:
        connection = Psycopg2Client(host=host, port=port, database=database,
                                    user=username, password=password)
        cursor = connection.cursor()
        logging.info("Connected to PostgreSQL")
        return {"connection": connection, "cursor": cursor}
    except:
        logging.error("Unable to connect to PostgreSQL")


def createMongoCollection(client, db_name, collection_name):
    """Function to create database and collection. These will not be created until first
    message is inserted"""
    try:
        db = client[db_name]
        collection = db[collection_name]
        logging.info("Collection and Database created")
        return collection
    except:
        logging.error("Unable to create Mongo database and collection")


def createTablePostgreSQL(PostgresClient, table_name, table_schema):
    """Function to create a table in PostgreSQL if not exists"""
    query = "CREATE TABLE IF NOT EXISTS public.{0} ({1})".format(
        table_name, table_schema)
    try:
        PostgresClient["cursor"].execute(query)
        PostgresClient["connection"].commit()
        logging.info("Table created")
    except:
        logging.error("Unable to create table")


def writeMessageToMongo(message, collection):
    """Function to insert a single message into MongoDB collection defined in previous function"""
    try:
        decoded_msg = json.loads(message.value.decode("utf-8"))
        collection.insert_one(decoded_msg)
        logging.info("Quote successfully inserted in MongoDB")
    except:
        logging.error("Unable to insert the message to Mongo database")


def writeMessageToPostgreSQL(message, PostgresClient):
    """Function to insert a single message into PostreSQL defined in previous function"""
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
            writeMessageToMongo(msg, collection)
            writeMessageToPostgreSQL(msg, connection)
        else:
            pass

    connection["cursor"].close()


if __name__ == "__main__":
    main()
