from kMeans import kMeans
import numpy as np

# All matrix have to be 2D Arrays Shape (2, ) : array.ndim = 2
x = [1, 1.5, 3, 5, 3.5, 4.5, 3.5, 4, ]  # col 1
y = [1,   2, 4, 7,   5,   5, 4.5, 4, ]  # col 2

# - treating data ---------------------------------------
X_zip = list( zip(x, y) )   # samples : tuple

X = np.array([ row for row in X_zip ])  # @ll rows

# - @Self kMeans model
kmeans = kMeans(k_clusters=2,
                centroidSelectionMethod='randomly',
                iterNbr=5,
                )

"""
# kmeans.fit_(X=np.array([x,y,]), )
kmeans.fit_(X=[np.array(x)[:5], np.array(y)[:5], ], )

kmeans.predict_(X=[np.array(x)[5:], np.array(y)[5:], ], )"""

# --------------------------------------------------------------------
# - Training Model on Data
kmeansTrained = kmeans.fit_(X=X, )
print(f" kmeansTrained : {kmeansTrained} \n")

# --------------------------------------------------------------------
# - |
# kmeans.selectInitCentroids()

# --------------------------------------------------------------------
# - Predicting many Class
predictions = kmeans.predict_(X=np.array([[2, 5, ]], ))
print(f" predictions : {predictions} \n")

# -------------------------------------------------------------------- # --------------------------------------------------------------------

"""c1 = (3, 4)
c2 = (4.5, 5)"""

"""
d = m.sqrt( sum( pow( diff(xi - xj), 2) ) )

=RACINE( SOMME(SOMME.CARRES(C12;-C3); SOMME.CARRES(D12;-D3) ) )

=RACINE( SOMME( SOMME.CARRES(F5;-D8); SOMME.CARRES(G5;-E8) ) )

=RACINE( SOMME( SOMME.CARRES(H5;-D8); SOMME.CARRES(I5;-E8) ) )"""

"""
import pandas as pd
import random as rd

dDict = {
    'x': [1, 1.5, 3, 5, 3.5, 4.5, 3.5, 4, ],
    'y': [1,   2, 4, 7,   5,   5, 4.5, 4, ],
}

# self.clusters = rd.sample(population=)

dFrame = pd.DataFrame(data=dDict)
dListDict = dFrame.to_dict(orient='records')

print(f" dFrame : \n {dFrame} \n")
print(f" dListDict : \n {dListDict} \n")

clusters = rd.sample(population=dListDict, k=3)

print(f" clusters : \n {clusters} \n")
"""



