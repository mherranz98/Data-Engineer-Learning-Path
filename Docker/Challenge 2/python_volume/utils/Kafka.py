from kafka import KafkaConsumer
import logging


class Kafka:

    def __init__(self) -> None:
        self.connectKafka = "connectKafka"

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
        except Exception as e:
            logging.error("Unable to connect to Kafka listener")
            logging.exception(e)
            quit()
