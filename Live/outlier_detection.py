import matplotlib.pyplot as plt
import numpy as np
multiple_dataset = [[11,23,33,44,104,22,55,44],[10,20,150,40,20,50,30,50],[12,21,150,45,21,52,31,53]]


outlier_indices = []
mean = np.mean(multiple_dataset[1])
std = np.std(multiple_dataset[1])
zscore_formula = np.abs(list(((i-mean)/std) for i in multiple_dataset[1]))
#print(zscore_formula)

for i in range(len(zscore_formula)):
    if zscore_formula[i] > 2:
        outlier_indices.append(i)


outliers = [multiple_dataset[1][i] for i in outlier_indices]
print(outliers)
multiple_dataset[1][2]