#!/usr/bin/python

import os
import numpy as np
from collections import defaultdict
import math
import random
import time
import heapq
import copy
import csv
import skfuzzy as fuzz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


######################################################################
# References
# Implementation Code for normal K-Mean Algo: 
# http://qatar.cmu.edu/~dfossati/15-110-fall12/resources/20121125.kmeans.py
######################################################################



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
    #print dataset
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
# Fuzzy skfuzzy.cmeans
# https://github.com/scikit-fuzzy/scikit-fuzzy/blob/master/docs/examples/plot_cmeans.py
######################################################################

# Test data generation
# Define three cluster centers
centers = [[4, 2],
           [1, 7],
           [5, 6]]
           
# Define three cluster sigmas in x and y, respectively
sigmas = [[0.8, 0.3],
          [0.3, 0.5],
          [1.1, 0.7]]
           
# Generate test data
np.random.seed(42)  # Set seed for reproducibility
xpts = np.zeros(1)
ypts = np.zeros(1)
labels = np.zeros(1)
for i, ((xmu, ymu), (xsigma, ysigma)) in enumerate(zip(centers, sigmas)):
    xpts = np.hstack((xpts, np.random.standard_normal(200) * xsigma + xmu))
    ypts = np.hstack((ypts, np.random.standard_normal(200) * ysigma + ymu))
    labels = np.hstack((labels, np.ones(200) * i))

alldata = np.vstack((xpts, ypts))
print "alldata: " + str(alldata)

fig1, axes1 = plt.subplots(3, 3, figsize=(8, 8))
    
fpcs = []

for ncenters, ax in enumerate(axes1.reshape(-1), 2):
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(dataset, ncenters, 2, error=0.005, maxiter=1000, init=None)

# Store fpc values for later
fpcs.append(fpc)
    
print "fpcs: " + str(alldata)
