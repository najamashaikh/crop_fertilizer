import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

crop = pd.read_csv("Dataset/Crop_recommendation.csv")

crop.head() 
crop.tail() 
crop.shape 
crop.info() 
crop.isnull()
crop.isnull().sum() 
crop.duplicated() 
crop.duplicated().sum() 
crop.describe() 
crop.columns 
crop['label'].value_counts() 