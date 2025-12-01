import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)
    android_dev = df[df['Job Title'] == 'Android Developer']
    avg_salary = android_dev['Salary'].mean()
    company_avg_salary = df.groupby('Company Name')['Salary'].mean()
    top5_companies = company_avg_salary.sort_values(ascending=False).head(5)

    return avg_salary, top5_companies
