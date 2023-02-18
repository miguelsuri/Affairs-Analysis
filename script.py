import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Data cleaning
with open('C:\\Users\\migue\\OneDrive\\Desktop\\Comp Sci Part 2\\Data Analysis\\Personal Projects\\Affairs Analysis\\Affairs-Analysis\\Affair dataset.csv') as csv_input:
    csv_reader = csv.reader(csv_input, delimiter=',')

    #heading = next(csv_reader)

    with open("C:\\Users\\migue\\OneDrive\\Desktop\\Comp Sci Part 2\\Data Analysis\\Personal Projects\\Affairs Analysis\\Affairs-Analysis\\cleanedData.csv", "w") as csv_output:
        writer = csv.writer(csv_output)
        for r in csv_reader:
            writer.writerow((r[1],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10]))

#Q2
with open('C:\\Users\\migue\\OneDrive\\Desktop\\Comp Sci Part 2\\Data Analysis\\Personal Projects\\Affairs Analysis\\Affairs-Analysis\\cleanedData.csv', 'r') as csv_input:
    csv_reader = csv.reader(csv_input, delimiter=',')
    rows = 0
    columns = 0

    for row in csv_reader:
        rows = rows + 1
        white = next(csv_reader)
    print(rows - 1)


print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

df = pd.read_csv('C:\\Users\\migue\\OneDrive\\Desktop\\Comp Sci Part 2\\Data Analysis\\Personal Projects\\Affairs Analysis\\Affairs-Analysis\\cleanedData.csv')

#Q3
df3 = df
print(df3.dtypes)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q4
df4 = pd.DataFrame(df)
df4['affair_status'] = np.where(df4['affairs'] > 0 , 'Yes' , 'No')
df4 = df4[['affairs','affair_status','gender','age','yearsmarried','children','religiousness','education','occupation','rating']]
df4.to_csv('C:\\Users\\migue\\OneDrive\\Desktop\\Comp Sci Part 2\\Data Analysis\\Personal Projects\\Affairs Analysis\\Affairs-Analysis\\cleanedData.csv')
print(df4)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q5
df5 = pd.DataFrame(df)
print(df5.isna().sum())

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q6
df6 = pd.DataFrame(df)
print(df6['gender'].value_counts())

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q7
df7 = pd.DataFrame(df)
print('Most common age: ' + str(df7['age'].value_counts().idxmax()))

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q8
df8 = pd.DataFrame(df)
df8Males = df8[['gender' , 'age']]
df8Males = df8Males[df8Males['gender'] == 'male']

df8Females = df8[['gender' , 'age']]
df8Females = df8Females[df8Females['gender'] == 'female']
print('Most common age for males: ' + str(df8Males['age'].value_counts().idxmax()))
print('Most common age for females: ' + str(df8Females['age'].value_counts().idxmax()))

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q9
#affairs: 0 = none, 1 = once, 2 = twice, 3 = 3 times, 7 = 4–10 times, 12 = monthly, 12 = weekly, 12 = daily.
df9 = pd.DataFrame(df)
df9MaleAffairs = df9[['gender' , 'affairs']]
df9MaleAffairs = df9MaleAffairs[df9MaleAffairs['gender'] == 'male']

df9FemaleAffairs = df9[['gender' , 'affairs']]
df9FemaleAffairs = df9FemaleAffairs[df9FemaleAffairs['gender'] == 'female']
#print(df9MaleAffairs.drop(df9MaleAffairs[df9MaleAffairs['affairs'] == 12].index).value_counts())
print("Percentage of times males cheated: " + str(df9MaleAffairs.drop(df9MaleAffairs[df9MaleAffairs['affairs'] == 0].index).value_counts().sum() / df9MaleAffairs.value_counts().sum() * 100) + "%")
print("Percentage of times females cheated: " + str(df9FemaleAffairs.drop(df9FemaleAffairs[df9FemaleAffairs['affairs'] == 0].index).value_counts().sum() / df9FemaleAffairs.value_counts().sum() * 100) + "%")

print("Percentage of times of continuous cheating by men: " + str(df9MaleAffairs.drop(df9MaleAffairs[df9MaleAffairs['affairs'] == 0].index).loc[df9MaleAffairs['affairs'] == 12].value_counts().sum() / df9MaleAffairs.value_counts().sum() * 100) + "%")
print("Percentage of times of continuous cheating by womem: " + str(df9FemaleAffairs.drop(df9FemaleAffairs[df9FemaleAffairs['affairs'] == 0].index).loc[df9FemaleAffairs['affairs'] == 12].value_counts().sum() / df9FemaleAffairs.value_counts().sum() * 100) + "%")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q10
df10 = pd.DataFrame(df)
df10 = df10.loc[df10['affair_status'] == 'Yes' , ['gender' , 'age']]
df10 = df10[df10['gender'] == 'female']
print(df10.value_counts())

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q11
df11 = pd.DataFrame(df)
df11Under5 = pd.DataFrame(df)
df11Under5 = df11Under5.loc[df11Under5['affair_status'] == 'Yes' , ['yearsmarried']]
df11Under5 = df11Under5.loc[df11Under5['yearsmarried'] < 5]
q11Result1 = (len(df11Under5) / len(df11) * 100)
print("Percentage of chaeting that occurs in marriages under 5 years: " + str(q11Result1) + "%")

df11Over5 =pd.DataFrame(df)
df11Over5 = df11Over5.loc[df11Over5['affair_status'] == 'Yes' , ['yearsmarried']]
df11Over5 = df11Over5.loc[df11Over5['yearsmarried'] >= 5]
q11Result2 = (len(df11Over5) / len(df11) * 100)
print("Percentage of chaeting that occurs in marriages over, including, 5 years: " + str(q11Result2) + "%")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#Q12
df12 = pd.DataFrame(df)
