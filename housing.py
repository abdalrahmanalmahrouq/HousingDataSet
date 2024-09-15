#Housing Price Dataset

# https://www.kaggle.com/datasets/sukhmandeepsinghbrar/housing-price-dataset/data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\abdal\Downloads\Housing.csv.zip')

df=pd.DataFrame(data)

df.head()

df.tail()

# df.info()

df.describe().apply(lambda x:round(x,0))

df.dtypes

df[df.duplicated()]

#What is the average price of properties listed in each zip code?

df_avg=df.groupby('zipcode').agg(avg_price=('price','mean')).apply(lambda x: round(x,0))
df_avg

#How does the number of bedrooms affect the average price?

df_bed = df.groupby('bedrooms').agg(avg=('price', 'mean')).reset_index()

plt.figure(figsize=(10, 6))


positions = np.arange(len(df_bed))
bar_width = 0.5

plt.bar(positions, df_bed['avg'], color='skyblue', width=bar_width)

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('Average Price by Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Average Price ($)')

plt.xticks(positions, df_bed['bedrooms'])
plt.show()

# In this figure you can see if you need house with a lot of bedrooms you must pay more money but there is some exceptions
# Like the 4 least bars and this can show you that the number of bedrooms it's not the only factor that affect at the price

#Are properties with a waterfront view significantly more expensive than those without?

avg_price_df=df.groupby('waterfront').agg(avg_front=('price','mean')).apply(lambda x : round(x,2)).reset_index()

plt.bar(avg_price_df['waterfront'],avg_price_df['avg_front'], color = ['red','blue'])
plt.xlabel("Waterfront")
plt.ylabel("Average Price ($)")
plt.title("Average Price by Waterfront View Status")
plt.xticks([0, 1], ['No Waterfront', 'Waterfront'])
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.show()

# Here is a proof  of huge different price between house with waterfront or without

#Examine the relationship between the size of the living area ( sqft_living )and the price.

df_sq = df.groupby('sqft_living').agg(avg_price=('price', 'mean')).reset_index()


plt.figure(figsize=(12, 6))
plt.scatter(df_sq['sqft_living'], df_sq['avg_price'], color='blue')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('Scatter Plot of Average Price vs. Square foot of Living Space')
plt.xlabel('Square foot of living area')
plt.ylabel('Average Price ($)')


plt.show()
 # Here you can see that the most of houses are concentrated at less than 60000 feet and the price = 0 - 1M$

#How does the condition ( condition ) influence the property price?

df_cond = df.groupby('condition').agg(avg_price=('price', 'mean')).reset_index()

plt.figure(figsize=(10, 6))
plt.bar(df_cond['condition'], df_cond['avg_price'], color='green')

plt.title('Average Price by Condition')
plt.xlabel('Condition')
plt.ylabel('Average Price ($)')

plt.show()

# Here you can see that condition 5 is the best


#Are newer properties ( yr_built ) priced differently compared to older ones?


df_year = df.groupby('yr_built').agg(avg_price=('price', 'mean')).apply(lambda x: round(x, 2)).reset_index()


plt.figure(figsize=(10, 6))
plt.plot(df_year['yr_built'], df_year['avg_price'], color='blue')


plt.xlabel('Year Built')
plt.ylabel('Average Price ($)')
plt.title('Average House Price Over the Years')

plt.grid(True)


plt.show()

## Here is the conclusion that the year of built doesn't affect the price

#Is there a noticeable difference in prices between properties with and without a basement ( sqft_basement )?

df['basement']=df['sqft_basement'].apply(lambda x :x>0)
# Here i make this to separate the houses that contains basement and without
# To make the figure meaningful

df_base = df.groupby('basement').agg(avg_price=('price', 'mean')).reset_index()

plt.figure(figsize=(10, 6))
plt.bar(df_base['basement'], df_base['avg_price'], color='orange')
plt.xticks([0, 1], ['without Basement', 'with Basement'])
plt.title('Average Price by Basement')
plt.xlabel('Basement')
plt.ylabel('Average Price ($)')

plt.show()

# Here you can see from the figure the houses that contains basement more expensive than houses without

#Analyze if properties in areas with larger sqft_lot15 have higher average prices.

df_lot15 = df.groupby('sqft_lot15').agg(avg_price=('price', 'mean')).reset_index()

plt.figure(figsize=(10, 6))
plt.scatter(df_lot15['sqft_lot15'], df_lot15['avg_price'], color='purple')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('Scatter Plot of Average Price vs. Lot Size (sqft_lot15)')
plt.xlabel('Lot Size (sqft_lot15)')
plt.ylabel('Average Price ($)')

plt.show()


#Investigate whether properties in certain geographic locations (based on lat and long ) are more expensive.

df_grouped=df.groupby(['lat','long']).agg(avg_price=('price','mean')).sort_values('avg_price',ascending=False).reset_index()
df_grouped

plt.figure(figsize=(12, 8))
plt.scatter(df['long'], df['lat'], c=df['price'], cmap='viridis', alpha=0.6, edgecolors='k')
plt.colorbar(label='Price')
plt.title('Geographic Distribution of Property Prices')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
# Here is the darker colors mean cheaper properties and lighter colors mean more expensive ones

#Determine if properties with more floors ( floors ) tend to have higher or lower prices.

import numpy as np
df_floor = df.groupby('floors').agg(avg_price=('price', 'mean')).reset_index()

plt.figure(figsize=(10, 6))
positions = np.arange(len(df_floor))
bar_width = 0.5
plt.bar(positions, df_floor['avg_price'], color='teal', width=bar_width)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('Average Price by Number of Floors')
plt.xlabel('Number of Floors')
plt.ylabel('Average Price ($)')
plt.xticks(positions, df_floor['floors'])
plt.show()
 # Here you can see the houses with 2.5 floors is the most expensive
