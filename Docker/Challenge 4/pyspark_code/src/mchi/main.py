from mchi.job import readKafka, explodeDataframe, writeStream, writeDatabases
from mchi.utils import get_spark_context

if __name__ == "__main__":

    # Spark job executed against standalone Docker cluster
    sparkAppName = "simpsons"
    spark = get_spark_context(sparkAppName)

    streamDataframe = readKafka(
        bootstrapServers="kafka:29092",
        topic="simpson_quotes",
        sparkSession=spark)

    df = explodeDataframe(streamDataframe)

    url_postgres = "jdbc:postgresql://postgres:5432/simpsons"
    uri_mongo = 'mongodb://mchi:mchi1234@mongodb:27017/simpsons.quotes?authSource=admin'
    properties = {'user': 'mchi', 'password': 'mchi1234',
                  'driver': 'org.postgresql.Driver'}

    batchMongo = writeDatabases.writeMongo()
    batchPostgres = writeDatabases.writePostgres()

    df.writeStream(explodeDataframe, batchMongo)
    df.writeStream(explodeDataframe, batchPostgres)

    # pyspark --master standalone --py-files main.py
