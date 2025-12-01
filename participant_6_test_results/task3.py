import pandas as pd
def task3(file_path):
    df = pd.read_csv(file_path)

    result=df[df["Job Title"]=="Android Developer"]["Salary"].mean()
    top5=df.groupby("Company Name")["Salary"].mean().sort_values(ascending=False).head(5)
  
    return result, top5
