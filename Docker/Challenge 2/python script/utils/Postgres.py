import logging
from psycopg2 import connect as Psycopg2Client
from string import Template
import json


class Postgres:

    def __init__(self) -> None:
        self.connectPostgres = "connectPostgres"

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
            logging.error(
                "Unable to insert the message to PostgreSQL database")
