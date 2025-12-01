import pandas as pd
def task3ai(file_path):
    df = pd.read_csv(file_path)

    highest = df.sort_values("Salary", ascending=False).iloc[0]
    top_company = highest["Company Name"]

    ft = df[df["Employment Status"].str.contains("full time", case=False, na=False)]
    top_locations = ft["Location"].value_counts().head(10)

    return top_company, top_locations