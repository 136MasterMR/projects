# -*- coding: cp1253 -*-
L=[]
string=raw_input("Give a string: ")
while string!="end":
    num=len(string) 
    L.append(num)
    s=sum(L)
    string=raw_input("Give a string: ")
print "The total sum of the strings is ",s
