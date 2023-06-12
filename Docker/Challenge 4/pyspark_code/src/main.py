from pyspark.sql.functions import *
from pyspark.sql import SparkSession
#from pyspark.sql.types import *

# ---------------------------------------------------------------------------------

# Create SparkSession
spark_kafka = SparkSession \
    .builder \
    .appName("Streaming_PySpark") \
    .config("spark.sql.debug.maxToStringFields", "100") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .getOrCreate()

# ---------------------------------------------------------------------------------

# Reduce verbose in prompt to solely warnings
spark_kafka.sparkContext.setLogLevel('WARN')

# ---------------------------------------------------------------------------------

# Read in stream mode all records that Kafka receives
kafka_df_stream = spark_kafka \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("failOnDataLoss", "false") \
    .option("subscribe", "quotes-simpsons") \
    .option("startingOffsets", "earliest") \
    .load()

# Decode value attribute in the streamDF
string_df = kafka_df_stream.selectExpr("CAST(value AS STRING)")

# Explode JSON
schema_simpsons = StructType([
    StructField("quote", StringType(), True),
    StructField("character", StringType(), True),
    StructField("image", StringType(), True),
    StructField("characterDirection", StringType(), True)])

exploded_df = string_df.withColumn('data', from_json(col('value'), schema=schema_simpsons)) \
                       .select(col('data.quote').alias('quotes'),
                               col('data.character').alias('charact'),
                               col('data.image').alias('imag'),
                               col('data.characterDirection').alias('characterdirection'))

# Function that applies to all records ingested in the microbatches


def foreach_batch_function(df, epoch_id):
    global window
    # Properties for writing to DB
    url_postgres = "jdbc:postgresql://postgres:5432/simpsons"
    uri_mongo = 'mongodb://mchi:mchi1234@mongodb:27017/simpsons.quotes?authSource=admin'
    uri_mongo_count = 'mongodb://mchi:mchi1234@mongodb:27017/simpsons.count?authSource=admin'
    properties = {'user': 'mchi', 'password': 'mchi1234',
                  'driver': 'org.postgresql.Driver'}

    window += 1

    counter_df = df.groupBy("charact") \
                   .agg(count("charact").alias("counter")) \
                   .withColumn("window_number", lit(window)) \
                   .select(col("window_number"), col("charact"), col("counter"))

    print("Inserting a quote into the DB ...")

    # Write new records to DB
    # Write to Postgres
    df.write \
        .jdbc(url=url_postgres,
              table='public.quotes',
              mode='append',
              properties=properties
              )
    # Write to Mongo
    df.write \
        .format('mongo') \
        .mode('append') \
        .option("uri", uri_mongo) \
        .option("database", "simpsons") \
        .option("collection", "quotes") \
        .save()


# Finally, execute the streaming write with previous function
exploded_df.writeStream \
    .format("console") \
    .foreachBatch(foreach_batch_function) \
    .trigger(processingTime="1 minute") \
    .start() \
    .awaitTermination()
