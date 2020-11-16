from sklearn.metrics import silhouette_samples
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt


cluster_labels = np.unique(y_kmeans)
n_clusters = cluster_labels.shape[0]

# シルエット係数の計算
silhouette_vals = silhouette_samples(childrenk, y_kmeans, metric='euclidean')
# サンプルデータ、クラスター番号、ユークリッド距離でシルエット係数の計算
y_ax_lower, y_ax_upper = 0, 0
y_ticks = []

for i, c in enumerate(cluster_labels):
    # cluster_labelsには0-5の値が入る
    c_silhouette_vals = silhouette_vals[y_kmeans==c]
    c_silhouette_vals.sort()
    # サンプルの個数をグループごとに足してy軸の最大値を決定
    y_ax_upper += len(c_silhouette_vals)
    # 色の値を作る
    color = cm.jet(float(i)/n_clusters)
    """
    # 棒グラフの描画
    range : (底辺の範囲を指定)
    c_silhouette_vals : 棒の幅(1サンプルを表す)
    height : 棒の高さ
    edgecolor : 棒の端の色
    color : 棒の色
    ======================
    棒グラフの幅を指定して、その位置を使ってylabels
    """
    plt.barh(range(y_ax_lower, y_ax_upper), c_silhouette_vals, height=1.0, edgecolor='none', color=color)
    yticks.append((y_ax_lower + y_ax_upper) / 2)    # ラベルの表示位置
    y_ax_lower += len(c_silhouette_vals)            # 底辺の値に棒の幅を追加
    print('グループ', i+1, ', シルエット係数平均', np.mean(c_silhouette_vals),'個数', len(c_silhouette_vals))
    # print(f'グループ {i+1}, シルエット係数平均 {np.mean(c_silhouette_vals)} 個数 {len(c_silhouette_vals)}')

silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg, color='red', linestyle='==')
plt.yticks(yticks, cluster_labels + 1)
plt.ylabel('クラスタ')
plt.xlabel('シルエット係数')
plt.show()