import pandas as pd
from etl.extractor import Extractor


class DataProcessor:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.extract_data()
        self.df = pd.DataFrame()

    def extract_data(self):
        return Extractor.Extractor.fromCSV(self.file_name)

    def load_data(self, csv_file_name):
        self.df.to_csv(csv_file_name)
