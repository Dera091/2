from os import path
import string
with open('tekst.txt', 'r') as tekst:
    a = tekst.read()
    wyraz = len(a.split())
    wyraz1 = (a.split())
    
    print(wyraz)
    stat = {}
    for i in wyraz1:
      i = i.strip(string.punctuation + string.whitespace)
      c = i[-1]  
      
      if c in stat:
        stat[c] += 1
      else:
        stat[c] = 1
    
    for i1, i2 in stat.items():
        print(i1, i2)