import pandas as pd


df = pd.read_csv('jobs_data.csv')
df_copy = df.copy()
df_copy['job_posted_date'] = pd.to_datetime(df_copy['job_posted_date'])

df_salary = df_copy['salary_hour_avg'].median()
df_salary_hour_avg = df_copy['salary_hour_avg'].fillna(df_salary)
df_copy['salary_hour_avg'] = df_copy['salary_hour_avg'].fillna(df_salary)


print("Median Salary:", df_salary)
print("Sorted Salaries:",
      df_copy['salary_hour_avg'].dropna().sort_values().values)

# Final DataFrame
print(df_copy)


# class PandasManagement:
#     def __init__(self, df, df_copy):
#         self.df = pd.read_csv('jobs_data.csv')
#         self.df_copy = df.copy()

#     def copy(self):
#         return self.df_copy


# const res = PandasManagement()
