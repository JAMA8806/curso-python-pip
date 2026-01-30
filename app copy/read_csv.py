import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')# Read the CSV file with comma as delimiter
        header= next(reader)
        list_data = []
            
        for row in reader: 
            country = dict(zip(header, row)) # Create a dictionary by zipping the header and the row
            list_data.append(country)
            
        return list_data
           

if __name__ == '__main__':
    data = read_csv('../app copy/data.csv')
    print(data[3])