import plotly.express as px
import csv
import numpy as np
def getdatasource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as i:
        csv_reader = csv.DictReader(i)
        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{'x':coffee, 'y':sleep}
def findcorelation(datasource):
    corelation = np.corrcoef(datasource['x'], datasource['y'])
    print('The corelation between coffee and hours of sleep is', corelation[0,1])
def setup():
    data_path = 'cups of coffee vs hours of sleep.csv'
    datasource = getdatasource (data_path)
    findcorelation(datasource)
setup()