import pandas as pd

data = {
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": [
        "Single", "Married", "Single", "Married", "Divorced",
        "Married", "Divorced", "Single", "Married", "Single"
    ],
    "Taxable Income": [
        "125K", "100K", "70K", "120K", "95K",
        "60K", "220K", "85K", "75K", "90K"
    ],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print("Q1:")
print(df)

print("\nQ2:")
print(df.iloc[[0, 4, 7, 8]])

print("\nQ3.1:")
print(df.iloc[3:8])

print("\nQ3.2:")
print(df.iloc[4:9, 2:5])

print("\nQ3.3:")
print(df.iloc[:, 1:4])

print("\nQ4:")
try:
    iris_df = pd.read_csv("Iris.csv")
    print(iris_df.head())
except FileNotFoundError:
    print("Iris.csv not found. Put Iris.csv in the same folder as this program.")

print("\nQ5:")
try:
    iris_df = pd.read_csv("Iris.csv")
    iris_modified = iris_df.drop(index=4)
    iris_modified = iris_modified.drop(iris_modified.columns[3], axis=1)
    print(iris_modified)
except FileNotFoundError:
    print("Iris.csv not found.")

employee_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": [
        "2020-03-15", "2017-07-19", "2013-06-01",
        "2021-02-10", "2010-11-25"
    ],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

employees = pd.DataFrame(employee_data)

employees.to_csv("employees.csv", index=False)

print("\nQ6:")
print(employees)

print("\nQ6(a) Shape:")
print(employees.shape)

print("\nQ6(b) Information:")
employees.info()

print("\nQ6(c) Descriptive Statistics:")
print(employees.describe())

print("\nQ6(d) First 5 rows:")
print(employees.head())

print("\nQ6(d) Last 3 rows:")
print(employees.tail(3))

print("\nQ6(e)(i) Average Salary:")
print(employees["Salary"].mean())

print("\nQ6(e)(ii) Total Bonus:")
print(employees["Bonus"].sum())

print("\nQ6(e)(iii) Youngest Employee Age:")
print(employees["Age"].min())

print("\nQ6(e)(iv) Highest Performance Rating:")
print(employees["Rating"].max())

print("\nQ6(f) Sorted by Salary:")
print(employees.sort_values(by="Salary", ascending=False))

def performance_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

employees["Performance"] = employees["Rating"].apply(performance_category)

print("\nQ6(g) Performance Category:")
print(employees[["Name", "Rating", "Performance"]])

print("\nQ6(h) Missing Values:")
print(employees.isnull().sum())

employees.rename(columns={"Employee_ID": "ID"}, inplace=True)

print("\nQ6(i) Renamed DataFrame:")
print(employees)

print("\nQ6(j)(i) More than 5 Years Experience:")
print(employees[employees["Years_of_Experience"] > 5])

print("\nQ6(j)(ii) IT Employees:")
print(employees[employees["Department"] == "IT"])

employees["Tax"] = employees["Salary"] * 0.10

print("\nQ6(k) Tax:")
print(employees[["Name", "Salary", "Tax"]])

employees.to_csv("modified_employees.csv", index=False)

print("\nQ6(l): modified_employees.csv saved successfully.")