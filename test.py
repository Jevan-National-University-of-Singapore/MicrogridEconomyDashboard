from scipy.stats import sem
import statistics as st
import math

data_ironcay =[0.83,0.91,0.87,0.86,0.84,0.88,0.83,0.86,0.85,0.87]
ironcay_sd = st.stdev(data_ironcay)
print(sem(data_ironcay)*2)


data_experimental = [0.83,0.84,0.84,0.8,0.84,0.83,0.82,0.83,0.8,0.81]
experimental_sd = st.stdev(data_experimental)
print(sem(data_experimental)*2)

