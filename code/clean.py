import pandas as pd
import numpy as np

def clean_prov_ind(prov_acr: str) -> pd.DataFrame:
    df_prov: pd.DataFrame = pd.read_csv(f'../data/orig/cers/industry-{prov_acr.lower()}.csv')
    df_prov = df_prov.replace({'-': np.nan}).dropna()
    df_prov['period'] = df_prov['period'].map(lambda a : str(a[1]))
    df_prov['industry'] = df_prov['industry'].map(lambda a : str(a).split(' ')[0])
    df_prov['industry'] = df_prov['industry'].replace({'Not': '0'})
    df_prov = df_prov[df_prov['industry'] != 'Total']
    df_prov['count'] = df_prov['count'].map(lambda a : int(a))
    df_prov['amount_paid'] = df_prov['amount_paid'].map(lambda a : float(a))
    df_prov['properties'] = df_prov['properties'].map(lambda a : int(a))
    df_prov['prov'] = prov_acr
    return df_prov

provs = ['bc','ab','sk','mb','on','qc','nb','nl','ns','pe','nu','nt','yk']

dfs = [clean_prov_ind(prov) for prov in provs]

df = pd.concat(dfs)
print(df.sample(5))
df.to_pickle('../data/cers-ind-merged.pkl')
