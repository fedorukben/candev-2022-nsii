import zippyr
import pandas as pd

zippyr.open_zip('../data/ext/businesses.zip', '../data/ext/businesses')
df = pd.read_csv('../data/ext/businesses/33100270.csv')
df = df[['REF_DATE','GEO','Industry','Business dynamics measure','VALUE']].dropna()
df = df.rename(columns={'REF_DATE': 'date','GEO': 'geo','Industry': 'industry','Business dynamics measure': 'measure','VALUE': 'value'})
df['year'] = df['date'].apply(lambda a : int(a[:4]))
df = df[df['year'] >= 2018]
df = df[df['geo'] != 'Canada']
df['geo'] = df['geo'].apply(lambda a : a.split('\xa0')[0].split(', ')[-1])
df = df[df['geo'] != 'Ontario/Quebec']
df.to_pickle('../data/business-merged.pkl')
print(df)
print(df['geo'].unique())
zippyr.close_zip('../data/ext/businesses')
