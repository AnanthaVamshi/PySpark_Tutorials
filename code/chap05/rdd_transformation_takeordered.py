#!/usr/bin/python
#-----------------------------------------------------
# Apply a takeOrdered() transformation to an RDD
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


if __name__ == '__main__':

    #if len(sys.argv) != 2:  
    #    print("Usage: rdd_transformation_takeordered.py <file>", file=sys.stderr)
    #    exit(-1)

    #input_path = sys.argv[1]
    
    # create an instance of SparkSession
    spark = SparkSession\
        .builder\
        .appName("rdd_transformation_takeordered")\
        .getOrCreate()
    #
    print("spark = ",  spark)
    #
    sc = spark.sparkContext
    print("sc = ",  sc)
    
    #========================================
    # takeOrdered() transformation
    #
    # takeOrdered(N, key=None)
    # Get the N elements from an RDD ordered 
    # in ascending order or as specified by 
    # the optional key function.
    #
    #========================================
    numbers = [8, 10, 1, 2, 9, 3, 4, 5, 6, 7]
    print("numbers = ", numbers)
    #
    top3 = sc.parallelize(numbers).takeOrdered(3)
    print("top3 = ", top3)
    #
    bottom3 = sc.parallelize(numbers).takeOrdered(3, key=lambda x: -x)
    print("bottom3 = ", bottom3)
    #
    pairs = [(10,"z1"), (1,"z2"), (2,"z3"), (9,"z4"), (3,"z5"), (4,"z6"), (5,"z7"), (6,"z8"), (7,"z9")]
    print("pairs = ", pairs)
    #
    top3_pairs = sc.parallelize(pairs).takeOrdered(3)
    print("top3_pairs = ", top3_pairs)
    #
    bottom3_pairs = sc.parallelize(pairs).takeOrdered(3, key=lambda x: -x[0])
    print("bottom3_pairs = ", bottom3_pairs)

    
    # done!
    spark.stop()

