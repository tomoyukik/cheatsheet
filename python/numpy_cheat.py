# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
covid_df = pd.read_csv('./confirmed_pivot.csv', parse_dates=['date'])
covid_df = covid_df[covid_df['country'] == 'Japan']
covid_df.describe()

# %%
covid_df.dtypes

# %% 
# pandas.rolling
# onで指定したカラムはrollingでの計算対象外になり、結果のdataframeに含まれる
# 照準にソートされている必要があり、onで指定したカラムの順序にしたがって計算されるわけではない
sns.lineplot(
    data=covid_df.sort_values('date').rolling(60, on='date').mean(),
    x='date', y='total'
)
plt.show()