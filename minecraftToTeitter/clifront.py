'''
Created on 2016/08/02

@author: su-2
'''
import mtt
patten = "X(.)X"
olist = r"C\1C"
intext = 'AAGCAGTXCXGAGCAGXTXAGXTXA'
matchl = mtt.encLog(patten, olist)
matchl.SetSource(intext)
print(matchl.compDo())
