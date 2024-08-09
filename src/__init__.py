import pandas as pd
# import matplotlib.pyplot as plt

df = pd.read_csv('../root/pandas/data_jobs.csv')
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

df_modify = df.copy()

top_countries = df_modify['job_country'].value_counts().head(6).index

job_titles = ['Data Analyst', 'Data Engineer',
              'Data Scientist', 'Cloud Engineer']
df_job_country_salary = df_modify.pivot_table(
    values='salary_year_avg',
    index='job_country',
    columns='job_title_short ',
    aggfunc='median'
)

df_job_country_salary = df_job_country_salary.loc[top_countries]
df_job_country_salary = df_job_country_salary[job_titles]

print(df_job_country_salary)
