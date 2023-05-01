from pymongo import MongoClient
import logging
import json


class Mongo:

    # These code lines will not be executed when the Mongo class is used as an imported module in main.py file
    if __name__ == "__main__":
        print("Code is being executed as script")

    def __init__(self) -> None:
        self.connectMongoDB = "connectMongoDB"

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
        except Exception as e:
            logging.error("Unable to connect to MongoDB")
            logging.exception(e)

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
        except Exception as e:
            logging.error("Unable to create Mongo database and collection")
            logging.exception(e)

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
        except Exception as e:
            logging.error("Unable to insert the message to Mongo database")
            logging.exception(e)
