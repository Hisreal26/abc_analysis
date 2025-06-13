import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns

df = pd.read_csv("cancer_probabilities.csv")
st.write(df.head(10))

df = pd.read_csv("cancer_probabilities.csv")
st.write(df.tail(10))