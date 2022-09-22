import pandas as pd

POPULATION_CSV = '/Users/tom/PycharmProjects/OilPrices/Original_Population_Dataset(2022).csv'

class Population_CSV:

    def import_population(self):
        df = pd.read_csv(POPULATION_CSV)
        population = df['2022_last_updated']
        country = df['country']
        index = 0
        pop_list = []
        for num in range(len(population)):
            pop_list.append([country[num], population[num]])
        return pop_list