import pandas as pd

def task3(path):
    df = pd.read_csv(path)

    android_devs = df[df["Job Title"] == "Android Developer"]
    avg_sal = float(android_devs["Salary"].mean())

    company_means = df.groupby("Company Name")["Salary"].mean()
    top5 = company_means.nlargest(5)

    return avg_sal, top5
