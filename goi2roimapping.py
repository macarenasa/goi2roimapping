import pandas as pd
import numpy as np
import os
import sys
from scipy.stats import ranksums
from statsmodels.sandbox.stats.multicomp import multipletests
import matplotlib.pyplot as plt

#Ask user to input filepath to load the aggregated MicroArray expression data form the Allen specific to the user
data_input = input("Enter the path for AllenHumanBrainAtlas_agg.csv : ")
     
assert os.path.exists(data_input), "I did not find the file at, "+str(data_input)
f = open(data_input,'r+')
print("Hooray, we found the reference file!")
f.close()

data = pd.read_csv(data_input, header=[0]) #this reads the reference .csv MicroArray expression data form the Allen
data.insert(0, "target", False) #inserts a new column to the data set called "target"; Inserts a value to all rows of "False"
print('Reference data set loaded...')

#ask user to input genes.
genes=input('Enter genes of interest (goi) acronyms (separated by commas, no spaces):') #specifying here the input type
genes=genes.split(',')

#set the target as True on those rows that match the gene_symbol and the selected genes
data['target'] = data['gene_symbol'].isin(genes)


#Create an empty dataframe, with the necessary columns to store the results
genes_mask=data["target"]
mapping_result = pd.DataFrame(columns=['region_id','p-value', 'corrected_p-value'])

print("Performing multiple comparisons (ranksums) now...")

#Loop through all columns in MicroArray except the target and gene_symbol column
for column in  data.loc[:, ~data.columns.isin(['target', 'gene_symbol'])]:
    genes_region=data[column]
    genes_true=genes_region[genes_mask]
    genes_false=genes_region[~genes_mask]
    ranksums_result=ranksums(genes_true, genes_false)[1]
    result_row = [column,ranksums_result,'']
    mapping_result.loc[len(mapping_result)] = result_row

print("Performing Bonferroni correction...")

#Bonferroni correction of results
mapping_result["corrected_p-value"] = multipletests(mapping_result["p-value"], method='bonferroni')[1] #bonferroni correction of results

print("Done!")


#Setting the filepath specific to the user to find Brain_Regions.csv
brainregions_input = input("Enter the path for Brain_Regions.csv: ")
     
assert os.path.exists(brainregions_input), "I did not find the file at, "+str(brainregions_input)
f = open(brainregions_input,'r+')
print("Hooray! Brain ROIs found!")
f.close()

#Lad key to brain regions by reading in the csv
brainregions = pd.read_csv(brainregions_input, header=[0])
print('Brain Regions loaded. Generating outputs...')

#rename rows in mapping_result to match brain regions in brainregions
mapping_result = mapping_result.merge(brainregions,on='region_id',how="left")

#make and export boxplots of signiicant brain regions 
#select all values from "data" for which region_id in "mapping_result" have p<0.05
df4 = data[data.columns.intersection(mapping_result.loc[mapping_result['p-value'].lt(0.05), 'region_id'])]

df5 = df4.join(data["gene_symbol"])

df6 = df5.join(data["target"])
    
boxplot = df6.boxplot(by='target', figsize=(12,15))

plt.savefig("comparison_plots.jpg", format="jpg")
print("Comparison plot exported as .jpg to working directory:",os.getcwd())

#export list of ROIs to csv
mapping_result.to_csv('goi2roimapping_results.csv', index=False)
print("Exported .csv to working directory:",os.getcwd())
