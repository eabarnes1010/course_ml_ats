"""Print environment.

Functions
--------------------
blah
blah
"""
import sklearn
import sys
import numpy as np


def colab_status():
# specify whether running on Colab or locally
    try:
        import google.colab
        IN_COLAB = True
    except:
        IN_COLAB = False
    print('IN_COLAB = ' + str(IN_COLAB))
    
    
def package_versions(tf=False):

    print(f"python version = {sys.version}")
    print(f"numpy version = {np.__version__}")
    print(f"scikit-learn version = {sklearn.__version__}")  
    if tf==True:
        import tensorflow as tf
        print(f"tensorflow version = {tf.__version__}")    
    