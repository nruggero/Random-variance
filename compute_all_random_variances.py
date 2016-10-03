import pandas as pd
import numpy as np
import itertools


df = pd.read_csv('Hum2_csv_nick.csv', index_col="Protein ID")

cols = df.columns

sample1 = []
sample2 = []
total_variance = []

for x in itertools.combinations(cols,2):
	first_col = df[x[0]].values.reshape(-1,1)
	second_col = df[x[1]].values.reshape(-1,1)
	variance = np.var( np.hstack((first_col, second_col)) , axis =1 ) 

	sample1.append(x[0])
	sample2.append(x[1])
	total_variance.append(variance.sum())

output_data = {"Sample 1" : sample1,
				"Sample 2" : sample2,
				"Sum of variance" : total_variance}

df_out = pd.DataFrame(output_data, columns = ["Sample 1", "Sample 2", "Sum of variance"])
df_out.to_csv("out.csv")