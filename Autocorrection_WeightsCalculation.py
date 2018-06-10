# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 14:07:09 2018

@author: yeswanth.kuruba
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:48:42 2017

@author: yeswanth.kurubapair
"""
import pandas as pd
from collections import OrderedDict
import itertools
import missingMatrixImputation
import consistency_check_weights_calculator

def dataPreparation(inputPath):
    # After filling the Manditory fields and atleast two non-mandatory fields..
    data = pd.read_csv(inputPath,index_col = None)
    Parent = list(OrderedDict.fromkeys(data['Parent'].tolist()))
    all_final_weights = []
    
    for par in Parent:      
        data_ = data[data['Parent']==par].sort_values("Index")
        print("Data for parent Node \'"+par+"\' : \n",data_)
        matrix,miss = missingMatrixImputation.missingMatrix(data_)
        print("Pairwise Comparision Matrix : \n",matrix)
        print("Missing indices : \n",miss)
        Criterias = data_["Field A"][0:1].tolist()+data_["Field B"][0:len(matrix)-1].tolist()
        if(len(matrix)>2):
            correct_matrix,correct_value,correct_index = missingMatrixImputation.missingPairsImputation(matrix,miss)
            if(len(correct_index)!=0):
                print("Please change the values of "+Criterias[correct_index[0]]+" and "+Criterias[correct_index[1]]+" with the value "+str(correct_value))
            else:
                e,weights,max_val = consistency_check_weights_calculator.weights_cal(matrix)  
                for i in range(len(Criterias)):
                    final_weights = []
                    final_weights.append(par)
                    final_weights.append(Criterias[i])
                    final_weights.append(weights[i])
                    all_final_weights.append(final_weights)       
        else:
            e,weights,max_val = consistency_check_weights_calculator.weights_cal(matrix) 
            for i in range(len(Criterias)):
                final_weights = []
                final_weights.append(par)
                final_weights.append(Criterias[i])
                final_weights.append(weights[i])
                all_final_weights.append(final_weights)
                
    allCriterias_weights = pd.DataFrame(all_final_weights,columns = ['Parent','Node','Weights'])
    return allCriterias_weights
            
if(__name__ == "__main__" ):
    inputPath= 'PairWise_data.csv'
    weights = dataPreparation(inputPath)    
    weights.to_csv('calculated_weights.csv',index=False)
