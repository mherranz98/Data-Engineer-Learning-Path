import logging
from kafka import KafkaConsumer
from pymongo import MongoClient
import psycopg2
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
        connection = psycopg2.connect(host=host, port=port, database=database,
                                      username=username, password=password)
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


def createTablePostgreSQL(PostgresClient, database_name, table_name, table_schema):
    """Function to create a table in PostgreSQL if not exists"""
    query1 = "CREATE DATABASE IF NOT EXISTS {0}".format(database_name)
    query2 = "CREATE TABLE IF NOT EXISTS {0} ({1})".format(
        table_name, table_schema)
    try:
        PostgresClient.cursor.execute(query1)
        PostgresClient.cursor.execute(query2)
        PostgresClient.connection.commit()
        logging.info("Database and table created")
    except:
        logging.error("Unable to create database or table")


def writeMessageToMongo(message, collection):
    """Function to insert a single message into MongoDB collection defined in previous function"""
    try:
        decoded_msg = json.loads(message.value.decode("utf-8"))
        collection.insert_one(decoded_msg)
        logging.info("Quote inserted")
    except:
        logging.error("Unable to insert the message to Mongo database")


def writeMessageToPostgreSQL(message, PostgresClient, database_name, table_name):
    """Function to insert a single message into PostreSQL defined in previous function"""
    decoded_msg = json.loads(message.value.decode("utf-8"))
    query = "INSERT INTO public.quotes(quotes, charact, imag) VALUES ('{0}','{1}','{2}')".format(
        decoded_msg['quote'], decoded_msg['character'], decoded_msg['image'])
    try:
        PostgresClient.cursor.execute(query)
        PostgresClient.connection.commit()
        logging.info("Quote inserted")
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
    password = 'mchi1234'
    database_name = "simpson_db"
    table_name = "quotes"
    table_schema = """ quote_id SERIAL, 
        quotes VARCHAR(500),
        character VARCHAR(500),
        image VARCHAR(500)
        """

    """
    mongoClient = connectMongoDB(
        host=host, port=port, username=username, password=password)

    # Create MongoDB collection and database
    db_name = "simpson_db"
    collection_name = "quotes"
    collection = createMongoCollection(mongoClient, db_name, collection_name)
    """

    postgresClient = connectPostgreSQL(
        host=host, port=port, database=database_name, username=username, password=password)

    createTablePostgreSQL(postgresClient, database_name=database_name,
                          table_name=table_name, table_schema=table_schema)

    # Insert messages in stream while connected to kafka bootstrap server (kafka_consumer)
    # for msg in kafka_consumer:
    #writeMessageToMongo(msg, collection)


if __name__ == "__main__":
    main()
