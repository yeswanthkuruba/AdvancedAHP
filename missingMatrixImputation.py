# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:48:36 2018

@author: yeswanth.kuruba
"""
import pandas as pd
import numpy as np
from collections import OrderedDict
import scipy.optimize as sciopt
import math
import consistency_check_weights_calculator

def missingMatrix(data_):
    
    priority = data_["Priority"].tolist()
    intensity = data_["Intensity"].tolist()
    Criterias_all = data_["Field A"].tolist() + data_["Field B"].tolist()
    intensity_new = []
    for i,j in zip(priority,intensity):
        #print i
        if(pd.isnull(i)):
            intensity_new.append(0)
        elif(i == "A"):
            intensity_new.append(j)
        else:
            intensity_new.append(1./j)
    
    Criterias = list(OrderedDict.fromkeys(Criterias_all))
    Criteria_len = len(Criterias)
    
    Matrix_U = np.ones((Criteria_len,Criteria_len),float)
    indices = np.triu_indices(Criteria_len,k=1.)
    Matrix_U[indices] = intensity_new
    miss = np.argwhere(Matrix_U == 0)
    Matrix_U[Matrix_U == 0] = 1
    matrix = np.triu(Matrix_U) + np.tril(1./Matrix_U.T, k = -1)
    return matrix,miss

def missingPairsImputation(a,miss):
    CR_list = []
    b = a.reshape(len(a)*len(a))
    for val in range(len(b)):
        for m in miss:
            popt = sciopt.fminbound(consistency_check_weights_calculator.lammax, consistency_check_weights_calculator.pmin, consistency_check_weights_calculator.pmax, args=(b,m[0],m[1]))
        a = b.reshape(int(math.sqrt(len(b))),int(math.sqrt(len(b))))
        e,weights,max_val = consistency_check_weights_calculator.weights_cal(a)
        CR = consistency_check_weights_calculator.consistency_check(a.shape[0],max_val)
        CR_list.append(CR) 
        if(val>1 and round(CR_list[val],5)==round(CR_list[val-1],5)):
            break
    if(CR<consistency_check_weights_calculator.min_CR):
        #print('Consistant and call your rest of the code')
        correct_matrix,correct_value,correct_index = [],[],[]
    else:
        correct_matrix,correct_value,correct_index = consistency_check_weights_calculator.CorrectedMatrix(b)
        print('inconsistant matirx please change values as suggested')
        print(correct_value,correct_index)

    return correct_matrix,correct_value,correct_index

