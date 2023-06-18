from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, StructField
from pyspark.sql.functions import col, from_json


class readKafka:

    def __init__(self) -> None:
        self.readKafka = "readKafka"

    def readStreamKafkaTopic(bootstrapServers: str, topic: str, sparkSession: SparkSession):
        kafkaStream = sparkSession \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", bootstrapServers) \
            .option("failOnDataLoss", "false") \
            .option("subscribe", topic) \
            .option("startingOffsets", "earliest") \
            .load()

        return kafkaStream


class transformStreamDataframe:

    def explodeDataframe(df):

        # Decode value attribute in the streamDF
        string_df = df.selectExpr("CAST(value AS STRING)")

        # Explode JSON
        schema_simpsons = StructType([
            StructField("quote", StringType(), True),
            StructField("character", StringType(), True),
            StructField("image", StringType(), True),
            StructField("characterDirection", StringType(), True)])

        exploded_df = string_df.withColumn('data', from_json(col('value'), schema=schema_simpsons)) \
            .select(col('data.quote').alias('quotes'),
                    col('data.character').alias(
                'charact'),
            col('data.image').alias('imag'),
            col('data.characterDirection').alias('characterdirection'))

        return exploded_df


class writeDatabases:

    def __init__(self) -> None:
        self.batchFunctions = "batchFunctions"

    def writeStream(df, batchFunction) -> None:
        df.writeStream \
            .format("console") \
            .foreachBatch(batchFunction) \
            .trigger(processingTime="1 minute") \
            .start() \
            .awaitTermination()

    def writeMongo(uriMongo: str, database: str, collection: str) -> None:
        return df.write \
            .format('mongo') \
            .mode('append') \
            .option("uri", uriMongo) \
            .option("database", database) \
            .option("collection", collection) \
            .save()

    def writePostgres(properties: dict(str, str), uriPostgres: str, table: str) -> None:
        return df.write \
            .jdbc(url=uriPostgres,
                  table=table,
                  mode='append',
                  properties=properties)
