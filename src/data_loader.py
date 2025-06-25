import pandas as pd
import os
from typing import Tuple
import random
from geonamescache import GeonamesCache

def load_data(train_path: str, test_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load CSV files into pandas DataFrames for training and testing datasets.
    """
    if not os.path.exists(train_path):
        raise FileNotFoundError(f"{train_path} not found.")
    if not os.path.exists(test_path):
        raise FileNotFoundError(f"{test_path} not found.")
        
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    return train_df, test_df

def load_kalimati_dataset(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    # Map unique crops to place names for anonymization
    gc = GeonamesCache()
    places = list(gc.get_us_states().keys())
    random.seed(42)
    random.shuffle(places)
    unique_crops = df['Commodity'].unique()
    if len(unique_crops) > len(places):
        multiplier = (len(unique_crops) // len(places)) + 1
        places *= multiplier
        random.shuffle(places)
    crop_to_place_mapping = {crop: places[i] for i, crop in enumerate(unique_crops)}
    df['Commodity'] = df['Commodity'].map(crop_to_place_mapping)
    return df
