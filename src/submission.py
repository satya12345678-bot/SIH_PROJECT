import pandas as pd

def create_submission(index, predictions, filename="submission.csv"):
    result = pd.DataFrame({
        'Index': index,
        'FPS': predictions
    })
    result.to_csv(filename, index=False)