import os
from pyspark import SparkConf, SparkContext

# Set up the Spark configuration and context
conf = SparkConf().setAppName("SimpleApp").setMaster("local[*]")
sc = SparkContext(conf=conf)

# Create an RDD from a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_rdd = sc.parallelize(numbers)

# Perform a basic transformation: filter even numbers
even_numbers_rdd = numbers_rdd.filter(lambda x: x % 2 == 0)

# Collect the results
even_numbers = even_numbers_rdd.collect()

# Print the results
print("Even numbers:", even_numbers)

# Stop the Spark context
sc.stop()
