import pandas as pd


class Extract:
    def __init__(self):
        pass

    def extract_data(self, file_path: str):
        """
        Will simply extract the csv data into a dataframe
        """
        return pd.read_csv(file_path)
