import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)
    android_avg = df.query("`Job Title` == 'Android Developer'")["Salary"].mean()

    top5 = (
        df.groupby("Company Name")["Salary"]
        .agg("mean")
        .sort_values(ascending=False)
        .head(5)
    )
    return android_avg, top5
