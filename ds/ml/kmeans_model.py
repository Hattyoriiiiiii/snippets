from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn import preprocessing 

# データのimportとcolumnの選択
df = pd.read_csv('')
X = df[['column_1', 'column_2']]

# 前処理
sc = preprocessing.StandardScaler()
sc.fit(X)
X_norm = sc.transform(X)

# kmeansモデルの作成
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=7)
# クラスターの重心
result = kmeans.fit()


# クラスター番号の予測
y_pred = kmeans.predict(X)

# クラスター番号をpandasのSeriesで保持
labels = pd.Series(kmeans.labels_, name='cluster_number')
print(labels.value_counts(sort=False))

# 元データにクラスター番号の結合
df_merge = pd.concat([df, labels], axis=1)