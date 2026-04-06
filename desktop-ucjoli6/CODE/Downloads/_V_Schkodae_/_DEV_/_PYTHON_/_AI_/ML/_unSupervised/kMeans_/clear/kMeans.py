from typing import (
    Any, Literal
)
# from copy import deepcopy
import random as rd
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt


class kMeans:
    """
- sklearn min docs :
    **Notes**

The k-means problem is solved using either Lloyd’s or Elkan’s algorithm.\n
The average complexity is given by ***O(k n T)***, where *n* is the number of samples and *T* is the number of iteration.\n
The worst case complexity is given by ***O(n^(k+2/p))*** with *n = n_samples*, *p = n_features*. Refer to [“How slow is the k-means method?” D. Arthur and S. Vassilvitskii - SoCG2006.](https://doi.org/10.1145/1137856.1137880) for more details.\n
In practice, the k-means algorithm is very fast (one of the fastest clustering algorithms available), but it falls in local minima. That’s why it can be useful to restart it several times.\n
If the algorithm stops before fully converging (because of **tol** or **max_iter** ), **labels_** and **cluster_centers_** will not be consistent, i.e. the **cluster_centers_** will not be the means of the points in each cluster. Also, the estimator will reassign **labels_** after the last iteration to make **labels_** consistent with **predict** on the training set.\n

    **Examples**
    
```
>>> from sklearn.cluster import KMeans
>>> import numpy as np
>>> X = np.array([[1, 2], [1, 4], [1, 0],
...               [10, 2], [10, 4], [10, 0]])
>>> kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
>>> kmeans.labels_
array([1, 1, 1, 0, 0, 0], dtype=int32)
>>> kmeans.predict([[0, 0], [12, 3]])
array([1, 0], dtype=int32)
>>> kmeans.cluster_centers_
array([[10.,  2.],
       [ 1.,  2.]])
```
For examples of common problems with K-Means and how to address them see  [Demonstration of k means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py).\n
For a demonstration of how K-Means can be used to cluster text documents see  [Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py).\n
For a comparison between K-Means and MiniBatchKMeans refer to example  [Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#sphx-glr-auto-examples-cluster-plot-mini-batch-kmeans-py).\n
For a comparison between K-Means and BisectingKMeans refer to example  [Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html#sphx-glr-auto-examples-cluster-plot-bisect-kmeans-py).\n

- src : [KMeans — scikit-learn 1.8.0 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans) \n
    """
    
    def __init__(self, k_clusters:int=5, kDetMethod:str|Literal['elbow', 'auto', ]=None, centroidSelectionMethod:str|Literal['randomly', 'man_input', ]='randomly', *, iterNbr:int=7, ):
        """
        **__INIT__** : *with*   *>*
        ```
        def __init__(self, k_clusters:int=5, kDetMethod:str='elbow', centroidSelectionMethod:str='randomly'or'man_input', *, iterNbr:int=7, ): ...
        ```
        **__END__** ***docs***  *<*
        """
        self.k_clusters = k_clusters    # Number of cluster(s) to generate or build
        self.kDetMethod = kDetMethod    # How can algo. have to choose or help to fix k (n_clusters) to do cluster optimal ?!
        self.centroidSelectionMethod = centroidSelectionMethod  # 
        self.ITERlim = iterNbr  # Max or lim_Iteration after enventual convergence or not
        """ ***Max number of iterations run after eventual convergence.*** """
        # - Datas - Points | Centers - distMetrics - centers Samples -
        self.XdNDArray : np.ndarray = None      # data to be clustered - Array | MatrixLike
        self.datasetCp : pd.DataFrame = None    # data to be clustered - Matrix | DataFrame
        """```self.datasetCp = pd.DataFrame({
            'lPoints': [],  # letters
            'iPoints': [],  # dataPoints
        }) # wasted
        ```"""
        self.centroids = pd.DataFrame({
            'init': [ () for idx in range(k_clusters) ],     #initialz
            'tUpdated': [ () for idx in range(k_clusters) ], #training
            'pUpdated': [ () for idx in range(k_clusters) ], #prediction
            }, # #1 init
            index=[ f"C{idx}" for idx in range(k_clusters) ]
        )   # n | k
        self.distanceSet : pd.DataFrame = None  # update
        """```self.distanceSet = pd.DataFrame({
            'letters': [],
            # add later the others ...
            'dCi': [],
        })   # update
        ```"""
        self.clusters = pd.DataFrame({  # CLASSES
            'name': [ f"Class_{idx}" for idx in range(k_clusters) ], # class i
            #'number': [ idx for idx in range(k_clusters) ],   # i
            'asgPointsLtrs': [ [] for idx in range(k_clusters) ],    # : str = 'Oi'
            'asgPointsCoords': [ [] for idx in range(k_clusters) ],  # : tuple = (x, y, ..., µ)
        })  # initVid
        # - eval Metrics -
        self.Inertia = 0.0  # Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.
        """ ***Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.*** """
        self.silouhetteScoreCluster = None  # 'Oi' by 'Oj'
        self.silouhetteScoreGlobal = 0.0    # Mean of individualz Si - Silouhette Scores
        # -
    # - ---------------------------------------------------------------------------------------¤$
    # - INIT
    def __init__sysData__(self,
                          data:Any|list|np.ndarray|dict|pd.Series|pd.DataFrame=None, ):
        self.XdNDArray = np.array(data) # - 1
        self.datasetCp = pd.DataFrame(data=data, columns=[f"ax{idx+1}" for idx in range(data.shape[1])], index=[f"data{idx+1}" for idx in range(data.shape[0])]) # - 2
    
    # - --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------¤$
    # - TRAINING
    def fit_(self, X:Any|list|np.ndarray, y:Any|list|np.ndarray=None, ):
        self.traininModel = True
        self.__init__sysData__(data=X, )
        # print(f"\nX_dFrame : \n{self.datasetCp}\n")
        # print(f"\nX_dArray : \n{self.XdNDArray}\n")
        # print(f"\nClusters : \n{self.clusters}\n")
        self.selectInitCentroids()
        return f"\n{self}\nkMeans(k_clusters={self.k_clusters}, kDetMethod={self.kDetMethod}, centroidSelectionMethod={self.centroidSelectionMethod}, iterNbr={self.ITERlim})\n"
    
    # - --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------¤$
    # - ALGO. MAIN STEPS -> derivated from LOOP | -> @override : 'move into kmeansLoop() method'
    def selectInitCentroids(self, ):
        """ Select k centroids *randomly* or *by user input* ('man_input') """
        if self.centroidSelectionMethod == 'randomly':
            # dataset_ = self.datasetCp.to_dict(orient='records')   # -
            dataset_ = self.XdNDArray.tolist()
            self.centroids['init'] = pd.Series(data=rd.sample(population=dataset_, k=self.k_clusters),
                                               index=[ f"C{idx}" for idx in range(self.k_clusters) ])
            if self.traininModel: self.centroids['tUpdated'] = self.centroids['init'].copy()
        if self.centroidSelectionMethod == 'man_input':
            self.centroids['init'] = pd.Series(data=input(f"format : [[Xi, ...], ...]\n-> "),
                                               index=[ f"C{idx}" for idx in range(self.k_clusters) ])
            if not self.traininModel: self.centroids['pUpdated'] = self.centroids['init'].copy()
        print(f"\nCentroids : \n{self.centroids}\n")
    
    def calculateDistance(self, dataPoints:Any):
        for cet in self.centroids['tUpdated']:
            euclideanDistance = np.sqrt(  )
        ...
    
    def assignPoints2Clusters(self, ):
        ...
    
    def findNewCentroids(self, ):
        ...
    
    # - --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------¤$
    # - METRICS
    def detInertia(self, ):
        ...
    
    def detSilhouetteScore(self, ) -> float:
        return self.silouhetteScoreGlobal
    
    # - --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------¤$
    # - PREDICTIONS
    def predict_(self, X:Any|list|np.ndarray, y:Any|list|np.ndarray=None, ):
        predictions = []    # -
        dataUnClass = np.array(X)   # -
        return predictions

    # - --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------¤$
    # - ALGO. LOOP
    def iterLoop(self, ):
        ...

    """def mainExample(self, ):
        kmeans = kMeans(
            k_clusters=3,
            clusterSelectionMethod='randomly',
            iterNbr=5,
        )"""
    # - --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------¤$

if __name__ == '__main__':
    kmeans = kMeans()
    # kmeans.mainExample()

#