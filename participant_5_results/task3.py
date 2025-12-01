import pandas as pd
def task3(file_path):
    data_frame = pd.read_csv(file_path)
    
    android_mask = data_frame['Job Title'] == 'Android Developer'
    android_developers = data_frame[android_mask]
    android_salary_avg = android_developers['Salary'].mean()
    
    company_salaries = data_frame.groupby('Company Name')['Salary'].mean()
    sorted_companies = company_salaries.sort_values(ascending=False)
    top_five_companies = sorted_companies.iloc[:5]
    
    return android_salary_avg, top_five_companies