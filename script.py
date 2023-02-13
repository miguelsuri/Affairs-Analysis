import csv
import pandas as pd
import numpy as np


#Data cleaning
with open('Affair dataset.csv', 'r') as csv_input:
    csv_reader = csv.reader(csv_input, delimiter=',')

    #heading = next(csv_reader)

    with open("cleanedData.csv", "w") as csv_output:
        writer = csv.writer(csv_output)
        for r in csv_reader:
            writer.writerow((r[1],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10]))

#Q2
with open('cleanedData.csv', 'r') as csv_input:
    csv_reader = csv.reader(csv_input, delimiter=',')
    rows = 0
    columns = 0

    for row in csv_reader:
        rows = rows + 1
        white = next(csv_reader)
    print(rows - 1)


print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q3
df3 = pd.read_csv('cleanedData.csv')
print(df3.dtypes)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q4
df4 = pd.DataFrame(pd.read_csv('cleanedData.csv'))
df4['affair_status'] = np.where(df4['affairs'] > 0 , 'Yes' , 'No')
df4 = df4[['affairs','affair_status','gender','age','yearsmarried','children','religiousness','education','occupation','rating']]
print(df4)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q5
df5 = pd.DataFrame(pd.read_csv('cleanedData.csv'))
print(df5.isna().sum())

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q6
