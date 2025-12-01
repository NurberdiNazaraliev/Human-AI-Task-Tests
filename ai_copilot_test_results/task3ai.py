import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)
    highest_salary_row = df.loc[df['Salary'].idxmax()]
    highest_salary_comp=highest_salary_row['Company Name']
    full_time = df[df['Employment Status'] == 'Full Time']
    city_counts = full_time['Location'].value_counts().head(10)
    return highest_salary_comp, city_counts
