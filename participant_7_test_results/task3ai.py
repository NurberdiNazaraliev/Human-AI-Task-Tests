import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)
    top_sal=df[df['Salary'] == df['Salary'].max()]
    top_com=top_sal['Company Name']
    full_time = df[df['Employment Status'].str.contains('Full Time', case=False, na=False)]
    top_cities = full_time['Location'].value_counts().head(10)
    
    return top_com, top_cities
