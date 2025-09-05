import pandas as pd

def load_exoplanet_data():
    url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+ps&format=csv'
    df = pd.read_csv(url, low_memory=False)  
    return df