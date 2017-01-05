#!/usr/bin/env python
#
# Li Xin 014696390
# Distributed Systems 2016 
# Big Exercise 4

import os
import sys
from operator import add
from pyspark import SparkConf, SparkContext

### Dataset
DATA1 = '/cs/work/scratch/spark-data/data-1.txt'

### Some variables you may want to personalize
AppName = "BE4"
TMPDIR = "/cs/work/scratch/spark-tmp"

### Creat a Spark context on Ukko cluster
conf = (SparkConf()
        .setMaster("spark://ukko007:7077")
        .setAppName(AppName)
        .set("spark.rdd.compress", "true")
        .set("spark.broadcast.compress", "true")
        .set("spark.cores.max", 10)
        .set("spark.local.dir", TMPDIR))
sc = SparkContext(conf = conf)

def statistics_summary(fn):
    data = sc.textFile(fn)
    data = data.map(lambda s: float(s))
    summary = []
    summary.append(data.mean())
    summary.append(data.max())
    summary.append(data.min())
    summary.append(data.variance())
    return summary


def find_mode(fn):
    data = sc.textFile(fn)
    data = data.map(lambda s: (float(s), 1))
    mode = data.reduceByKey(add).sortBy(lambda s: s[1], False).first()
    return mode

def hist(fn, granularity, length):
    data = sc.textFile(fn)
    # reverse the values to minus and the range to [-100, 0] so that the bucket 
    # limits are exact the same(left start point exclusive, right end point included) 
    # as specified in the problem, which is the reverse of the bucket divison of 
    # histogram() function provided by Spark
    data = data.map(lambda s: -float(s))
    i = -length
    buckets = []
    while (i <= 0):
        buckets.append(i)
        i = i + granularity
    hist = data.histogram(buckets)[1]
    hist.reverse()
    # make items which equal 0 exclusive in the histogram
    zero = data.filter(lambda s: s == 0).count()
    hist[0] = hist[0] - zero

    return hist

if __name__=="__main__":
    #1. calculating the average, variance, max, and min
    summary = statistics_summary(DATA1)
    print("Avg: %f" % summary[0])
    print("variance: %f" % summary[3])
    print("max: %f" % summary[1])
    print("min: %f" % summary[2])

    #2. find the mode
    mode = find_mode(DATA1)
    print("mode: ", mode)

    #3. calculate histogram of different granularity
    f_10 = open('hist_10.txt', 'w')
    f_100 = open('hist_100.txt', 'w')
    f_1000 = open('hist_1000.txt', 'w')
    hist_10 = hist(DATA1, 10, 100)
    hist_100 = hist(DATA1, 1, 100)
    hist_1000 = hist(DATA1, 0.1, 100)

    for i in hist_10:
        f_10.write(str(i) + '\n')
    for i in hist_100:
        f_100.write(str(i) + '\n')
    for i in hist_1000:
        f_1000.write(str(i) + '\n')

    f_10.close()
    f_100.close()
    f_1000.close()

    sys.exit(0)

