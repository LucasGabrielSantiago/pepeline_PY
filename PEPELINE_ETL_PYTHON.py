import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['User_ID'].tolist()
print(user_ids)