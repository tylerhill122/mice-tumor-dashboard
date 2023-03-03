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

# Calculate the final tumor volume of each mouse across four of the treatment regimens:
# Capomulin, Ramicane, Infubinol, and Ceftamin
# Start by getting the last (greatest) timepoint for each mouse
mouseid = pd.DataFrame(df.groupby(["Mouse ID"])["Timepoint"].max())
# Merge this group df with the original dataframe to get the tumor volume at the last timepoint
new_mouse_df = pd.merge(df, mouseid, on="Mouse ID")
new_mouse_df.head()

# IQR and outlier calculation
def iqr():
    # Put treatments into a list for for loop (and later for plot labels)
    drugs = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]
    # Create empty list to fill with tumor vol data (for plotting)
    tumor_vol = []
    # Calculate the IQR and quantitatively determine if there are any potential outliers. 
    # Using dictionary to store values
    iqr_dict = {
        "Drug": [],
        "IQR": [],
        "UB": [],
        "LB": [],
        "Outliers": [],
    }
    # Locate the rows which contain mice on each drug
    for drug in drugs:
        # sort by drug
        drug1 = new_mouse_df.loc[new_mouse_df["Drug Regimen"] == drug]
        
        # locate the row where timepoint is the last timepoint
        drug2 = drug1.loc[drug1["Timepoint_x"] == drug1["Timepoint_y"]]
        
        # declare tumor volume value
        tv = drug2["Tumor Volume (mm3)"]
        
        # append tumor volume to tumor_vol list
        tumor_vol.append(tv)
        
        # determine quartiles and IQR
        quartiles = tv.quantile([0.25,0.5,0.75])
        lowerq = quartiles[0.25]
        upperq = quartiles[0.75]
        iqr = upperq-lowerq
        
        # determine upper and lower bound to check for outliers
        lower_bound = lowerq - (1.5*iqr)
        upper_bound = upperq + (1.5*iqr)

        # append dictionary to track IQR and UB/LB for each drug
        iqr_dict["Drug"].append(drug)
        iqr_dict["IQR"].append(iqr)
        iqr_dict["UB"].append(upper_bound)
        iqr_dict["LB"].append(lower_bound)

        # finding outliers, store in IQR dict, print if there are any outliers and for which drug
        outliers = (tv.loc[(drug2["Tumor Volume (mm3)"] >= upper_bound) | (drug2["Tumor Volume (mm3)"] <= lower_bound)]).count()
        iqr_dict["Outliers"].append(outliers)
        if int(outliers) > 0:   
            print(f'There are {outliers} outlier(s) in {drug}')

    # create DataFrame from dictionary
    iqr_df = pd.DataFrame(iqr_dict).set_index("Drug")
    return iqr_df