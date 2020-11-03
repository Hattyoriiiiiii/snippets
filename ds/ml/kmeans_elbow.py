# elbow methodによるクラスター数の決定
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 距離の総和を求める
start, end = 1, 10
dist_list = []
for i in range(start, end):
    kmeans = KMeans(n_clusters=i, init='random', random_state=7)
    kmeans.fit(X)
    dist_list.append(kmeans.inertia_)

# 可視化
plt.plot(range(start, end), dist_list, marker='+')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')