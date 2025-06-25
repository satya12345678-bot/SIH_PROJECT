import pandas as pd
import os
from typing import Tuple

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
