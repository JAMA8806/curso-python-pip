import utils
import read_csv
import charts

def run ():
    data = read_csv.read_csv('./data.csv')
    task = input("Choose a task: /n 1.Population by country /n 2. World Population Percentage /n")
    if task == '1':
        country = input("Enter country name: ")
        result = utils.population_by_country(data, country)
        print(result) 
        keys, values = utils.get_population(result[0])# Pass the country data to get_population
        chart_type = input("Enter chart type (bar/pie): /n 1. bar /n 2. pie /n")
        if chart_type == '1':
            charts.generate_bar_chart(keys, values, country)
        elif chart_type == '2':
            charts.generate_pie_chart(keys, values, country)  
        else:
            print("Invalid chart type. Please choose 1 for'bar' or 2 for'pie'.")
    elif task == '2':
        Continent = input("Enter continent name: ")
        data = list(filter(lambda item: item['Continent'] == Continent, data)) # Filter data for South America
        
        labels, values = utils.world_population_percentage(data)
        charts.generate_pie_chart(labels, values, Continent)
        



 # if controls that this code runs only when the script is executed directly, not when imported as a module
if __name__ == '__main__':
    run()