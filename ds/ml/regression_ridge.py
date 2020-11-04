from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

ridge = Ridge(random_state=7)
ridge.fit(X_train, y_train)

print(model.__class__.__name__)
print('正解率(train):{:.3f}'.format(model.score(X_train, y_train)))
print('正解率(test):{:.3f}'.format(model.score(X_test, y_test)))