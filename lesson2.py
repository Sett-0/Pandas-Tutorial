import pandas as pd 
import numpy as np

people = {
    'first': ['Anna', 'Mathew', 'Gus'],
    'last': ['Watson', 'Queen', 'Fring'],
    'email': ['AnnaWatson@mail.ru', 'MAthewQueen@gmail.com', 'GusFring@methmail.com']
}

df = pd.DataFrame(people)
# print(df)
# print(df['email'])
# print(type(df['email']))
# print(df.email)
# print(df[['last', 'email']])
# print(df.columns)

# loc and ilocs
# print(df.iloc[0])
# print(df.iloc[[0, 1]])
# print(df.iloc[[0, 1], [1, 2]])
# print(df.iloc[:, [True, True, False]])

# print(df.loc[0])
# print(df.loc[[0, 1]])
# print(df.loc[:, 'email'])
# print(df.loc[:1, ['email', 'last']]) # Order is important (because in that case 
#                                      #  it returns new df object and not series)
# print(type(df.loc[:1, ['email', 'last']]))

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')
pd.set_option('display.max_columns', df.shape[1])

print(df.shape)
# print(df.columns)
with pd.option_context('display.max_colwidth', None):
    print(schema_df.loc[schema_df['qname'] == 'YearsCode', 'question'])
    print(schema_df.loc[schema_df['qname'] == 'YearsCodePro', 'question'])

df['YearsCodePro'] = df['YearsCodePro'].apply(pd.to_numeric, errors='coerce')
df = df[~df['YearsCodePro'].isna()] # FUCK
print(df.loc[df['YearsCodePro'], 'YearsCodePro'])
