
# coding: utf-8

# In[1]:


'''
【课程2.2】  Pandas数据结构Series：基本概念及创建

"一维数组"Serise

'''


# In[9]:


# series数据结构
# series是带有标签的一维数组，可以保存任何数据类型（整数，字符串，浮点数，python对象等），轴标签统称为索引

import numpy as np
import pandas as pd

s = pd.Series(np.random.rand(5))
print(s)
print(type(s))

print(s.index,type(s.index))
print(list(s.index))

print(s.values,type(s.values))
# .index查看series索引，类型为rangeindex
# .values查看series值，类型是ndarray

# 核心：series相比于ndarray，是一个自带索引index的数组 → 一维数组 + 对应索引
# 所以当只看series的值的时候，就是一个ndarray
# series和ndarray较相似，索引切片功能差别不大
# series和dict相比，series更像一个有顺序的字典（dict本身不存在顺序），其索引原理与字典相似（一个用key，一个用index）

s = pd.Series(np.random.rand(5),index=list('abcde'))
print(s)


# In[17]:


# Series 创建方法一：由字典创建，字典的key就是index，values就是values

dic = {'a':1 ,'b':2 , 'c':3, '4':4, 5:'hell'}
s = pd.Series(dic)
print(s)
# 注意：key肯定是字符串，假如values类型不止一个会怎么样？


# In[22]:


# Series 创建方法二：由数组创建(一维数组)
arr = np.random.randn(5)
s = pd.Series(arr)
print(s)

ss = pd.Series(arr,index=list('abcde'),dtype=np.object,name='test') #name给Series取一个名字
print(ss)

sss = ss.rename('hello')
print(sss)


# In[24]:


# Series 创建方法三：由标量创建
s = pd.Series(10,index=range(4))
print(s)


# In[25]:


'''
【2.2】课程作业
'''


# In[30]:


# 有字典、数组创建Series

dic ={'jack':90.0, 'Marry':92.0, 'Tom':89.0, 'Zack':65.0}
s = pd.Series(dic,name='作业1')
print(s)

ar = np.array([90.0,92.0,89.0,65.0])
print(ar)

ss = pd.Series(ar, index=['Jack','Marry','Tom','Zack'],name='作业1')
print(ss)


# In[31]:


'''
【课程2.3】  Pandas数据结构Series：索引

位置下标 / 标签索引 / 切片索引 / 布尔型索引

'''


# In[38]:


# 位置下标，类似序列
s = pd.Series(np.random.rand(5))
print(s)
print(s[0],type(s[0]),s[0].dtype)
print(float(s[0]),type(float(s[0])))

#print(s[-1])


# In[42]:


# 标签索引

s = pd.Series(np.random.rand(5), index=list('abcde'))
print(s)

print(s['b'], type(s['b']),s['a'].dtype)

sci = s[['a','b','c']]
print(sci,type(sci))


# In[51]:


# 切片索引
s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5), index = list('abcde'))
print(s1,s2)

print(s1[1:4],s1[4]) #右开区间
print(s2['a':'d'], s2['d']) #两边都闭区间

print(s2[0:3],s2[3])

print('---')

print(s2[:-1])
print(s2[::2]) #下标索引，各2位取值


# In[58]:


# 布尔型索引

s = pd.Series(np.random.rand(3)*100)
s[4] = None
print(s)
bs1 = s > 50
bs2 = s.isnull()
bs3 = s.notnull()
print(bs1,type(bs1),bs1.dtype)
print(bs2,type(bs2),bs2.dtype)
print(bs3,type(bs3),bs3.dtype)


# In[59]:


'''
【2.3】课程作业
'''


# In[3]:


import pandas as pd
import numpy as np
s = pd.Series(np.random.rand(10)*100, index = list('abcdefghij'))
print(s['b'],s['c'])
print(s)
print(s[3:6])
print(s[s>50])


# In[4]:


'''
【课程2.4】  Pandas数据结构Series：基本技巧

数据查看 / 重新索引 / 对齐 / 添加、修改、删除值

'''


# In[6]:


# 数据查看

s = pd.Series(np.random.rand(15))
print(s.head(5))
print(s.tail(5))


# In[10]:


# 重新索引reindex

s = pd.Series(np.random.rand(3), index = list('abc'))
print(s)

s1 = s.reindex(['c','b','a','d'])
print(s1)

s2 = s.reindex(['c','b','a','d'], fill_value = 0)
print(s2)

# 根据新的索引重新排列顺序，不改变值得大小，如果新索引对应没有值，用NaN填充，fill_value来定义天充值值


# In[12]:


# Series对齐

s1= pd.Series(np.random.rand(3),index=['Jack','Mary','Tom'])
s2 = pd.Series(np.random.rand(3), index=['Wang','Jack','Mary'])

print(s1)
print(s2)
print(s1+s2)

# Series 和 ndarray 之间的主要区别是，Series 上的操作会根据标签自动对齐
# index顺序不会影响数值计算，以标签来计算
# 空值和任何值计算结果扔为空值


# In[17]:


#删除.drop

s = pd.Series(np.random.rand(5), index= list('ngjur'))
print(s)
s1 = s.drop('n')
print(s1)
print(s)
s2 = s.drop(['n','j'])
print(s2)

#删除元素后返回副本，不改变原来的值


# In[29]:


# 添加元素
s1 = pd.Series(np.random.rand(5), index= list('ngjur'))

s1['a'] = 23

s2 = pd.Series(np.random.rand(5))

s2[6]=100


s3 = s1.append(s2)
print(s3)


# In[33]:


# 修改

s1 = pd.Series(np.random.rand(5), index= list('ngjur'))
s1['n']=-100
s1[['j','r']] = 1000
print(s1)


# In[34]:


'''
【2.4】课程作业
'''


# In[40]:


import pandas as pd
import numpy as np

s = pd.Series(range(10),index=list('abcdefghij'))
print(s)

s[['a','e','f']]= 100
s1 = s.drop('b')
print(s1)


# In[42]:


s1 = pd.Series(np.random.rand(5)*10, index=list('abcde'))
s2 = pd.Series(np.random.rand(5)*10, index=list('edefg'))
print(s1, '\n', s2)
print(s1+s2)


# In[43]:


'''
【课程2.5】  Pandas数据结构Dataframe：基本概念及创建

"二维数组"Dataframe：是一个表格型的数据结构，包含一组有序的列，其列的值类型可以是数值、字符串、布尔值等。

Dataframe中的数据以一个或多个二维块存放，不是列表、字典或一维数组结构。

'''


# In[50]:


# Dataframe 数据结构
# Dataframe是一个表格型的数据结构，“带有标签的二维数组”。
# Dataframe带有index（行标签）和columns（列标签）

data = {'name':['Jack','Tom', 'Mary'],
       'age':[18,19,20],
       'gender':['m','m','w']}
frm = pd.DataFrame(data)
print(frm)
print(type(frm))

print(frm.index)
print(frm.columns)
print(frm.values)


# In[60]:


# Dataframe 创建方法一：由数组/list组成的字典
# 创建方法:pandas.Dataframe()

data1 = {'a':[1,2,3],
        'b':[3,4,5],
        'c':[6,7,8]}
df1 = pd.DataFrame(data1)
print(data1)
print(df1)

# 由字典创建DataFrame时，key是DataFrame的columns标签，值列表中的值数量必须一致,index默认为数字标签

data2 ={'one':np.random.rand(3),
       'two':np.random.rand(3)}
print(data2)
df2 = pd.DataFrame(data2)
print(df2)

df1 = pd.DataFrame(data1, columns=['c','a','b','d'])  # 按照columns重新排序，columns标签下没有值时填充NaN
print(df1)

df1 = pd.DataFrame(data1, columns=['c','a'])  # 如果columns重新指定时候，列的数量可以少于原数据
print(df1)

df2 = pd.DataFrame(data2, index=['f1','f2','f3']) # 重新定义index标签时，数量必须跟值的数量一样
print(df2)


# In[63]:


# Dataframe 创建方法二：由Series组成的字典

data1 = {'one':pd.Series(np.random.rand(2)),
        'two':pd.Series(np.random.rand(3))}
print(data1)
df1 = pd.DataFrame(data1)
print(df1)

data1 = {'one':pd.Series(np.random.rand(2)),
        'two':pd.Series(np.random.rand(3),index=list('abc'))}
print(data1)
df1 = pd.DataFrame(data1)
print(df1)

# Series的长度可以不一致
# 如果两个Series的index不一致时，合并标签，没有值得位置填充NaN


# In[67]:


# Dataframe 创建方法三：通过二维数组直接创建、

ar = np.random.rand(9).reshape(3,3)
df = pd.DataFrame(ar, index = range(3), columns=list('abc'))
print(df)
# 通过二维数组直接创建Dataframe，得到一样形状的结果数据，如果不指定index和columns，两者均返回默认数字格式
# index和colunms指定长度与原数组保持一致


# In[70]:


# Dataframe 创建方法四：由字典组成的列表

data = [{'one':1,'two':2},{'one':5,'two':10,'three':20}]
df = pd.DataFrame(data)
df2 = pd.DataFrame(data,index=['a','b'])
print(df)
print(df2)


# In[72]:


# Dataframe 创建方法五：由字典组成的字典

data = {'Jack':{'math':90,'english':80},
       'Marry':{'math':90,'art':91}}

df = pd.DataFrame(data)
print(df)

df1 = pd.DataFrame(data,index=['a','b','c'])
print(df1)


# In[73]:


'''
【2.5】课程作业
'''


# In[78]:


#通过数组创建

ar = np.random.randint(0,10,size=(5,4))
print(ar)

df = pd.DataFrame(ar,index=list('abcde'),columns=['four','one','three','two'])
print(df)


# In[81]:


# 由数组/list组成的字典

data = {'four':[4,5,6,7,8],
       'one':[1,2,3,4,5],
       'three':[3,4,5,6,7],
       'two':[2,3,4,5,6]}
df = pd.DataFrame(data, index = list('abcde'))
print(df)


# In[86]:


# 由Series组成的字典
data = {'four':np.arange(4,9),
       'one':np.arange(1,6),
       'three': np.arange(3,8),
       'two': np.arange(2,7)}

print(data)
df = pd.DataFrame(data,index=list('abcde'))
print(df)


# In[87]:


'''
【课程2.6】  Pandas数据结构Dataframe：索引

Dataframe既有行索引也有列索引，可以被看做由Series组成的字典（共用一个索引）

选择列 / 选择行 / 切片 / 布尔判断

'''


# In[99]:


# 选择行与列

df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                   index = ['one','two','three'],
                   columns = ['a','b','c','d'])
print(df)

print(df['a'],type(df['a']))
print(df[['a','b']])

# 选择列，直接索引cloumns标签，多个标签显示多列数据，输出格式为Series或者DataFrame

print('----')

data1 = df.loc['one']

print(data1,type(data1))
print(data1.index) # 选取一行数据输出一个series，原DataFrame的columns的值变成series的index

data1 = df.loc[['one','two']]
print(data1,type(data1))


# In[104]:


# df[] - 选择列
# 一般用于选择列，也可以选择行
df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                   index = ['one','two','three'],
                   columns = ['a','b','c','d'])
print(df)
print('-----')

data1 = df['a']
data2 = df[['b','c']]  # 尝试输入 data2 = df[['b','c','e']]
print(data1)
print(data2)
# df[]默认选择列，[]中写列名（所以一般数据colunms都会单独制定，不会用默认数字列名，以免和index冲突）
# 单选列为Series，print结果为Series格式
# 多选列为Dataframe，print结果为Dataframe格式

data3 =df[:1]
print(data3,type(data3))
# df[]中为数字时，默认选择行，且只能进行切片的选择，不能单独选择（df[0]）
# 输出结果为Dataframe，即便只选择一行
# df[]不能通过索引标签名来选择行(df['one'])


# In[115]:


# df.loc[] - 按index选择行
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df1)
print(df2)
print('-----')

data1 = df1.loc['one']
data2 = df2.loc[1]
print(data1,type(data1))
print(data2,type(data2))

data3 = df1.loc[['one','three']]
print(data3,type(data3))

data4 = df2.loc[[1,3,4]]  #第4行不存在，填充NaN
print(data4)

data5 = df1.loc['one':'three']
print(data5)
data6 = df2.loc[1:3]
print(data6)
#切片两边都是闭区间

 核心笔记：df.loc[label]主要针对index选择行，同时支持指定index，及默认数字index


# In[123]:


# df.iloc[] - 按照整数位置（从轴的0到length-1）选择行
# 类似list的索引，其顺序就是dataframe的整数位置，从0开始计

df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('------')

print(df.iloc[0]) # 取第1行，输出series对象

print(df.iloc[-1]) # 取倒数第一行，输出对象为series
# 单位置索引
# 和loc索引不同，不能索引超出数据行数的整数位置

print(df.iloc[[0,3,1]]) #索引多行，顺序可变

print(df.iloc[1:3])
print(df.iloc[::3]) #隔3行索引


# In[5]:


# 布尔型索引
# 和Series原理相同
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('------')

b1 = df < 20
print(b1,type(b1)) 
print(df[df<20])
print('---')

b2 = df['a'] > 50
print('this is b2 \n', b2,type(b2))
print(df[df['a']>50])  #保留df['a']这一列中，df['a']>50为True的那一行数据

b3 = df[['a','b']] > 50 #保留选中的行，满足条件的返回True，否则返回False
print('this is b3 \n', b3)
print(df[b3])

b4 = df.loc[['one','tree']] > 50
print('this is b4 \n', b4)
print(df[b4])
# 多行做判断
# 索引结果保留 所有数据：True返回原数据，False返回值为NaN


# In[12]:


# 多重索引：比如同时索引行和列
# 先选择列再选择行 —— 相当于对于一个数据，先筛选字段，再选择数据量
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                 index  = ['one', 'two', 'three', 'four'],
                 columns = list('abcd'))
print(df)
print('----')

print(df[['a','c']].loc[['two','four']])
print('----')

print(df[['b','c','d']].iloc[0:3])
print('----')


print(df[['b','c','d']].iloc[::2])
print('----')


# In[ ]:


'''
【课程2.7】  Pandas数据结构Dataframe：基本技巧

数据查看、转置 / 添加、修改、删除值 / 对齐 / 排序

'''


# In[18]:


# 数据查看、转置

df = pd.DataFrame(np.random.rand(16).reshape(8,2)*100,
                 columns = ['a','b'])
print(df)
print('---')

print(df.head(4))
print('---')

print(df.tail(3))
print('---')

print(df.T)


# In[22]:


# 添加与修改
df  = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  columns = ['a','b','c','d'])
print(df)
print('---')

df['e']= [1,2,3,4]
print(df)
print('---')

df.loc[4] = 100
print(df)
print('---')

df.iloc[2] = 40
print(df)
print('---')


# In[35]:


# 删除  del / drop()

df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                 columns = ['a','b','c', 'd'])
print(df)
print('---')

del df['a']
print(df)   #删除列，改变原数据
print('---')


print(df.drop(1,inplace=False)) #删除行，inplace=Flase不改变元数据
print('---')
print(df)
print('---')

print('d&axis=1')
print(df.drop(['d'],axis=1))  #删除列，inplace=Flase不改变元数据

print(df)


# In[42]:


# 对齐

df1 =pd.DataFrame(np.random.randn(10,4),columns=['A','B','C','D'])
df2 =pd.DataFrame(np.random.randn(7,3),columns=['A','B','C'])

print(df1)
print('---')
print(df2)
print('---')
print(df1+df2)  
# DataFrame对象之间的数据自动按照列和索引（行标签）对齐
#对应数字相加，不可计算用NaN填充


# In[48]:


# 排序1 - 按值排序 .sort_values
# 同样适用于Series
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df1)
print('---')

print(df1.sort_values(['a'],ascending=True))
print(df1.sort_values(['a'],ascending=False))
# ascending参数：设置升序降序，默认升序
# 单列排序


print('---')
df2 = pd.DataFrame({'a':[1,1,1,1,2,2,2,2],
                   'b':list(range(8)),
                   'c':list(range(8,0,-1))})

print(df2)
print('多列排序，按列顺序排序')
print(df2.sort_values(['a','c']))


# In[50]:


# 排序2 - 索引排序 .sort_index

df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  index = [5,4,3,2],
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  index = ['h','s','x','g'],
                   columns = ['a','b','c','d'])

print(df1)
print(df1.sort_index())

print('---')
print(df2)
print(df2.sort_index())
# 按照index排序
# 默认 ascending=True, inplace=False


# In[51]:


'''
【课程2.6】  课程作业

'''


# In[60]:


# 【课程2.6  Pandas数据结构Dataframe：索引】 课程作业

import numpy as np  #科学计算的包
import pandas as pd  #列表数据处理的包

df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                 columns=list('abcd'),
                 index=['one','two','three','four'])
print(df)

print('quiz 1')
print(df[['b','c']])
print('quiz 2')
print(df.iloc[2:5])
print('quiz 3')
print(df.iloc[0:2])

print('quiz 3')
print(df[df>50])
print()


# In[63]:


'''
【课程2.7】  课程作业

'''


# In[2]:


#【课程2.7  Pandas数据结构Dataframe：基本技巧】 课程作业
print('作业1')
df = pd.DataFrame(np.random.rand(9).reshape(3,3)*100,
                 index=list('abc'),
                 columns=['v1','v2','v3'])
print(df)
df.sort_index(ascending=False,inplace=True)
print(df)
df.sort_values('v2',ascending=False,inplace=True)
print(df)

print('\n 作业2')
df1 = pd.DataFrame(np.random.rand(10).reshape(5,2)*100,
                 index=list('abcde'),
                 columns=['v1','v2'])
print(df1)
df2 = df1.T
df2['b']=100
del df2['e']
print(df2)


# In[7]:


import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.rand(9).reshape(3,3)*100,
                  index=list('abc'), 
                   columns=['v1','v2','v3'])
print(df1)

df1.sort_index(ascending=False, inplace=True) # inplace = true to repalce the origianl DataFrame

print(df1)

df1.sort_values('v2',ascending=False,inplace=True)

print(df1)


# In[12]:


import numpy as np
import pandas as pd

dfr = pd.DataFrame(np.random.rand(10).reshape(5,2)*100,
                  index=list('abcde'), columns=['v1','v2'])
print(dfr)

dfr2= dfr.T

print(dfr2)


# In[27]:


import numpy as np
import pandas as pd

s1 = pd.Series({'Jack':90.0, 'Marry':92.0, 'Tome':89.0},name='作业1')

print(s1)

s2 = pd.Series(data=[90.0, 92.0, 89.0], index = ['Jack', 'Marry', 'Tom'], name='zuoye1')
print(s2)

s3 = pd.Series(data=np.random.rand(10)*100, index=list('abcdefghij'))
print(s3)
print('---')
print(s3[['b','c']])

print('---')
print(s3[3:6])

print('---')
print(s3[s3>50])



# In[36]:


s4 = pd.Series(data=range(10),index=list('abcdefghij'))
print(s4)
print('---')

# s4['a']=100
# s4['e']=100
# s4['f']=100

s4[['a','e','f']]=100

s4 = s4.drop('b')

print(s4)


# In[38]:


s1 = pd.Series(data=np.random.rand(5),index=list('abced'))
s2 = pd.Series(data=np.random.rand(5),index=list('cdefg'))

print(s1+s2)


# In[50]:


#Creat dataFrame by n-dimensional array

data= np.random.randint(1,10,size=(5,4))
print(data, type(data))

df1= pd.DataFrame(data,index=list('abcde'),columns=['four','one','three','two'])
print(df1)



# In[69]:


data1=np.random.rand(16).reshape(4,4)*100
df1=pd.DataFrame(data1,index=['one','two','three','four'],columns=list('abcd'))
print(df1)
print('---')

print(df1[['b','c']])
print('---')

print(df1.loc['three'])
print('---')

print(df1.iloc[2:6])

print('---')
print(df1[df1>50])

print('---')
print(df1.loc[['two','one']])

