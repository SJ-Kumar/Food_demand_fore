import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('seaborn')

df_meal = pd.read_csv(r'C:\10-Practice\DemoProject\fooddemandfore\meal_info.csv') 

df_center = pd.read_csv(r'C:\10-Practice\DemoProject\fooddemandfore\fulfilment_center_info.csv') 

df_food = pd.read_csv(r'C:\10-Practice\DemoProject\fooddemandfore\train_food.csv') 

df = pd.merge(df_food,df_center,on='center_id') 
df = pd.merge(df,df_meal,on='meal_id')

print(df)
table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)
print(table)

#dictionary for meals per food item
item_count = {}

for i in range(table.index.nunique()):
    item_count[table.index[i]] = table.num_orders[i]/df_meal[df_meal['category']==table.index[i]].shape[0]

#bar plot 
plt.bar([x for x in item_count.keys()],[x for x in item_count.values()],color='orange')

#adjust xticks
plt.xticks(rotation=70)

#label x-axis
plt.xlabel('Food item')

#label y-axis
plt.ylabel('No. of meals')

#label the plot
plt.title('Meals per food item')

#save plot
plt.savefig(r'C:\10-Practice\DemoProject\fooddemandfore\matplotlib_plotting_7.png',dpi=300,bbox_inches='tight')

#display plot
plt.show();

#dictionary for cuisine and its total orders
d_cuisine = {}

#total number of order
total = df['num_orders'].sum()

#find ratio of orders per cuisine
for i in range(df['cuisine'].nunique()):

#cuisine
    c = df['cuisine'].unique()[i]

#num of orders for the cuisine
c_order = df[df['cuisine']==c]['num_orders'].sum()
d_cuisine[c] = c_order/total

#pie plot 
plt.pie([x*100 for x in d_cuisine.values()],labels=[x for x in d_cuisine.keys()], autopct='%0.1f', explode=None ,) 

#plt.pie([x*100 for x in d_cuisine.values()],labels=[x for x in d_cuisine.keys()],autopct='%0.1f',explode=[0,0,0.1,0]) 

#label the plot 
plt.title('Cuisine share %') 
plt.savefig(r'C:\10-Practice\DemoProject\fooddemandfore\matplotlib_plotting_8.png',dpi=300,bbox_inches='tight') 
plt.show();


#Box plot

#dictionary for base price per cuisine
c_price = {}
for i in df['cuisine'].unique():
    c_price[i] = df[df['cuisine']==i].base_price

#plotting boxplot 
plt.boxplot([x for x in c_price.values()],labels=[x for x in c_price.keys()]) 

#x and y-axis labels 
plt.xlabel('Cuisine') 
plt.ylabel('Price') 

#plot title 
plt.title('Analysing cuisine price') 

#save and display 
plt.savefig(r'C:\10-Practice\DemoProject\fooddemandfore\matplotlib_plotting_9.png',dpi=300,bbox_inches='tight') 
plt.show();

#Histogram
#plotting histogram 
plt.hist(df['base_price'],rwidth=0.9,alpha=0.3,color='blue',bins=15,edgecolor='red') 

#x and y-axis labels 
plt.xlabel('Base price range') 
plt.ylabel('Distinct order') 

#plot title 
plt.title('Inspecting price effect') 

#save and display the plot 
plt.savefig(r'C:\10-Practice\DemoProject\fooddemandfore\matplotlib_plotting_10.png',dpi=300,bbox_inches='tight') 
plt.show();

#LinePlot

#new revenue column 
df['revenue'] = df.apply(lambda x: x.checkout_price*x.num_orders,axis=1) 

#new month column 
df['month'] = df['week'].apply(lambda x: x//4) 

#list to store month-wise revenue 
month=[] 
month_order=[] 

for i in range(max(df['month'])):
    month.append(i) 
    month_order.append(df[df['month']==i].revenue.sum()) 
    
#list to store week-wise revenue 
week=[] 
week_order=[] 

for i in range(max(df['week'])): 
    week.append(i) 
    week_order.append(df[df['week']==i].revenue.sum())

#subplots returns a Figure and an Axes object 
fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(20,5)) 

#manipulating the first Axes 
ax[0].plot(week,week_order) 
ax[0].set_xlabel('Week') 
ax[0].set_ylabel('Revenue') 
ax[0].set_title('Weekly income') 

#manipulating the second Axes 
ax[1].plot(month,month_order) 
ax[1].set_xlabel('Month') 
ax[1].set_ylabel('Revenue') 
ax[1].set_title('Monthly income') 

#save and display the plot 
plt.savefig(r'C:\10-Practice\DemoProject\fooddemandfore\matplotlib_plotting_11.png',dpi=300,bbox_inches='tight') 
plt.show();