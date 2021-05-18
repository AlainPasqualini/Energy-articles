import streamlit as st 
import pandas as pd 
import numpy as np 
import pydeck as pdk 


#from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
def display(l):
    return df.head(l)
interact(display,l=2)

#this shouls work
