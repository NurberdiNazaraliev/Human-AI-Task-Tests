import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)

    android_devs = df[df["Job Title"].str.contains("Android Developer")]
    average_salary = android_devs["Salary"].mean()

    averageSalaryByCompany = df.groupby("Company Name")["Salary"].mean()
    top5 = averageSalaryByCompany.sort_values(ascending=False).head(5)

    return average_salary, top5
