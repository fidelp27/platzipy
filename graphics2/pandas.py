import read_csv
import charts
import utils
import pandas as pd


def run():       
    
    # data = list(filter(lambda item: item["Continent"] == "South America", data))
    
    # countries = list(map(lambda x: x["Country"], data))
    # percentages = list(map(lambda x: x["World Population Percentage"], data))
    # charts.generate_pie_chart(countries, percentages)   
    
    df = pd.read_csv("./graphics2/info.csv")
    df = df[df['Continent'] == "Africa"]
    countries = df["Country"].values
    percentages = df["World Population Percentage"].values
    charts.generate_pie_chart(countries, percentages)   
    
    data = read_csv.read_csv("./graphics2/info.csv")
    country = input("Type a country => ")
    result = utils.population_by_country(data, country)
    
    if len(result)>0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)
    
if __name__ == "__main__":
     run()
    