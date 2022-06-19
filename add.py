# -*- coding:utf-8 -*-
"""
data:2022/06/18
author:lupan1551
"""

#这是一个帮助你求和的道具
 
#main
def zhangqinghanbmi():
    firstnumber=float(input("请输入第一个数："))
    secnumber=float(input("请输入第二个数"))
    next=int(input("继续输入请按1\n否请按0:"))
    end=firstnumber+secnumber
    if next==0:
        print("结果为:%f"%(end)) 
    while next==1:
        third=float(input("请输入下一个数"))
        end=end+third
        next=int(input("继续输入请按1\n否请按0"))
        
    print("结果为:%f"%(end))

zhangqinghanbmi()