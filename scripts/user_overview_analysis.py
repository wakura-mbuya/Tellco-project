import sys
import pandas as pd
import numpy as np

sys.path.append('../scripts')
from load_data import LoadData

#Load the telecommunication dataset
loader = LoadData()
telco_df = loader.read_excel('../data/Week1_challenge_data_source.xlsx')

def clean_data(df):
    """
    Cleans the dataframe passed by imputing missing values and ensuring all data types are of the correct type
    """
    
    df = df.dropna(subset=['IMSI', 'MSISDN/Number', 'IMEI', 'Handset Manufacturer', 'Handset Type', 'Last Location Name'])
    df = impute_missing_values(df)
    return df
    
    
def impute_missing_values(df):
    """
    This function imputes missing values by filling them with the mean
    """
    for i in df.columns:
        df[i].fillna(df[i].mode()[0], inplace=True)
    return df


def get_top_handsets(df):
    """
    This function identifies the top handsets used by customers
    Args:
    -----
    df: pd.DataFrame - The dataframe containing the clean dataset
    
    Return
    ------
    DataFrame
    """
    
    return df['Handset Type'].value_counts()

if __name__ == "__main__":
    loader = LoadData()
    telco_df = loader.read_excel('../data/Week1_challenge_data_source.xlsx')
    clean_telco_df = clean_data(telco_df)
    print(get_top_handsets(clean_telco_df.head()))


    
    