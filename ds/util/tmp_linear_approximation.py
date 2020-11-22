from sklearn.linear_model import LinearRegression
reg = LinearRegression()

X = df['濃度'].values.reshape(-1,1)
y = df['吸光度']

reg.fit(X, y)

print("intercept: ", reg.intercept_)
print("coefficient: ", reg.coef_)


fig, axes = plt.subplots(figsize=(18,12))
plt.rcParams['font.family'] = 'IPAexGothic'
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
sns.regplot(df['濃度'], df['吸光度'], ci=None, color='Green')
plt.xlabel('濃度(μg/mL)', fontsize=30)
plt.ylabel('吸光度', fontsize=30)
axes.text(400, 0.15, 
          'y='+ str(round(float(reg.coef_),4))+'x+'+str(round(reg.intercept_, 4)), 
          size=30, color='green')
plt.title('図1. 検量線', fontsize=40)
# plt.savefig('/Users/hattoritatsuya/2020年度授業資料/火3_実験/中村研/fig/nakamuralab_day9_fig1.png')
plt.show()