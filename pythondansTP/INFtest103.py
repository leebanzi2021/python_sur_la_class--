import numpy as np 
import matplotlib.pyplot  as  plt 
import matplotlib.image  as  img 
from sklearn.datasets import fetch_openml
 
np.sqrt(2)
X,y = fetch_openml(name= 'Fashion-MNIST',version=1 , return_X_y = True )

