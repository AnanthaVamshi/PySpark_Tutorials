#!/usr/bin/python
#-----------------------------------------------------
# Apply a join() transformation to an RDD
# Input: NONE
#------------------------------------------------------
# Input Parameters:
#    NONE
#-------------------------------------------------------
# @author Mahmoud Parsian
#-------------------------------------------------------
from __future__ import print_function 
import sys 
from pyspark.sql import SparkSession 


#=========================================
def create_pair(t3):
    # t3 = (name, city, number)
    name = t3[0]
    #city = t3[1]
    number = int(t3[2])
    return (name, number)
#end-def
#==========================================

if __name__ == '__main__':

    #if len(sys.argv) != 2:  
    #    print("Usage: rdd_transformation_join.py <file>", file=sys.stderr)
    #    exit(-1)

    # create an instance of SparkSession
    spark = SparkSession\
        .builder\
        .appName("rdd_transformation_join")\
        .getOrCreate()
    #
    print("spark=",  spark)

    #========================================
    # join() transformation
    #
    # join(other, numPartitions=None)
    #
    # Description:
    # Return an RDD containing all pairs of elements with 
    # matching keys in self and other.  Each pair of elements 
    # will be returned as a (k, (v1, v2)) tuple, where (k, v1) 
    # is in self RDD and (k, v2) is in other RDD. Performs a 
    # hash join across the cluster.
    #========================================
 
    source_pairs = [(1,"u"), (1,"v"), (2, "a"), (3,"b"), (4,"z1") ]
    print("source_pairs = ", source_pairs)
    source = spark.sparkContext.parallelize(source_pairs)
    print("source.count(): ", source.count())
    print("source.collect(): ", source.collect())

    other_pairs = [(1,"x"), (1,"y"), (2, "c"), (2,"d"), (3,"m"), (8,"z2") ]
    print("other_pairs = ", other_pairs)
    other = spark.sparkContext.parallelize(other_pairs)
    print("other.count(): ", other.count())
    print("other.collect(): ", other.collect())

    #-----------------------------------------
    # source.join(other)
    #-----------------------------------------
    joined = source.join(other)
    print("joined.count(): ", joined.count())
    print("joined.collect(): ", joined.collect())

     
    # done!
    spark.stop()

