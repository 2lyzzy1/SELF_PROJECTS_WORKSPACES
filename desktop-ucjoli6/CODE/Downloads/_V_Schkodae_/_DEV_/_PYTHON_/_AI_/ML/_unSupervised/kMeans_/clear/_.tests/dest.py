import numpy as np
import pandas as pd

# All matrix have to be 2D Arrays Shape (2, ) : array.ndim = 2
x = [1, 1.5, 3, 5, 3.5, 4.5, 3.5, 4, ]  # col 1
y = [1,   2, 4, 7,   5,   5, 4.5, 4, ]  # col 2
z = [1,   2, 4, 7,   5,   5, 4.5, 4, ]  # col 2

# - treating data ---------------------------------------
X_zip = list( zip(x, y, z) )   # samples : tuple
print(f"\n X_zip : {X_zip}")
X = np.array([ row for row in X_zip ])  # @ll rows
print(f"\n X : {X}")

# -
data = list( zip(*X) )
print(f"\n data : {data}")
"""
x_ = data[0]
y_ = data[1]
print(f"\n x_ : {x_} \n y_ : {y_} ")"""

df = pd.DataFrame(data=X, columns=[f"ax{idx+1}" for idx in range(X.shape[1])], index=[f"d{idx+1}" for idx in range(X.shape[0])])
print(f"\n df :\n{df}")

print(f"\n df.where(cond=(df['ax1'] == 5)) : \n{df.where(cond=(df['ax1'] == 5))}\n")
print(f"\n df.where(cond=(df['ax1'] == 5)).index : \n{df.where(cond=(df['ax1'] == 5)).index}\n")

