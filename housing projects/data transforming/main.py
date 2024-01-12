import pandas as pd

df = pd.read_csv('housedata.csv', sep=';')

print(df)
mask = df.eval('price.isnull() | discription.isnull() | location.isnull() '
               '|  Bedrooms.isnull() | Bathrooms.isnull() | Parking_spaces.isnull() '
               '| floor_size.isnull()')

filterd_df = df[~mask]

print(filterd_df)

filterd_df.to_csv('transformed housedata.csv', index =False )
