import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)
    
    android_avg = df.query("`Job Title` == 'Android Developer'")['Salary'].mean()
    
    company_avg = df.groupby('Company Name').agg({'Salary': 'mean'})
    top_5 = company_avg.nlargest(5, 'Salary')
    
    return android_avg, top_5