from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from graphframes import *

conf = SparkConf().setAppName('graph_processing') \
.set('spark.jars.packages', 'graphframes:graphframes:0.8.1-spark3.0-s_2.12')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

spark = SparkSession(sc)

# Vertices DataFrame
v = spark.createDataFrame([
("1", "John", 28),
("2", "Mike", 30),
("3", "Sara", 25)
], ["id", "name", "age"])

# Edges DataFrame
e = spark.createDataFrame([
("1", "2", "friend"),
("2", "3", "follows"),
("3", "1", "friend")
], ["src", "dst", "relationship"])

# Create a GraphFrame
g = GraphFrame(v, e)

# Query: Get in-degree of each vertex.
g.inDegrees.show()

# Query: Count the number of "follow" connections in the graph.
g.edges.filter("relationship = 'follows'").count()

# Run PageRank algorithm, and show results.
results = g.pageRank(resetProbability=0.01, maxIter=20)
results.vertices.select("id", "pagerank").show()

# Stop SparkSession
spark.stop()