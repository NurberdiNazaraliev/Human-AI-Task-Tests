import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)

    android_devs = df[df["Job Title"]==("Android Developer")]
    average_salary = android_devs["Salary"].mean()
    
    top_average_salaries = df.groupby('Company Name')['Salary'].mean()
    top_5_companies = top_average_salaries.nlargest(5).index.tolist()

    # 3. Return both results
    return average_salary, top_5_companies
