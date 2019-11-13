from __future__ import print_function 
import sys 
from pyspark.sql import SparkSession 
#<1> Import the print() function
#<2> Import System-specific parameters and functions
#<3> Import SparkSession from the pyspark.sql module

#===================
# function:  `create_pair` to accept  
# a String object as "key,number" and  
# returns a (key, (number, 1)) pair.
#
# record as String of "key,number"
def create_pair(record):
    tokens = record.split(",")
    # key -> tokens[0] as String
    # number -> tokens[1] as Integer
    # return (key, (sum, count))
    return (tokens[0], (int(tokens[1]), 1))
# end-of-function
#===================
# function:  `add_pairs` accept two
# tuples of (sum1, count1) and (sum2, count2) 
# and returns sum of tuples (sum1+sum2, count1+count2).
#
# a = (sum1, count1)
# b = (sum2, count2)
def add_pairs(a, b):
    # sum = sum1+sum2
    sum = a[0] + b[0]
    # count = count1+count2 
    count = a[1] + b[1]
    return (sum, count)
# end-of-function
#===================

if __name__ == '__main__':

    # <4>    
    if len(sys.argv) != 2:  
        print("Usage: ", __file__, "  <input-path>", file=sys.stderr)
        exit(-1)

    # <5>
    spark = SparkSession\
        .builder\
        .appName("average_monoid_use_reducebykey")\
        .getOrCreate()

    #  sys.argv[0] is the name of the script.
    #  sys.argv[1] is the first parameter
    # <6>
    input_path = sys.argv[1]  
    print("input_path: {}".format(input_path))

    # read input and create an RDD<String>
    # <7>
    records = spark.sparkContext.textFile(input_path) 
    print("records.count(): ", records.count())
    print("records.collect(): ", records.collect())

    # create a pair of (key, (number, 1)) for "key,number"
    # <8>
    sum_and_freq = records.map(create_pair)
    print("sum_and_freq.count(): ", sum_and_freq.count())
    print("sum_and_freq.collect(): ", sum_and_freq.collect())

    # aggregate the (sum, count) of each unique key
    # <9>
    sum_count = sum_and_freq.reduceByKey(add_pairs) 
    print("sum_count.count(): ", sum_count.count())
    print("sum_count.collect(): ", sum_count.collect())

    # create the final RDD as RDD[key, average]
    # <10>
    # v = (v[0], v[1]) = (sum, count)
    averages =  sum_count.mapValues(lambda v : float(v[0]) / float(v[1])) 
    print("averages.count(): ", averages.count())
    print("averages.collect(): ", averages.collect())

    # done!
    spark.stop()
#end-program

#<4> Make sure that we have 2 parameters in the command line
#<5> Create an instance of a SparkSession object by using the builder pattern SparkSession.builder class
#<6> Define input path (this can be a file or a directory containing any number of files
#<7> Read input and create the first RDD as RDD[String] where each object has this foramt: "key,number"
#<8> Create key_number_one RDD as (key, (number, 1))
#<9> Aggregate (sum1, count1) with (sum2, count2) and create (sum1+sum2, count1+count2) as values
#<10> Apply the mapValues() transformation to find final average per key

