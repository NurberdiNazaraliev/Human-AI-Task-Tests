import pandas as pd

def task3ai(path):
    df = pd.read_csv(path)

    top_company = df.loc[df["Salary"].idxmax(), "Company Name"]

    top_cities = (
        df[df["Employment Status"].str.contains("Full Time", case=False, na=False)]
        .groupby("Location")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    return top_company, top_cities
