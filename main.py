import pandas as pd
import numpy as np




def dataSet():
    df = pd.read_csv("/Users/stephenthomas/desktop/homePrice/Train.csv")
    return df
    
    
print(dataSet())



