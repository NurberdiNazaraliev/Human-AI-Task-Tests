import pandas as pd
def task3(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    android_devs = df[df['Job Title'] == 'Android Developer']
    avg_salary = android_devs['Salary'].mean()
  
    company_avg_salary = df.groupby('Company Name')['Salary'].mean().sort_values(ascending=False)
    top_com=company_avg_salary.head(5)
    return avg_salary, top_com