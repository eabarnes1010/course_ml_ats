# ATS 780A7 - Machine Learning for the Atmospheric Sciences (Colorado State University)
***
Course materials of the python examples (.py), data (.csv,.nc), and jupyter notebooks (.ipynb) used in ATS 780A7 SP22, F23. The python examples and their data can just be downloaded or run on Google's Colaboratory.

## Tensorflow Code
***
Code was written on an Apple M1 Max chip using python 3.10, tensorflow 2.7.0, and tensorflow-probability 0.15.0.

### Python Environment
```
- conda create --name env-780A7f23 python=3.10.10
- conda activate env-780A7f23
- conda install -c apple -c conda-forge -c nodefaults tensorflow-deps
- python -m pip install tensorflow-macos==2.10.0
- python -m pip install tensorflow-metal==0.6.0
- pip install tensorflow-probability==0.15 silence-tensorflow
- conda install numpy scipy matplotlib scikit-learn jupyterlab
- pip install pandas statsmodels icecream palettable seaborn progressbar2 tabulate isort
- pip install tqdm pydot graphviz
- pip install -U scikit-image
- pip install shap
```

## Extra Information
***

### Credits
The majority of the materials were created by [Dr. Elizabeth A. Barnes](https://barnes.atmos.colostate.edu), while additional collaborators are specified in the code when relevant.


### License
This project is licensed under an MIT license.

MIT © [Elizabeth A. Barnes](https://github.com/eabarnes1010)
