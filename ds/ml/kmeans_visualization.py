import matplotlib.pyplot as plt

# 散布図
plt.scatter()


# clusterごとの棒グラフ
ax = labels.value_counts(sort=False).plot(kind='bar')
ax.set_xlabel('cluster number')
ax.set_ylabel('count')