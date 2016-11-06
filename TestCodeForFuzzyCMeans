!/usr/bin/python
# Reference Code for normal K-Mean Algo: http://qatar.cmu.edu/~dfossati/15-110-fall12/resources/20121125.kmeans.py
import os
import numpy as np
from collections import defaultdict
import csv
import math
import random
import time
import heapq
import copy

######################################################################
# Input the data resource and convert it into dataset of instances
######################################################################

def loadCSVResource(fileName):
    fileHandler = open(fileName, "rt")
    lines = fileHandler.readlines()
    fileHandler.close()
    dataset = []
    for line in lines:
        instance = lineToTuple(line)
        dataset.append(instance)
    return dataset

# To split a CSV file you can also use Excel tools

def lineToTuple(line):
    cleanLine = line.strip()
    cleanLine = cleanLine.replace('"', '')
    lineList = cleanLine.split(",")
    stringsToNumbers(lineList)
    lineTuple = tuple(lineList)
    return lineTuple

def stringsToNumbers(myList):
    for i in range(len(myList)):
        if (isValidNumberString(myList[i])):
            myList[i] = float(myList[i])

def isValidNumberString(s):
  if len(s) == 0:
    return False
  if  len(s) > 1 and s[0] == "-":
      s = s[1:]
  for c in s:
    if c not in "0123456789.":
      return False
  return True
  
# In this example we use Bensaid dataset 
dataset = loadCSVResource("4-BensaidData.csv")
print "dataset: " + str(dataset)


######################################################################
# Use the data resource for fuzzy clustering
######################################################################


