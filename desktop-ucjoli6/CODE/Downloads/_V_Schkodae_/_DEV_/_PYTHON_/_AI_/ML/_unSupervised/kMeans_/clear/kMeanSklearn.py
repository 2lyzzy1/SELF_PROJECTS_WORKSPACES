import numpy as np
from sklearn.cluster import KMeans

# All matrix have to be 2D Arrays Shape (2, ) : array.ndim = 2

x = [1, 1.5, 3, 5, 3.5, 4.5, 3.5, 4, ]  # col 1
y = [1,   2, 4, 7,   5,   5, 4.5, 4, ]  # col 2

X_zip = list( zip(x, y) )   # samples : tuple

X = np.array([ row for row in X_zip ])  # @ll rows

# --------------------------------------------------------------------

kmeans = KMeans(n_clusters=3, init='random', )

kmeansTrained = kmeans.fit(X=X, )

print(f"\n kmeansTrained : {kmeansTrained} \n")

print(f"\n labels : {kmeansTrained.labels_} \n")

# --------------------------------------------------------------------

predictions = kmeans.predict(X=np.array([[2, 5], [0, 0]], ))    # 2D

print(f"\n predictions : {predictions} \n")

# -------------------------------------------------------------------- # --------------------------------------------------------------------


