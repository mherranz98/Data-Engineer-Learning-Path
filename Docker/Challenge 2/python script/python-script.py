import logging
from kafka import KafkaConsumer
from pymongo import MongoClient
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


def writeMessageToMongo(message, collection):
    """Function to insert a single message into collection defined in previous function"""
    try:
        decoded_msg = json.loads(message.value.decode("utf-8"))
        collection.insert_one(decoded_msg)
        logging.info("Quote inserted")
    except:
        logging.error("Unable to insert the message to Mongo database")


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
    mongoClient = connectMongoDB(
        host=host, port=port, username=username, password=password)

    # Create MongoDB collection and database
    db_name = "simpson_db"
    collection_name = "quotes"
    collection = createMongoCollection(mongoClient, db_name, collection_name)

    # Insert messages in stream while connected to kafka bootstrap server (kafka_consumer)
    for msg in kafka_consumer:
        writeMessageToMongo(msg, collection)


if __name__ == "__main__":
    main()
