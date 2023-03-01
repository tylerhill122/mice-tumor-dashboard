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
    drug_df = df.groupby("Drug Regimen")
    drug_summary_df = drug_df.agg(["mean","median","var","std","sem"])["Tumor Volume (mm3)"]
    return drug_summary_df.to_html()