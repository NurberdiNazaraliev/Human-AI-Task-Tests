import pandas as pd

def task3ai(csv_path):
    # Load dataset
    df = pd.read_csv(csv_path)

    max_salary_index = df["Salary"].idxmax()
    company_highest_salary = df.loc[max_salary_index, "Company Name"]

    top10_fulltime_cities = (
        df[df["Employment Status"].str.strip().str.lower() == "full time"]
        .groupby("Location", as_index=False)
        .size()
        .sort_values("size", ascending=False)
        .head(10)
        .rename(columns={"size": "Full Time Count"})
    )
    top10_fulltime_cities_series = top10_fulltime_cities.set_index('Location')['Full Time Count']

    return company_highest_salary, top10_fulltime_cities_series
