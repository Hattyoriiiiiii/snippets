from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

# main実行部
sc = StandardScaler()
X_std = sc.fit_transform(cancer.data)

pca = PCA(n_components=2)
pca.fit(X_std)
X_pca = pca.transform(X_std)

print('X_pca shape:{}'.format(X_pca.shape))
print('Explained variance ratio:{}'.format(pca.explained_variance_ratio_))


# 列にラベルをつける
X_pca = pd.DataFrame(X_pca, columns=['pc1', 'pc2'])
X_pca = pd.concat([X_pca, df.target], axis=1)


# ==================================================
# 可視化
pca_nontarget = X_pca[X_pca.target == 0]
pca_target = X_pca[X_pca.target == 1]

plt.scatter(x='pc1', y='pc2', data=pca_nontarget, color='red', label='non_target')
plt.scatter(x='pc1', y='pc2', data=pca_target, color='blue', label='target')
