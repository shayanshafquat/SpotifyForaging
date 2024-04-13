from pyspark import SparkContext

sc = SparkContext()

# Read data from stdin
rdd = sc.textFile('-')  # '-' means standard input

# Example: Count lines if each row is a line of text
print(rdd.count())

sc.stop()