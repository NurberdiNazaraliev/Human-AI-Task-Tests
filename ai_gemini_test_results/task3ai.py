import pandas as pd

def task3ai(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please verify the file path.")

    df['Job Title'] = df['Job Title'].astype(str).str.strip()
    df['Employment Status'] = df['Employment Status'].astype(str).str.strip()
    
    max_salary_row = df.loc[df['Salary'].idxmax()]
    highest_salary_company = max_salary_row['Company Name']
    


    full_time_workers = df[df['Employment Status'] == 'Full Time']
    top_10_cities = (
        full_time_workers['Location']
        .value_counts()
        .head(10)
        .reset_index()
    )
    top_10_cities.columns = ['Location', 'Full Time Workers Count']

    return highest_salary_company, top_10_cities
