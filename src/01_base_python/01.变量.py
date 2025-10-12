
"""
语法基础-变量
"""

# 数字
a = 10
b = 20

print(a + b) # 30

# 字符串
str1 = 'hello world'
print(str1) # hello world

str2 = 'TOM'
print(str2+' '+str1) # TOM hello world

# 布尔
isOk = True
print(isOk) # True
isOk = False
print(isOk) # False

# 列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1+list2) # [1, 2, 3, 4, 5, 6]

list3 = [
    [1,1],
    [2,1,'a'],
    [3,1,False],
    [4,2,str2],
    [5,1,str1+str2],
    a+b
]
print(list3)
#[[1, 1], [2, 1, 'a'], [3, 1, False], [4, 2, 'TOM'], [5, 1, 'hello worldTOM'], 30]


# 函数
def add(a,b):
    """
     计算两个数的和。

     Args:
         a (int): 第一个加数。
         b (int): 第二个加数。

     Returns:
         int: 两个加数的和。
     """
    return a+b
print(add(1,2))