import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)
    android_devs = df[df['Job Title'] == 'Android Developer']
    avg_salary_android = android_devs['Salary'].mean()

    avg_salary_by_company = df.groupby('Company Name')['Salary'].mean()
    top_5_companies = avg_salary_by_company.sort_values(ascending=False).head(5)
    return avg_salary_android, top_5_companies
