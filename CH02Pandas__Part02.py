
# coding: utf-8

# In[1]:


'''
【课程2.8】  时间模块：datetime

datetime模块，主要掌握：datetime.date(), datetime.datetime(), datetime.timedelta()

日期解析方法：parser.parse

'''


# In[6]:


# datetime.date：date对象

import datetime 
today = datetime.date.today()
print(today,type(today))
print(str(today),type(str(today)))
# datetime.date.today 返回今日
# 输出格式为 date类

t = datetime.date(2016,1,3)
print(t,type(t))

# (年，月，日) → 直接得到当时日期


# In[12]:


# datetime.datetime：datetime对象

now = datetime.datetime.now()
print(now,type(now))
print(str(now),type(str(now)))
# .now()方法，输出当前时间
# 输出格式为 datetime类
# 可通过str()转化为字符串

t1 = datetime.datetime(2016,2,2)
t2 = datetime.datetime(2014,1,3,12,30,45)
print(t1,'\n',t2)

print(t1-t2,type(t1-t2))
# 相减得到时间差 —— timedelta


# In[21]:


# datetime.timedelta：时间差

today = datetime.datetime.today()
print(today)

yesterday = today - datetime.timedelta(1,60) # 1天，60秒
print(yesterday)

print(today-datetime.timedelta(7))


# In[25]:


# parser.parse：日期字符串转换

from dateutil.parser import parse

date = '12-05-2017'
t = parse(date)
print(t,type(t))
# 字符串转换成datetime格式

print(parse('2000-1-1'), '\n',
     parse('5/1/2015'), '\n',
     parse('5/1/2015',dayfirst=True), '\n', # 国际通用格式中，日在月之前，可以通过dayfirst来设置
     parse('5.1.2015'), '\n',
     parse('22/1/2015'),'\n',
     parse('Jan 31, 1997 10:45 PM'))
# 各种格式可以解析，但无法支持中文


# In[26]:


'''
【课程2.8】  课程作业

'''


# In[12]:


#【课程2.8  时间模块：datetime】 课程作业
# 作业1：请调用datetime模块，输出以下时间信息

import datetime as dt

print(dt.datetime.now())

dt1 = dt.datetime(2017,5,1,12,30,0)
print(dt1)

dt2 = dt.datetime(2000, 12, 1, 0, 0, 0)
print(dt2)

st = '12-1-2000'
from dateutil.parser import parse
dt1 = parse(st)

print(dt1)


# In[ ]:


'''
【课程2.9】  Pandas时刻数据：Timestamp

时刻数据代表时间点，是pandas的数据类型，是将值与时间点相关联的最基本类型的时间序列数据

pandas.Timestamp()

'''


# In[13]:


# pd.Timestamp()

import numpy as np
import pandas as pd

date1 = datetime.datetime(2016,12,1,12,45,30)
date2 = '2017-12-21'
t1 = pd.Timestamp(date1)
t2 = pd.Timestamp(date2)

print (t1,type(t1))
print(t2,type(t2))

print(pd.Timestamp('2017-12-22 15:00:22'))


# In[16]:


# pd.to_datetime

import pandas as pd
from datetime import datetime

date1 = datetime(2017,12, 2, 15)
date2 = '2017.8.9'

t1 = pd.to_datetime(date1)
t2 = pd.to_datetime(date2)

print(t1, type(t1))
print(t2, type(t2))

late_list = ['2018-8-9', '2019.2.8']
t2 = pd.to_datetime(late_list)
print(t2, type(t2))


# In[22]:


from datetime import datetime
import pandas as pd

date3 = ['2017-2-1','2017-2-2','2017-2-3','hello world!','2017-2-5','2017-2-6']
t3 = pd.to_datetime(date3, errors = 'ignore')
print(t3,type(t3))
# errors = ignore，表示遇到错误不执行，返回原数据，数据类型是数组

t4 = pd.to_datetime(date3, errors = 'coerce')
print(t4,type(t4))
# errors = coerce,不可扩展，缺失值返回NaT（Not a Time），结果认为DatetimeIndex


# In[24]:


'''
2.9 课程作业
'''




# In[52]:


# 作业1
date_list = []
for i in range(31):
    date = '2017-12-%i' %(i+1)
    date_list.append(str(date))
    
print(date_list)
print('---')

import pandas as pd
t1 = pd.to_datetime(date_list)
print(t1, type(t1))
print('---')

date_count = len(date_list)
mid = round(date_count/2)
print(date_count, mid)

print(t1[mid], type(t1[mid]))

import math
print(math.ceil(1.2))
print(math.floor(1.2))
print(round(1.2))


# In[68]:


# 作业2
import os, sys

os.getcwd() #获取当前路径
path = '/Users/KevinTang/DataAnalysist/Numpy&Pandas'
date_txt = open (path + '/date_info.txt', 'w', encoding = 'utf8' ) #创建一个txt文件并打开为写入模式

#定义字符串
st = ''
for i in range(8):
    st = st + '2015010%i,' %(i+1)
st = st.rstrip(',')  #去除末尾的某种字符，空则去除末尾空格

#写入字符串，并关闭文件
date_txt.write(st)
date_txt.close()


#打开文件为只读模式
get_date_txt = open(path + 'date_info.text', 'r', encoding = 'utf8')

# print(get_date_txt.read())

#读取字符串，并按照‘，’分隔，存入数组
date_st = get_date_txt.read()
date_list = date_st.split(',')
#print(date_list)

# 转化为时间戳数据
import pandas as pd
date_stmp = pd.to_datetime(date_list)
print(date_stmp, type(date_stmp))
    


# In[79]:


import xlrd  #读取EXCEL库

path = '/Users/KevinTang/DataAnalysist/Numpy&Pandas/11.xlsx'

data_file = xlrd.open_workbook('/Users/KevinTang/DataAnalysist/Numpy&Pandas/22.xls')

print(data_file.sheet_names())




# In[1]:


'''
【课程2.10】 Pandas: datetimeIndex
pd.date_range()

'''


# In[7]:


# pd.DatetimeIndex()与时间序列，可作为数组的索引

import pandas as pd
import numpy as np

rng = pd.DatetimeIndex(['20170101', '20170102','20170103','20170104'])
print(rng, type(rng))
#直接定义时间戳索引，可以用字符串列表，可也以用datetiem.datetime

print('---')
print(rng[2],type(rng[2]))
#datetimeIndex相当于一个时间戳组成的列表，可以用索引引用

vl = pd.Series(np.random.rand(len(rng)),index = rng)
print(vl, type(vl))

#时间戳索引作为一维数组的索引


# In[25]:


# pd.date_range() 生成日期范围,生成的结果是datetimeIndex

rng1 = pd.date_range(start='20170101', end='20170130',freq='D') # 默认freq为日历天数,按月freq='M'
print(rng1,type(rng1))

rng2 = pd.date_range(start='2017-1-1', periods=7)
print(rng2)

rng3 = pd.date_range(end = '1/23/2017 14:00:00', periods=10, normalize=True) 
#datetimeIndex相当于一个时间戳组成的列表，可以用索引引用
print(rng3)

rng4 = pd.date_range('20170201', periods=7, name='hey time index', closed='left')
print(rng4)

rng5 = pd.date_range('20170201', periods=7, name='hey time index', closed='right')
print(rng5,type(rng5))

# closed：默认为None的情况下，左闭右闭，left则左闭右开，right则左开右闭

print(list(pd.date_range(start='20170101', periods=4)))
# 把datetiemIndex转化为列表，列表里的元素为timestamp


# In[35]:


# pd.date_range()-日期范围：频率(1)

print(pd.date_range('2017/1/1', '2017/1/4')) #默认评率为日
print(pd.date_range('2017/1/1', '2017/1/4', freq='B')) #freq='B'为按工作日
print(pd.date_range('2017/1/1', '2017/1/2', freq='H')) #按小时
print(pd.date_range('2017/1/1', '2017/1/2', freq='T')) #按分钟T/MIN
print(pd.date_range('2017/1/1', '2017/1/4', freq='S')) #按秒
print(pd.date_range('2017/1/1 12:00:00', '2017/1/1 12:00:01', freq='L')) #按毫秒，千分之一秒
print(pd.date_range('2017/1/1 12:00:00', '2017/1/1 12:00:01', freq='U')) #按微秒，百万分之一秒

print(pd.date_range('2017/1/1', '2017/2/1', freq='W-TUE'))
# W-MON：从指定星期几开始算起，每周
# 星期几缩写：MON/TUE/WED/THU/FRI/SAT/SUN

print(pd.date_range('2017/1/1', '2017/12/1', freq='WOM-2MON'))
# WOM-2MON：每月的第几个星期几开始算，这里是每月第二个星期一


# In[42]:


# pd.date_range()-日期范围：频率(2)

print(pd.date_range('2017','2018', freq = 'M'))  #M:每个月的最后一个日历日
print(pd.date_range('2017','2018', freq = 'Q-FEB'))  
#Q-月：指定月为季度末，每个季度末最后一个日历日
# Q:默认12月为季度末
print(pd.date_range('2017','2020', freq = 'A-FEB')) 
#A-月：每年指定月份的最后一个日历日
print('------')

print(pd.date_range('2017','2018', freq = 'BM'))  
print(pd.date_range('2017','2020', freq = 'BQ-DEC'))  
print(pd.date_range('2017','2020', freq = 'BA-DEC')) 
print('------')
# BM：每月最后一个工作日
# BQ-月：指定月为季度末，每个季度末最后一月的最后一个工作日
# BA-月：每年指定月份的最后一个工作日

print(pd.date_range('2017','2018', freq = 'MS'))  
print(pd.date_range('2017','2020', freq = 'QS-DEC'))  
print(pd.date_range('2017','2020', freq = 'AS-DEC')) 
print('------')
# M：每月第一个日历日
# Q-月：指定月为季度末，每个季度末最后一月的第一个日历日
# A-月：每年指定月份的第一个日历日

print(pd.date_range('2017','2018', freq = 'BMS'))  
print(pd.date_range('2017','2020', freq = 'BQS-DEC'))  
print(pd.date_range('2017','2020', freq = 'BAS-DEC')) 
print('------')
# BM：每月第一个工作日
# BQ-月：指定月为季度末，每个季度末最后一月的第一个工作日
# BA-月：每年指定月份的第一个工作日


# In[45]:


# pd.date_range()-日期范围：复合频率

print(pd.date_range('2017/1/1','2017/2/2',freq='7D')) #7天
print(pd.date_range('2017/1/1', '2017/1/2', freq='2h30min')) # 2小时30分钟
print(pd.date_range('2017','2018',freq='2M')) # 2天


# In[52]:


# asfreq：时期频率转换

ts = pd.Series(np.random.rand(4), index=pd.date_range('2017/1/1','2017/1/4'))
print(ts)

ts1 = ts.asfreq('4H', method='ffill')
print(ts1)
# 改变频率，这里是D改为4H
# method：插值模式，None不插值，ffill用之前值填充，bfill用之后值填充


# In[55]:


# pd.date_range()-日期范围：shift超前/滞后数据
ts = pd.Series(np.random.rand(4), index=pd.date_range('2017/1/1','2017/1/4'))
print(ts)
print('----------')

print(ts.shift(2))
print('----------')

print(ts.shift(-2))
print('----------')


# In[ ]:


'''
【课程2.11】  Pandas时期：Period

核心：pd.Period()

'''


# In[4]:


# pd.Period()创建时期

import pandas as pd
import numpy as np

p = pd.Period('2017', freq='M')
print(p, type(p))
#生成一个以2017-1开始，月为频率的时间构造器
# pd.Period()参数：一个时间戳 + freq参数 ——freq用于指明该period的长度，时间戳则说明该period在时间轴上的位置

print(p+1)
print(p-1)
print(pd.Period('2012', freq = 'A-DEC') - 1)

#通过加减整数，将周期整体移动
# 这里是按照 月、年 移动


# In[10]:


# pd.period_range()创建时期范围

prng = pd.period_range('1/1/2011', '1/1/2012', freq = 'M')
print(prng, type(prng))
print(prng[0], type(prng[0]))

ts = pd.Series(np.random.rand(len(prng)), index=prng)
print(ts, type(ts))
print(ts.index)
#时间序列

# Period('2011', freq='A-DEC')可以看成多个时间期的时间段中的游标
# Timestamp表示一个时间戳，是一个时间截面；Period是一个时期，是一个时间段。但两者作为index时区别不大


# In[16]:


# asfreq：频率转换

p = pd.Period('2017', 'A-DEC')
print(p)
print('---')
print(p.asfreq('M', how = 'start'))
print('---')
print(p.asfreq('M', how = 'end'))
print('---')

# 通过.asfreq（freq, method=None, how=None）方法转换为别的评率

prng = pd.period_range('2017', '2018', freq='M')
ts1 = pd.Series(np.random.rand(len(prng)), index=prng)
print(ts1,type(ts1))
print('---')

ts2 = pd.Series(np.random.rand(len(prng)), index=prng.asfreq('D', how='start'))
print(ts2,len(ts2))

print(ts2.head())


# In[4]:


# 时间戳与时期之间的转换：pd.to_period()、pd.to_timestamp()

import numpy as np
import pandas as pd

rng = pd.date_range('2016/1/1', periods=10, freq='M')
prng=pd.period_range('2017', '2018', freq='M')

print(rng, type(rng))
print(prng, type(prng))
print('----')

ts1 = pd.Series(np.random.rand(len(rng)), index=rng)
print(ts1.head())
print(ts1.to_period().head())
# index从每月最后一日转换为每月

ts2 = pd.Series(np.random.rand(len(prng)), index=prng)
print(ts2.head())
print(ts2.to_timestamp().head())
# index从每月，转换为每月第一天


# In[5]:


'''
【课程2.12】  时间序列 - 索引及切片

TimeSeries是Series的一个子类，所以Series索引及数据选取方面的方法基本一样

同时TimeSeries通过时间序列有更便捷的方法做索引和切片
 
''''''
【课程2.12】  时间序列 - 索引及切片

TimeSeries是Series的一个子类，所以Series索引及数据选取方面的方法基本一样

同时TimeSeries通过时间序列有更便捷的方法做索引和切片
 
'''


# In[18]:


# 索引

from datetime import datetime

rng = pd.date_range('2017/1', '2017/3')
ts = pd.Series(np.random.rand(len(rng)), index=rng)
print(ts.head())

print(ts[0])
print(ts[:2])

print('-----------')

print(ts['2017/1/2'])
print(ts['20170103'])
print(ts['1/10/2017'])
print(ts[datetime(2017,1,20)])



# In[23]:


# 切片

rng = pd.date_range('2017/1', '2017/3', freq='12H')
ts = pd.Series(np.random.rand(len(rng)), index=rng)

print(ts['2017/1/5':'2017/1/10'])
print('--------')
# 和Series按照index索引原理一样，也是末端包含

print(ts['2017/2'].head())


# In[29]:


# 重复索引的时间序列

dates = pd.DatetimeIndex(['1/1/2015','1/2/2015','1/3/2015','1/4/2015','1/1/2015','1/2/2015'])
print(dates, type(dates))
print('------')

ts = pd.Series(np.random.rand(6), index=dates)
print(ts)
print('------')
print(ts.is_unique, ts.index.is_unique) #is_unique检查值是否重复，index.is_unique检查检索是否重复
print('------')

print(ts.groupby(level=0).mean()) #通过groupby做分组，重复的值这里用平均值处理
print(ts.groupby(level=0).sum()) #通过groupby做分组，重复的值这里用求和处理

