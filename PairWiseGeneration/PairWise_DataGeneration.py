# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:10:39 2018

@author: yeswanth.kuruba
"""

import pandas as pd
from collections import OrderedDict
import itertools

def PairwiseGeneration(inputPath):
    data = pd.read_csv(inputPath,index_col = None)
    Parent = list(OrderedDict.fromkeys(data['Parent'].tolist()))
    pairwise_lists = []
    c = 0
    for par in Parent:
        data_ = data[data['Parent']==par]        
        combinations = list(itertools.combinations(data_['Node'],2))
        dist = len(data_['Node'])
        const = 0
        mandatory = []
        for i in range(1,dist):
            const = const+i
            mandatory.append(len(combinations)-const)
        for i in range(len(combinations)):
            pairwise_list = []#
            pairwise_list.append(c)
            pairwise_list.append(par)
            pairwise_list.append(combinations[i][0])
            pairwise_list.append(combinations[i][1])
            if(i in mandatory):
                pairwise_list.append('Mandatory')
            else:
                pairwise_list.append('Non-Mandatory')
            pairwise_list.append("")
            pairwise_list.append("")
            pairwise_lists.append(pairwise_list)
            c = c+1
    pairwise_data = pd.DataFrame(pairwise_lists,columns = ["Index", "Parent",	"Field A",	"Field B",	"Flag",	"Priority",	"Intensity"]).sort_values('Flag')
    return pairwise_data

if(__name__ == "__main__" ):
    inputPath = "PairWiseGeneration//ahp_hierarchy.csv"
    pairwise_data = PairwiseGeneration(inputPath)
    pairwise_data.to_csv("PairWise_data.csv")