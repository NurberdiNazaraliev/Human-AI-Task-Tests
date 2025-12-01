import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)
    top_sal=df[df['Salary'] == df['Salary'].max()]
    top_com=top_sal['Company Name']
    top_cities = (
    df[df["Employment Status"] == "Full Time"]
      .groupby("Location")
      .size()
      .sort_values(ascending=False)
      .head(10)
    )



    
    return top_com, top_cities
