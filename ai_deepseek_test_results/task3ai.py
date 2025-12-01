import pandas as pd

def task3ai(csv_path):
   
    df = pd.read_csv(csv_path)

    highest_salary_employee = df.loc[df['Salary'].idxmax()]
    company=highest_salary_employee['Company Name']


   
    full_time_workers = df[df['Employment Status'] == 'Full Time']
    city_full_time = full_time_workers['Location'].value_counts().head(10)
    
    return company, city_full_time
