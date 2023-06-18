from pyspark.sql import SparkSession
import logging


def getSparkContext(appName: str) -> SparkSession:
    conf = SparkConf()
    conf.setAll(
        [
            ("spark.sql.debug.maxToStringFields", "100"),
            ("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0"),
            ("spark.app.name", appName)
        ]
    )
    return SparkSession.builder.config(conf=conf).getOrCreate()


def setLogLevel(sparkSession: SparkSession, logLevel: str) -> None:
    return sparkSession.setLogLevel(logLevel)
