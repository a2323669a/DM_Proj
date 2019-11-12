import numpy as np
import pandas as pd

df = pd.read_csv("./topic_embed.csv", sep=" ")
#%%
data = df.values.reshape((-1,))
#%%
indexs = [int(i) for i in data[0].split(',')]
