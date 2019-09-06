import pandas as pd

# INPUT THE CORRECT FILE PATH TO YOUR EXCEL FILE #
##################################################

df = pd.read_excel('C:/Users/Tyler/Desktop/school/Fall 2019/MAE 3040/Homework/Homework_1/Book1.xlsx')

#################################################


# SELECT THE CORRECT COLUMNS #
##############################

xAxis = df['strain']
yAxis = df['load.1']

##############################

totalRows = df.index[-1]

totalArea = 0
iterator = 0
while iterator < totalRows:
    # calculate trapizoidal area and add to total Area
    base = xAxis[iterator + 1] - xAxis[iterator]
    avgHeight = (yAxis[iterator] + yAxis[iterator + 1]) / 2
    area = base * avgHeight
    totalArea += area
    iterator += 1

print('The approximate area under the curve is: ' + str(totalArea))
