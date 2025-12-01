import pandas as pd

def task3ai(csv_path):
    df = pd.read_csv(csv_path)

    highest_salary_com = df.loc[df['Salary'].idxmax()]
    company_name = highest_salary_com['Company Name']

    full_time = df[df['Employment Status'].str.contains('Full Time', case=False, na=False)]
    top_cities = full_time['Location'].value_counts().head(10)

    return company_name, top_cities
