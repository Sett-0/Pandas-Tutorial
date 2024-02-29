# Pandas is a data analysis library that allows us to easily read and work with different types of data
# It is build on top of numpy => great perfomance
import pandas as pd 

df = pd.read_csv('data/survey_results_public.csv')
# print(df)
# print(df.shape)
# print(df.info())
# pd.set_option('display.max_columns', df.shape[1])
# print(df)

schema_df = pd.read_csv('data/survey_results_schema.csv')
# pd.set_option('display.max_rows', df.shape[1])
# print(schema_df)

num_rows = 10
print(schema_df.head(num_rows)) # prints first num_rows rows
print(schema_df.tail(num_rows)) # prints last num_rows rows
# test