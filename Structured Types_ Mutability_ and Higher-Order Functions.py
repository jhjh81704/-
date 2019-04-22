# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 00:27:23 2018

@author: user
"""

    ### 2018_1210    錄音檔 REC001.WAV 
    
    
## Tuples: 將元素放在 () 裡面，並且用「,」隔開。 例如：(A, B, C,.....)
# 你在 string 怎麼裁切，你在 Tuple 就怎麼裁切。
# Tuple 只能讀取, 不能寫入; 你無法去改 Tuple 的內容

# def q_and_r(x, y):  # p,6/50
#    q = x // y  # // 求商
#    r = x % y  #  % 求餘數
#    return (q, r)

    

    
## Manipulating tuples  p,7/50

#def get_data(aTuple):    # 這個例子我還是看不懂.....  2019/4/1 復習的過程中好像有漸漸了解
#    nums = ()
#    words = ()
#    for t in aTuple:
#        nums = nums + (t[0], )
#        if t[1] not in words:
#            words = words + (t[1], )
#    min_nums = min(nums)
#    max_nums = max(nums)
#    unique_words = len(words)
#    return (min_nums, max_nums, unique_words)

#example: aTuple = ((1,'my'),(3,'yours'),(5,'ours'),(7,'my')) # aTuple 是一個大的 Tuple, 裡面包了很多個小 Tuple
#>> get_data(((1,'my'),(3,'yours'),(5,'ours'),(7,'my')))



## List: 使用的是 []。幾乎看起來跟 Tuple 沒什麼兩樣。  p,8/50
## 例如：[4] rather then (4,)
## 可以在裡面放入不同類型的資料 (很少使用)
## List 裡面的內容可以修改



 ### 錄音檔 REC002.WAV  

## convert string to list 。
    ## 應用上：對特定格式的修改很有幫助

  # p,13/50
#L = [2, 1, 3]

#L.append(5)
##>> [2, 1, 3, 5]



  # p,14/50
#L1 = [2, 1, 3]
#L2 = [4, 5, 6]
#
#L3 = L1 + L2
##>> [2,1,3,4,5,6]
  
#L1.extend([0, 6])
##>> [2,1,3,0,6]

#L1.append([0, 6])
##>> [2,1,3,[0,6]]



  # p,15/50
#L = [2, 1, 3, 6, 3, 7, 0]
#
#L.remove(2)
##>> [1,3,6,3,7,0]
#
#L.remove(3)
##>> [1,6,3,7,0]
#
#del(L[1])
##>> [1,3,7,0]
#
#L.pop()
##>> [1,3,7]
  
  

  # p,16/50
#s = 'I <3 cs'
#
#L = list(s)
#>> ['I', ' ', '<', '3', ' ', 'c', 's']
#
#L = s.split()
#>> ['I', '<3', 'cs']
#
#L = s.split('<')
#>> ['I ', '3 cs']



#L = ['a', 'b', 'c']

#''.join(L)
#>> 'abc'

#'_'.join(L)
#>> 'a_b_c'



  # p,17/50
#L = [9, 6, 0, 3]
#sorted(L)  # 不會把 L 改掉
#
#L.sort()  # 會把 L 改掉
#>> [0, 3, 6, 9]
#
#L.reverse()
#>> [9, 6, 3, 0]




## Mutation and itertation  p,26/50
    ## list 有副作用 >> 可修改的特性
    ## 有關於 for loop 在這部分的副作用，請仔細聽上課錄音檔
    ## 針對這個副作用，我們建立副本來解決
    
#def remove_dups(L1, L2):
#    for e in L1:
#        if e in L2:
#            L1.remove(e)
#remove_dups(L1, L2)
#
#
#L1 = [1, 2, 3, 4]
#L2 = [1, 2, 5, 6]
#
#
#def remove_dups_new(L1, L2):  # 建立副本來解決問題
#    L1_copy = L1[:]
#    for e in L1_copy:
#        if e in L2:
#            L1.remove(e)
#remove_dups_new(L1, L2)





    ### 2018_1217   錄音檔 REC003.WAV

#def fact(n):  # p,28~29/50
#    
#    if n == 1:   ## base case 在遞迴運算非常重要
#        return n
#    else:
#        return n * fact(n-1)
#
#
#def fib(x):
#    """assumes x an int >= 0
#        return Fibonacci of x"""
#    
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)  
#
#L = [1, -2, 3.4]
#
#def applyToEach(L, f):  # p,28~29/50
#    for i in range(len(L)):
#        L[i] = f(L[i])
#
#applyToEach(L, abs)
#print(L)
#
#applyToEach(L, int)
#print(L)
#
#applyToEach(L, fact)
#print(L)
#
#applyToEach(L, fib)
#print(L)





## Generalization of higher order function(HOPs)  p,31/50

#for elt in map(abs,[1, -2, 3, -4]):
#    print(elt)



#L1 = [1, 28, 36]
#L2 = [2, 57, 9]
#
#for elt in map(min, L1, L2):
#    print(elt)




    ## How to store student information  p,34/50

#names = ['Ana', 'John', 'Denise', 'Katy']
#grade = ['B', 'A+', 'A', 'A']
#course = [2.00, 6.0001, 20.002, 9.01]
#
#def get_grade(student, name_list, grade_list, course_list):
#    i = name_list.index(student)
#    grade = grade_list[i]
#    course = course_list[i]
#    return (course, grade)



    ## Dictionary operations  p,36/50  {}: Dictionary

#grades = {'Ana': 'B', 'John':'A+', 'Denise': 'A', 'Katy': 'A'}
#    
#grades['Sylvan'] = 'A'
#>> grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A', 'Sylvan': 'A'}
#
#del(grades['Sylvan'])
#>> grades = {'Ana': 'B', 'John':'A+', 'Denise': 'A', 'Katy': 'A'}
#
#grades.keys()
#>> dict_keys(['Ana', 'John', 'Denise', 'Katy'])
#
#grades.values()
#>> dict_values(['B', 'A+', 'A', 'A'])




  ###錄音檔 REC004.WAV

    ## creating a dictionary   
    # 附件有一個 lyric.py  p,41/50
與佳駿討論



  ## p,47/50
#def fib_efficient(n, d):
#    if n in d:
#        return d[n]
#    else:
#        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#        d[n] = ans
#    return ans
#
#d = {1:1, 2:2}
#print(fib_efficient(6, d))














