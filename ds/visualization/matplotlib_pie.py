# 円グラフ(pie)
import matplotlib.pyplot as plt

# ラベルと値は反時計回りに指定する
labels = ["E", "D", "C", "B", "A"]

y = [10, 20, 30, 40, 50]
# 円グラフからの飛び出し
ex = [0, 0, 0, 0, 0.1]

# 円グラフを描く
plt.pie(y, explode = ex, labels = labels, autopct = '%1.1f%%', startangle = 90)
plt.show()