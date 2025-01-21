import pandas as pd


class Transform:
    def __init__(self, data:pd.DataFrame):
        self.data = data

    def standardize(self):
        for col in self.data.select_dtypes(include=["object"]):
            self.data[col] = self.data[col].str.capitalize()

        return self
        
    def cleaning(self):
        pass
        
    def categories(self):
        return self.data["Category"].drop_duplicates()