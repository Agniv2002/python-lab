import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy import stats 



#scatter plot
def scatter(data,x,y):
    plt.figure()
    plt.scatter(data[x],data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("hi there")
    plt.show()


def mean(data):
    return np.mean(data)
def median(data):
    return np.median(data)
def std(data):
    return np.std(data)
def var(data):
    return np.var(data)

def calculate_Regression(data,x,y):
    plt.figure()
    slope,intercept,c,d,e=stats.linregress(data[x],data[y])
    plt.scatter(data[x],data[y])
    plt.plot(data[x],slope*data[y]+intercept)
    plt.title(f"Regression Line for {x} and {y}")
    plt.show()

data=pd.read_csv("iris.csv")
x="SepalLengthCm"
y="PetalLengthCm"
scatter(data,x,y)
mean(data[y])
median(data[y])
var(data[y])
std(data[y])
calculate_Regression(data,x,y)