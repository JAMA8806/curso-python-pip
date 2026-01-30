def get_population(country):
    population = {
        '2020': int(country['2020 Population']),
        '2015': int(country['2015 Population']),
        '2010': int(country['2010 Population']),
        '2000': int(country['2000 Population']),
    }
    labels = population.keys()
    values = population.values()
    return labels, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def world_population_percentage(data):
    labels = []
    values = []
    for each_country in data:
        labels.append(each_country['Country/Territory'])
        values.append(float(each_country['World Population Percentage'].strip('%')))
    return labels, values

a = "Hola mundo. "