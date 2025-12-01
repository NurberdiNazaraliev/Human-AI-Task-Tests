import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)
    ad=df[df['Job Title']=='Android Developer']
    result=ad['Salary'].mean()

    df_comp=df.groupby('Company Name')["Salary"].mean()
    df_comp = df_comp.sort_values(ascending=False)
    top_companies_5=df_comp.head(5)
    
    return result, top_companies_5
