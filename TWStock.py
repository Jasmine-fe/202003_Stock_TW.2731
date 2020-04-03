#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import datetime as datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


# 觀光業
stock_Tiger = '2731.TW' #雄獅旅行社
stock_Bird = '5706.TW' #鳳凰旅行社

start = datetime.datetime(2020,3,2)
end   = datetime.datetime(2020,3,31)
DataFrame_Tiger = pdr.DataReader(stock_Tiger, 'yahoo', start, end)
DataFrame_Bird = pdr.DataReader(stock_Bird, 'yahoo', start, end)

# open price 開盤價
DataFrame_Tiger['Open'].plot(label='Tiger',figsize=(16,8),title='open price')
DataFrame_Bird['Open'].plot(label='Bird')
plt.legend()


# In[7]:


# Volume*Open 成交總金額 
DataFrame_Tiger['Total Traded'] = DataFrame_Tiger['Open']*DataFrame_Tiger['Volume']
DataFrame_Bird['Total Traded'] = DataFrame_Bird['Open']*DataFrame_Bird['Volume']

DataFrame_Tiger['Total Traded'].plot(label='Tiger',figsize=(16,8),title='open price')
DataFrame_Bird['Total Traded'].plot(label='Bird')
plt.legend()


# In[8]:


# 股價 ↓ 成交量 ↑
print('Max Total Traded', DataFrame_Tiger['Total Traded'].idxmax())


# In[9]:


print('Max Total Traded', DataFrame_Tiger['Open'].idxmin())


# In[8]:


# 移動平均線 Moving Averages (MA)
DataFrame_Tiger['MA3'] = DataFrame_Tiger['Open'].rolling(3).mean()
DataFrame_Tiger['MA10'] = DataFrame_Tiger['Open'].rolling(10).mean()
DataFrame_Tiger[['Open','MA3','MA10']].plot(label='Tiger',figsize=(16,8))


# In[11]:


# Return (日報酬率 Daily Percentage Change)
# Return = (P(n) /  P(n-1)) - 1 (n 為時間)

DataFrame_Tiger['returns'] = DataFrame_Tiger['Close'].pct_change(1)
DataFrame_Bird['returns'] = DataFrame_Bird['Close'].pct_change(1)


# In[12]:


DataFrame_Tiger['returns'].hist(bins=20)


# In[13]:


# returns 日報酬率 可以看出兩者漲跌的時間與百分比幾乎一樣，在武漢肺炎期間，旅遊業利多利空的來源有許多相似之處
DataFrame_Tiger['returns'].plot(kind='kde',label='Tiger',figsize=(12,6))
DataFrame_Bird['returns'].plot(kind='kde',label='Bird')
plt.legend()


# In[28]:


# 3月報酬率
# 如果不賺不賠的情況下，每天的 returns = 0 => Cumulative Return = 1
# 由下圖可知，假設在 3/2 買入，不管在三月什麼時候賣掉，報酬率都小於 1 ，穩賠不賺。

DataFrame_Tiger['Cumulative Return'] = (1 + DataFrame_Tiger['returns']).cumprod()
DataFrame_Bird['Cumulative Return'] = (1 + DataFrame_Bird['returns']).cumprod()
DataFrame_Tiger['Cumulative Return'].plot(label='Tiger',figsize=(16,8),title='Cumulative Return')
DataFrame_Bird['Cumulative Return'].plot(label='Bird',figsize=(16,8),title='Cumulative Return')
plt.legend()


# In[ ]:




