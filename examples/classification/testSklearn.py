from algotimer import Timer, TimerPloter
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

with Timer('GaussianNB, Train'):
    gnb = GaussianNB()
    clf = gnb.fit(iris.data, iris.target)

with Timer('GaussianNB, Test'):
    y_pred = clf.predict(iris.data)
    print("Number of mislabeled points out of a total %d points : %d"
        % (iris.data.shape[0], (iris.target != y_pred).sum()))

with Timer('KNN(K=3), Train'):
    neigh = KNeighborsClassifier(n_neighbors=3)
    clf = neigh.fit(iris.data, iris.target) 

with Timer('KNN(K=3), Test'):
    y_pred = clf.predict(iris.data)
    print("Number of mislabeled points out of a total %d points : %d"
        % (iris.data.shape[0], (iris.target != y_pred).sum()))

with Timer('KNN(K=5), Train'):
    neigh = KNeighborsClassifier(n_neighbors=5)
    clf = neigh.fit(iris.data, iris.target) 

with Timer('KNN(K=5), Test'):
    y_pred = clf.predict(iris.data)
    print("Number of mislabeled points out of a total %d points : %d"
        % (iris.data.shape[0], (iris.target != y_pred).sum()))

# plot it
ploter = TimerPloter()
ploter.plot()
