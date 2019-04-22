# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:32:20 2018

@author: user
"""

    ### 2018_1222
    
 ## Defensive programming
 
# 撰寫 function 的時候要有好習慣，寫 docstring 
# Modularize 模組化, 大問題化小問題
# Check conditions on input/output (assertions)
    # 針對輸入/輸出做檢查點
    # Testing/Validation
        # Compare input/output pairs to specification
        # "it's not working !"
        # "How can i break my program ?"
    # Debugging
        # 找出一些會導致出錯的 pattern 
        # "Why is it not working ?"
        # "How can i fix my program ?"
        # 寫下當初設計這個 program 的限制跟概念/想法 : 有助於之後進行除錯
        # 可能是文法錯誤、靜態語意 : 大部分來說 pytohn 會自己幫你抓出這些錯誤
        # 要有一組已知的 輸出: 有助於確定某個輸入最後輸出的答案是不是如我所預期的一樣
        # 需要一個一個模組去做除錯的測試、再進行整體的除錯
        
        ## Testing approaches
        # Black-box testing :　不去管程式碼怎麼寫的。準備一組 testing data。往後都能拿這組 testing data 來測試 
            # 就算程式改寫了，也能拿這組 testing data 來測試
            # natural boundary  # 講義 p,11/43
                # Ex: X >= 0 or x <= 0 (某些條件)
                # 找一些極端的例子來做測試 (設計一些測試的組合)
            # 黑盒子測試也是為了第三方使用者去設計的程式
        # Glass-box testing :　 # 講義 p,13/43
            # path-complete: 一組 data 跑 if, 另一組 data 跑 else 去做測試 (每一個路徑都要去做測試)
# Bugs     
    # Runtime bugs
        # overt vs covert: 這個錯誤是否明顯 ? # 講義 p,17/43
# print statement
#     Good way to test hypothesis
#     when to print
#         enter function
#         parameters
#         function results
#     use bisection method
#         put print halway in code
#         decide where bug may be depending on values
# Error masseage
    # Logic erroes (hard)
        # 畫流程圖
# Debugging steps: # 講義 p,23/43 



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









