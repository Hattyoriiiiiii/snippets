import matplotlib.pyplot as plt

# clusterごとの棒グラフ
ax = labels.value_counts(sort=False).plot(kind='bar')
ax.set_xlabel('cluster number')
ax.set_ylabel('count')