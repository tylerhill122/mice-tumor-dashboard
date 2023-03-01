import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import random

mouse_data_path = "static/data/mouse_data.json"

df = pd.read_json(mouse_data_path)