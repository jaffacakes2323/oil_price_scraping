from bs4 import BeautifulSoup
import requests
from update_dataframe import CSV_Pandas
from population_data import Population_CSV
import csv


oil_production_link = "https://www.worldometers.info/oil/oil-production-by-country/"


# needed to import file with CSV libray, as there was an encoding error: 'utf-8' codec can't decode byte 0xa3 in
# position 301: invalid start byte pandas
"""with open(OILFILE, encoding="utf8", errors='ignore') as file: 
    data = csv.reader(file)

    with open('Original_Oil_Dataset.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for line in data:
            writer.writerow(line)
"""

# USING BEAUTIFUL SOUP TO PARSE HTML AND SCRAPE THE DATA WE WANT
response = requests.get(oil_production_link)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

website_countries = []  # Need to pull country and oil production info, and pop them in these lists
website_data = []
counter = 1
table = soup.find_all(name="td")  # Looking for all the table data elements

for table_line in table:
    if counter == 2:
        website_countries.append(table_line.text)
    elif counter == 3:
        website_data.append(table_line.text)

    if counter == 3:
        counter = 1
    else:
        counter += 1

# COMBINING THE PULLED COUNTRY AND DATA LIST INTO ONE ORGANISED LIST
countries_data_list = []
index = 0
for country in website_countries:
    try:
        countries_data_list.append([country, website_data[index]])
        index += 1
    except:
        break

# SEARCHING AND ORGANISING OIL PRODUCTION DATA FOR COUNTRIES IN OUR OIL.CSV (IMPORTING CLASS)
file = CSV_Pandas()
file2 = Population_CSV()
population_list = file2.import_population()
csv_country_list = file.import_country_list()  # Import the data from our csv file, so we know which countries we need information for
country_oil_production = []
country_population = []
for search in csv_country_list:  # Came across some basic indexing errors that needed troubleshooting with print statments
    index = 0
    while index < len(countries_data_list):
        if search == countries_data_list[index][0]:
            country_oil_production.append(countries_data_list[index][1] )  # Added '+ search' to the append to make sure data matched the searched country
            index = (len(countries_data_list))
        if index == (len(countries_data_list) - 1):
            country_oil_production.append("-")  # + search
            index += 1
        else:
            index += 1
# Arranging population data for new column
for search in csv_country_list:
    index = 0
    while index < len(population_list):
        if search == population_list[index][0]: # If searched country in original CSV is equal to the indexed country in population CSV, then append
            country_population.append(population_list[index][1])
            index = (len(population_list))
        if index == (len(population_list) - 1):
            country_population.append("-") # If iterated through whole list and not found a match, end iteration so next one in csv_country_list will start
            index += 1
        else:
            index += 1

file.update_data_new_csv(country_oil_production, country_population)


