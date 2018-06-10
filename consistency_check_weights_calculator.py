# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:51:31 2018

@author: yeswanth.kuruba
"""

import numpy as np
import math

pmin = 0.11111 # mimimum bound
pmax = 9 # maximum bound
min_CR = 0.1

def lammax(p,a,i,j):
    b = a.reshape(int(math.sqrt(len(a))),int(math.sqrt(len(a))))
    b[i][j] = p
    b[j][i] = 1.0/p
    eigenvalues =np.linalg.eigvals(b)
    lam_max=np.max(eigenvalues)
    return lam_max

def weights_cal(a):
    
    eigenvalues, eigenvector=np.linalg.eig(a)
    max_index=np.argmax(eigenvalues)
    max_val=np.max(eigenvalues)
    eigenvector=np.float32(eigenvector)
    weights=eigenvector[:, max_index]
    weights = weights.tolist()
    weights=[ w/sum(weights) for w in weights ]
    i=0
    e = np.zeros(shape=(len(a),len(a)))
    for i in range(len(a)):
        j=0
        for j in range(len(a)):
            e[i,j]=float(a[i,j])*float(weights[j])/float(weights[i])
    return e,weights,max_val

def CorrectedMatrix(a):
    print('Corrected Matrix',a,len(a))
    a = a.reshape(int(math.sqrt(len(a))),int(math.sqrt(len(a))))
    e,weights,max_val = weights_cal(a)
    i = (-e).argsort(axis=None, kind='mergesort')
    j = np.unravel_index(i, e.shape) 
    list_ = np.vstack(j).T
    print("List :",list_)
    new_matrix = a   
    a[list_[0][0],list_[0][1]] = 0
    a[list_[0][1],list_[0][0]] = 0
    a[list_[0][0],list_[0][0]] = 2
    a[list_[0][1],list_[0][1]] = 2
    
    e,weights,max_val = weights_cal(a)
    
    replace_value = weights[list_[0][0]]/weights[list_[0][1]]
    
    if(replace_value>=1):
        new_matrix[list_[0][0],list_[0][1]] = round(replace_value)
        new_matrix[list_[0][1],list_[0][0]] = 1.0/round(replace_value)
    else:
        new_matrix[list_[0][0],list_[0][1]] = 1.0/round(1.0/replace_value)
        new_matrix[list_[0][1],list_[0][0]] = round(1.0/replace_value)
    
    return new_matrix,new_matrix[list_[0][0],list_[0][1]],(list_[0][0],list_[0][1])

def consistency_check(n,lambda_max):
    key = {'2':0.00,'3':0.58,'4':0.9,'5':1.12,'6':1.24,'7':1.32,'8':1.41,'9':1.45,'10':1.51}
    if (n!=1):
        RI=key[str(n)]
        CI= (lambda_max-n)/(n-1)
        CR = CI/RI
        if CR < min_CR :
            print("Consistent combinations CR: ",CR)
        else :
            print("Inconsistent please check the combinations CR: ",CR)
    else:
        print("Consistent ..")
    return CR
