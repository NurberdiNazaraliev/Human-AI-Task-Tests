import pandas as pd

def task3(file_path):
    df = pd.read_csv(file_path)
    android_avg_sal = df[df['Job Title'].str.contains("Android Developer", case=False)]['Salary'].mean()
    result = round(android_avg_sal, 2)

    top_companies_5 = (
        df.groupby('Company Name')['Salary']
          .mean()
          .sort_values(ascending=False)
          .head(5)
    )

    return result, top_companies_5
