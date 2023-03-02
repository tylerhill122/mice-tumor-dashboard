import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import random

# Import JSON data
mouse_data_path = "static/data/mouse_data.json"

# Read into Pandas as a DataFrame
df = pd.read_json(mouse_data_path)

# Summary Stats function
def summary_stats():
    new_df = df.drop(columns=['Mouse ID', 'Sex'])
    drug_df = new_df.groupby("Drug Regimen")
    drug_summary_df = drug_df.agg(["mean","median","var","std","sem"])["Tumor Volume (mm3)"]
    return drug_summary_df.to_html()

def data_prep(x):
    data_instance = {'item': [],'value': []}
    for index, value in x.items():
        data_instance['item'].append(index)
        data_instance['value'].append(value)
    return data_instance

# Bar Chart function
def barchart():
    timepoint = df['Drug Regimen'].value_counts()
    return data_prep(timepoint)

# Pie Chart function
def pie():
    sex_counts = df["Sex"].value_counts()
    return data_prep(sex_counts)