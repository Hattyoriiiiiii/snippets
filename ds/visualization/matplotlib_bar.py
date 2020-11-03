# 棒グラフ(bar)
import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D", "E", "F"]
x = range(0, 6)
y = [10, 20, 30, 40, 50, 60]
# 棒グラフを描画する
plt.bar(x, y, tick_label = labels)
plt.show()