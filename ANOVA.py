#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:50:03 2019

@author: nathanielastudillo
"""

'''
An ANOVA script for calculating the F value of a few samples of size n
'''
import numpy as np

def ANOVA(groups): #pass in a list of lists where each sublist is a group
    #data for groups
    groups = groups
    groupMeans = []
    n = len(groups[0])
    N = 0
    SSB = 0 #sum of squares between
    SSE = 0 #sum of squares error
    k=len(groups)
    #calculate N
    for group in groups:
        N += len(group)
    #compute group means
    for group in groups:
        groupMeans.append(np.mean(group))
    #compute total mean
    totalMean = np.mean(groupMeans)
    # calculate SSB
    for mean in groupMeans:
        SSB += n*((mean - totalMean)**2)
    #calculate SSE
    for group in groups:
        mean = np.mean(group)
        for item in group:
            SSE += (item - mean)**2
    #Calculate F Value        
    df1 = k-1
    df2 = N-k
    F = (SSB/df1)/(SSE/df2)
    return(F)


    
    