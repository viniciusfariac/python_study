from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as pls

x,y = make_regression(n_samples=200, n_features=1, noise=30)
model = LinearRegression()
model.fit(x,y)

pls.scatter(x,y)
pls.title("Regressions data")
pls.xlabel("characteristics (x)")
pls.xlabel("Target   (y)")
pls.plot(x, model.predict(x), color="red", linewidth=3)

pls.show()

