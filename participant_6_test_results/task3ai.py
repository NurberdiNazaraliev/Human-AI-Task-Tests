import pandas as pd

def task3ai(file_path):
    df = pd.read_csv(file_path)
    com_name= df.loc[df["Salary"].idxmax(), "Company Name"]

    top_10_cities = (
        df[df["Employment Status"] == "Full Time"]      
        .groupby("Location")["Employment Status"]          
        .count()                                      
        .sort_values(ascending=False)                
        .head(10)                                     
    )

    return com_name, top_10_cities
