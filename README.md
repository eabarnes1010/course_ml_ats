# ATS 780A7 - Machine Learning for the Atmospheric Sciences (Colorado State University)
***
Course materials of the python examples (.py), data (.csv,.nc), and jupyter notebooks (.ipynb) used ATS 780A7 Spring 2022. The python examples and their data can just be downloaded and used. For the jupyter notebooks you can:

1. view them directly here in github by clicking on the code directory above
2. use [nbviewer](https://nbviewer.jupyter.org/) to view them by copying the web address for the notebook into the search bar
3. view all of the python notebooks in nbviewer [here](https://nbviewer.jupyter.org/github/eabarnes1010/course_ml_ats/tree/master/code/)

## Tensorflow Code
***
Code was written in python 3.9.7, tensorflow 2.7.0, tensorflow-probability 0.15.0, sklearn 1.0.2 and numpy 1.21.5. 

### Python Environment
```
conda create --name env-hurr-tfp python=3.9
conda activate env-hurr-tfp
pip install tensorflow==2.7.0
pip install tensorflow-probability==0.15.0
pip install --upgrade numpy scipy pandas statsmodels matplotlib seaborn 
pip install --upgrade palettable progressbar2 tabulate icecream flake8
pip install --upgrade keras-tuner sklearn
pip install --upgrade jupyterlab black isort jupyterlab_code_formatter
pip install silence-tensorflow
pip install tqdm
```

## Extra Information
***

### Credits
The majority of the materials were created by [Dr. Elizabeth A. Barnes](https://barnes.atmos.colostate.edu), while additional collaborators are specified in the code when relevant.


### License
This project is licensed under an MIT license.

MIT © [Elizabeth A. Barnes](https://github.com/eabarnes1010)
