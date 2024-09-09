from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("PySpark Installation Test").getOrCreate()
df = spark.createDataFrame([(1,"hello"),(2,"world")],["id","message"])
df.show()