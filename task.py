import pandas as pd
import matplotlib.pyplot as mt

try:
    
    df = pd.read_csv('tarefas/vehicles_data.csv')
    
    print(df.head())
    print(df.dtypes)
    print(df.isnull().sum())
    print(df.describe())
    performGroupMe = df.groupby('Type')['Price($)'].mean()
    performGroup = df.groupby('Type')['Name'].count()
    performGreet170 = df[df['Price($)'] > 170]
    print(performGroupMe)
    print(performGroup)
    print(performGreet170)
    
    
    mt.plot(df['Model'],df['Price($)'])
    df['Price($)'].plot(kind='line', color='red',linewidth=2)
    mt.xlabel('Vehicles\'model')
    mt.ylabel('Price($)')
    mt.title('Vehicles\'model and price')
    mt.show()
    
    
    df.groupby('Type')['Price($)'].mean().plot(kind='bar')
    mt.xlabel('Type')
    mt.xlabel('Average Price($)')
    mt.title('Average Price($) by Type')
    mt.show()
    
    df['Price($)'].plot(kind='hist',bins=5)
    mt.xlabel('Price')
    mt.title('Price Distibution')
    mt.show()
except FileNotFoundError:
    print("File not found. Please check the filename")
