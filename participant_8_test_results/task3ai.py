import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)

    max_salary_row = df[df["Salary"] == df["Salary"].max()]
    company = max_salary_row["Company Name"].iloc[0]

    full_time = df[df["Employment Status"].str.contains("full time", case=False, na=False)]
    city_counts = full_time["Location"].value_counts().head(10)

    return company, city_counts
