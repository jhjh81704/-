# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:35:23 2019

@author: user
"""


class money(object):  # 計算月薪
    
    def __init__(self, money_hr, hr, day):        
        self.money_hr = money_hr
        self.hr = hr
        self.day = day
    
    def __str__(self):
        """
        月薪:  = 時薪 (money_hr) * 小時 (hr) * 天數 (day)
        """
        return str('月薪' + str(self.money_hr * self.hr *self.day))
    
    def __sub__(self, other):  # 兩份工作行情的比較
        return str(float(self.money_hr * self.hr *self.day \
                        - other.money_hr * other.hr *other.day))

 ##使用參考指令:
a = money(120, 9, 26)
b = money(150, 9, 22)
print(a)
print(b)
print('相差' + (a.__sub__(b)))  # 計算兩份工作行情的比較


#--------------------------------------------------------------------
 

# 計算時薪的這支程式碼有錯誤，但目前找不到問題出在哪裡......
class money_hr(money):  # 計算時薪

    def __inti__(self, money_month, hr, day):
       
        money._inti__(self, hr, day)
        self.money_month = money_month
    

    def __str__(self):
        """
        時薪: 月薪 (money_month) / 小時 (hr) * 天數 (day)
        """
        return '時薪' + str(self.money_month / (self.hr *self.day))
   
    def __sub__(self, other):  # 兩份工作行情的比較
        return str(self.money_month / (self.hr *self.day) \
                         - other.money_month / (other.hr *other.day))

 #使用參考指令:
a = money_hr(28000, 9, 26)
b = money_hr(25000, 9, 22)
print(a)
print(b)
print('相差' + (a.__sub__(b))) # 計算兩份工作行情的比較