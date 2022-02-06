import pandas as pd

df = pd.read_pickle('../data/business-merged.pkl')
df['industry'] = df['industry'].apply(lambda a : a.split('[')[-1][:-1])
df.to_pickle('../data/business-merged.pkl')
