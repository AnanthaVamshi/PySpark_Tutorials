#!/usr/bin/python
#-----------------------------------------------------
# Apply a join() 
# source_df.join(other_df)
#
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
    #    print("Usage: dataframe_join_inner.py <file>", file=sys.stderr)
    #    exit(-1)

    # create an instance of SparkSession
    spark = SparkSession\
        .builder\
        .appName("dataframe_join_inner")\
        .getOrCreate()
    #
    print("spark=",  spark)

    #========================================
    # join(other, on=None, how=None)
    #
    # Joins with another DataFrame, using the given 
    # join expression.
    #
    # Parameters:	
    #  other - Right side of the join
    #  on - a string for the join column name, 
    #       a list of column names, a join 
    #       expression (Column), or a list of Columns. 
    #       If on is a string or a list of strings 
    #       indicating the name of the join column(s), 
    #       the column(s) must exist on both sides, and 
    #       this performs an equi-join.
    #  how - str, default inner. Must be one of: 
    #        inner, cross, outer, full, full_outer, left, 
    #        left_outer, right, right_outer, left_semi, 
    #        and left_anti.
    #
    #========================================

    triplets = [("alex","Ames", 20),\
                ("alex", "Sunnyvale",30),\
                ("alex", "Cupertino", 40),\
                ("mary", "Ames", 35),\
                ("mary", "Stanford", 45),\
                ("mary", "Campbell", 55),\
                ("jeff", "Ames", 60),\
                ("jeff", "Sunnyvale", 70),\
                ("jane", "Austin", 80)]
                
    #
    print("triplets = ", triplets)
    df = spark.createDataFrame(triplets, ["name", "city", "age"])
    print("df.count(): ", df.count())
    print("df.collect(): ", df.collect())
    df.show()
    df.printSchema()
    #
    #
    triplets2 = [("alex", "software"),\
                 ("alex", "business"),\
                 ("mary", "marketing"),\
                 ("mary", "sales"),\
                 ("jane", "genomics")]
                
    #
    print("triplets2 = ", triplets2)
    df2 = spark.createDataFrame(triplets2, ["name", "dept"])
    print("df2.count(): ", df2.count())
    print("df2.collect(): ", df2.collect())
    df2.show()
    df2.printSchema()

    #-----------------------------------------
    # df.join(df2)
    #-----------------------------------------
    joined = df.join(df2, df.name == df2.name, 'inner')
    joined.show()
    joined.printSchema()  
    
         
    # done!
    spark.stop()

