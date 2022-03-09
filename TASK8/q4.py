import numpy as ns
import pandas as pd 

ser = pd.Series(['amrita','school','of','engineering','chennai','campus'])
st = ser.str.capitalize()

for i in st:
    print(i,end= " ")