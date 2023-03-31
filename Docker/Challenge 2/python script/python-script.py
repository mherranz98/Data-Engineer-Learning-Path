from kafka import KafkaConsumer
import json
import pymongo

# To consume latest messages and auto-commit offsets
topic='quotes-simpsons'
bootstrap_server='localhost:9092' 
# Use the listener internal of Docker to send from Kafka to Postgres 
consumer = KafkaConsumer(topic,bootstrap_servers=bootstrap_server)

# Connect to Mongo DB
# Server configuration with authentication requirements
client = pymongo.MongoClient(host="localhost",
                             port=27017, 
                             username='mchi', 
                             password='mchi1234') 

#Creates simpsons database and quotes collection inside it (if needed)
simpsons_db=client["simpsons"]
quotes_collection=simpsons_db["quotes"]

# Insert the records into the MongoDB 
# (still don't know why I have to use error-handling)
for msg in consumer:
    try:
        decoded_msg=json.loads(msg.value.decode("utf-8"))   
        quotes_collection.insert_one(decoded_msg)
        print("Quote inserted")
    except:
        pass

    