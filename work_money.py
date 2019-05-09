# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:35:23 2019

@author: user
"""


class Money(object):  # 計算月薪    
    def __init__(self, hr, day):        
        self.hr = hr
        self.day = day       
    
    def getMoney_hr(self): # 時薪
        return self.Money_hr
    
    def setMoney_hr(self, Money_hr):
        self.Money_hr = Money_hr
        
    def __str__(self):
        """
        月薪 = 時薪(self.Money_hr) * 小時(self.hr) * 天數(self.day)
        """
        return '月薪 =' + str(float(self.Money_hr * self.hr * self.day))
    
    def __sub__(self, other):  # 兩份工作行情的比較
        return str(float(self.Money_hr * self.hr *self.day \
                        - other.Money_hr * other.hr *other.day))


 ##使用參考指令:
a = Money(9, 26)
b = Money(9, 22)
a.setMoney_hr(120)
b.setMoney_hr(150)
print(a)
print(b)
print('相差: ' + (a.__sub__(b)))  # 計算兩份工作行情的比較


#--------------------------------------------------------------------
 

# 計算時薪的這支程式碼有錯誤，但目前找不到問題出在哪裡......
class Money_hr(Money):  # 計算時薪

   def __inti__(self, hr, day):
      
       Money.__inti__(self, hr, day)       
   
   def getMoney_month(self):
       return self.Money_month
   
   def setMoney_month(self, Money_month):
       self.Money_month = Money_month

   def __str__(self):
       """
       時薪 = 月薪 (self.Money_month) / 小時 (self.hr) * 天數 (self.day)
       """
       return '時薪 =' + str(float(self.Money_month / (self.hr *self.day)))
  
   def __sub__(self, other):  # 兩份工作行情的比較
       return str(float(self.Money_month / (self.hr *self.day) \
                        - other.Money_month / (other.hr *other.day)))

#使用參考指令:
c = Money_hr(9, 26)
d = Money_hr(9, 22)
c.setMoney_month(28000)
d.setMoney_month(25000)
print(c)
print(d)
print('相差:' + (a.__sub__(b))) # 計算兩份工作行情的比較