import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_pickle('../data/cers-ind-merged.pkl')
print(df.sample(5))
