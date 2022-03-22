from sklearn.datasets import make_regression
import pandas as pd
import os
import numpy as np

# If there's no dataset in the project directory, create a reasonably large one. 
# If it exists, append some new observations. 
if os.path.isfile("data/artists.csv"):
    artists = pd.read_csv('data/artists.csv')
    print("Artists dataset preview")
    print(artists.head())
    
if os.path.isfile("data/tracks.csv"):
    tracks = pd.read_csv('data/tracks.csv')
    print("Tracks dataset preview")
    print(tracks.head())