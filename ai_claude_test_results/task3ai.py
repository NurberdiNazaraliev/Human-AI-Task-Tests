import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)
    max_salary_idx = df['Salary'].idxmax()
    highest_paid_company = df.loc[max_salary_idx, 'Company Name']

    full_time_workers = df[df['Employment Status'] == 'Full Time']
    top_10_cities = full_time_workers['Location'].value_counts().head(10)
    return highest_paid_company, top_10_cities
