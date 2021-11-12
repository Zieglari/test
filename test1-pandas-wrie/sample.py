# test
from os import name
import pandas as pd
from pandas.core.frame import DataFrame

# dataframe Name and Age columns
df2 = pd.DataFrame([['ali', 44], ['hassan', 34], ['mohammad', 34], ['parsa', 3]],columns=['name', 'age'])
df = pd.DataFrame([['ali','doctor', 44],['hassan','mohandes', 34],['mohammad','motarjem', 34]],columns=['name','position', 'age'])
# df = pd.DataFrame(['ali','doctor','hassan','mohandes','mohammad','motarjem']])


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer_x3 =pd.ExcelWriter('3.xlsx', engine='xlsxwriter')
writer_x2 = pd.ExcelWriter('2.xlsx', engine = 'xlsxwriter')


# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer_x3, sheet_name='Sheet1', index=False)
df2.to_excel(writer_x2, sheet_name='Sheet1', index=False)


# Close the Pandas Excel writer and output the Excel file.
writer_x3.save()
writer_x2.save()
print('used 2 writer in same time by hassanreza zieglari')
print('file 3.xlsx is \n',df)
print('file 2.xlsx is \n',df2)