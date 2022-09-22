import pandas as pd

OILFILE = '/Users/tom/PycharmProjects/OilPrices/Original_Oil_Dataset.csv'


class CSV_Pandas:
    def __init__(self):
        self.df = pd.read_csv(OILFILE, sep=",")

    # Return the list of countries for main.py
    def import_country_list(self):
        country_list = self.df['Country']
        return country_list

    def update_data_new_csv(self, new_oil_production_data, new_population_data):
        # Originally iterated through data and added each row to DataFrame individually
        # before finding the more efficient way
        self.df["Yearly Oil Production (barrels per day)"] = new_oil_production_data
        self.df["Population"] = new_population_data
        self.df.to_csv("New_Petrol_Dataset(20.06.2022).csv")
        # Created a new CSV with appropriate title and added data