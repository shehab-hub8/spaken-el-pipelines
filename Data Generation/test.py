import pandas as pd

pd.set_option('display.max_rows', None)      # show all rows
pd.set_option('display.max_colwidth', None)  # show full text in each cell

df = pd.read_csv('department_treatment.csv')

print(df['diagnosis'])
