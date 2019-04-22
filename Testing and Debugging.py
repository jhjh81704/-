# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:32:20 2018

@author: user
"""

    ### 2018_1224


# 講義 p,27/43 ~ p,43/43 錄音檔 REC003
#與佳駿討論
 # 請用以下範例進行除錯↓↓↓
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False
    
    
def silly(n):
    
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
     
    
# try to run: isPal(['aba'])
# try to run: isPal(['ab'])
         
    
# take a break and come back to the bug later

# 找人討論程式碼也是一個不錯的學習方法









