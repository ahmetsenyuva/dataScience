import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('train.csv') #dosyadan veriler okundu.
print(df)
df.info() 