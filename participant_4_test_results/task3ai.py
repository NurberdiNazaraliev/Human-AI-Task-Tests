import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)

    max_salary_idx = df["Salary"].idxmax()
    top_company = df.at[max_salary_idx, "Company Name"]

    full_time_df = df[df["Employment Status"].str.contains("full time", case=False, na=False)]
    top_locations = full_time_df["Location"].value_counts().nlargest(10)

    return top_company, top_locations
