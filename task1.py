
import pandas as pd
import numpy as np

print("TITANIC DATASET")

titanic = pd.read_csv("titanic.csv")
print(titanic.head())
print(titanic.tail())
titanic.info()
print(titanic.describe())
print(titanic.dtypes)
print(titanic['Sex'].unique())
print(titanic['Embarked'].unique())
print(titanic['Survived'].value_counts())

target_titanic = 'Survived'
features_titanic = titanic.drop(columns=[target_titanic])

print(titanic.shape)
print(titanic.isnull().sum())

print("STUDENTS PERFORMANCE DATASET")

students = pd.read_csv("StudentsPerformance.csv")
print(students.head())
print(students.tail())
students.info()
print(students.describe())
print(students.dtypes)
print(students['gender'].unique())
print(students['lunch'].value_counts())

target_students = 'math score'
features_students = students.drop(columns=[target_students])

print(students.shape)
print(students.isnull().sum())

print("TASK COMPLETED")
