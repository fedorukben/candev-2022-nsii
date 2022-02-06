import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_pickle('../data/business-merged.pkl')

# df = df[df['industry'] == 'Transportation and warehousing [48-49]']
df = df[df['measure'] != 'Closing businesses']
df = df[df['year'] >= 2020]

for industry in df['industry'].unique():
    df2 = df.copy(deep=True)
    df2 = df2[df2['industry'] == industry]
    sns.lineplot(data=df2, x='date', y='value')
    # plt.show()

plt.show()
print(df['industry'].unique())

