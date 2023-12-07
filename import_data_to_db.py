import pandas as pd
from sqlalchemy import create_engine


# df = pd.read_csv('/Users/meetapandit/DE_Bootcamp/SQL_optimization_exercise/dataset/book.csv')
#print(df.head())

# convert year to int
# df['year'] = df['year'].fillna(0).astype('int')

# print(df.dtypes)

# engine = create_engine('postgresql://postgres:password@localhost:5433/postgres')

# df.to_sql("article",
#           engine,
#           if_exists="append",  index = False)

# Load table book into db
# df = pd.read_csv('/Users/meetapandit/DE_Bootcamp/SQL_optimization_exercise/dataset/book.csv')
# df = df.fillna(0)
# print(df.head())

# engine = create_engine('postgresql://postgres:password@localhost:5433/postgres')

# df.to_sql("book",
#           engine,
#           if_exists="append",  index = False)


# # Load table inproceedings into db
# df = pd.read_csv('/Users/meetapandit/DE_Bootcamp/SQL_optimization_exercise/dataset/inproceedings.csv')
# df = df.fillna(0)
# df['year'] = df['year'].astype('int')
# print(df.head())

# engine = create_engine('postgresql://postgres:password@localhost:5433/postgres')

# df.to_sql("inproceedings",
#           engine,
#           if_exists="append",  index = False)

# # Load table proceedings into db
df = pd.read_csv('/Users/meetapandit/DE_Bootcamp/SQL_optimization_exercise/dataset/proceedings.csv')
df = df.fillna(0)
df['year'] = df['year'].astype('int')
print(df.head())

engine = create_engine('postgresql://postgres:password@localhost:5433/postgres')

df.to_sql("proceedings",
          engine,
          if_exists="append",  index = False)

# Load table publications into db
df = pd.read_csv('/Users/meetapandit/DE_Bootcamp/SQL_optimization_exercise/dataset/publications.csv')
df = df.fillna(0)
df['year'] = df['year'].astype('int')
print(df.head())

# engine = create_engine('postgresql://postgres:password@hostname:port/postgres')

# Update the table name in the below segment to upload data for other tables lile proceedings and inproceedings
# df.to_sql("publications",
#           engine,
#           if_exists="append",  index = False)