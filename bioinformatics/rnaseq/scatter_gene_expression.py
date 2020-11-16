import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_1 = pd.read_csv('', sep='\t')
df_1 = df_1.drop(columns=[])
# df = df[['Geneid', 'PS_totalRNA_rep1_tpm', 'PS_totalRNA_rep2_tpm']]

df_1.columns = ['target_id', 'TPM_rep1']

df_2 = pd.read_csv('', sep='\t')
df_2 = df_2.drop(columns=[])
df_2.columns = ['target_id', 'TPM_rep2']

df = pd.merge(df_1, df_2, on='target_id')
df['log_rep1'] = np.log10(df.TPM_rep1 + 1)
df['log_rep2'] = np.log10(df.TPM_rep2 + 1)
df['diff'] = df['log_rep1'] - df['log_rep2']
# df['diff'] = abs(df['log_rep1'] - df['log_rep2'])

fig = plt.figure(figsize=(12,12))
plt.scatter(df.log_rep1, df.log_rep2)
plt.xlabel('log_rep1')
plt.ylabel('log_rep2')
fig.savefig('log.png')
