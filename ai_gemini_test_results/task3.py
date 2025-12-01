import pandas as pd

def task3(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please verify the file path.")

    df['Job Title'] = df['Job Title'].astype(str).str.strip()
    df['Employment Status'] = df['Employment Status'].astype(str).str.strip()

    android_dev_salary = df[df['Job Title'] == 'Android Developer']['Salary'].mean()

    top_5_companies = (
        df.groupby('Company Name')['Salary']
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )
    top_5_companies.columns = ['Company Name', 'Average Salary (INR)']

    return android_dev_salary, top_5_companies

