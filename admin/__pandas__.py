import ast
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()


def to_list(x):
    if pd.notna(x):
        return ast.literal_eval(x)
    else:
        return x


df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(to_list)
df_DA = df[(df['job_title_short'] == 'Data Analyst')
           & (df['job_country'] == 'United States')]
df_DA_US = df_DA.dropna(subset=['salary_year_avg'])
df_DA_US = df_DA_US.explode('job_skills')
df_DA_US[['salary_year_avg', 'job_skills']]

# index by skills
df_DA_US_GRP = df_DA_US.groupby(
    'job_skills')['salary_year_avg'].agg(['count', 'median'])


# sorted  by to pay
df_DA_top_pay = df_DA_US_GRP.sort_values(by='median', ascending=False).head(10)

# sorted by most demand skills
df_DA_top_skills = df_DA_US_GRP.sort_values(
    by='count', ascending=False).head(10)


print(df_DA_top_pay)
print(df_DA_top_skills)
