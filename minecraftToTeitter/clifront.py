'''
Created on 2016/08/02

@author: su-2
'''
import mtt
matchl = mtt.encLog()
while True:
    try:
        inputtext = input()
    except EOFError:
        break
    matchl.SetSource(inputtext)
    result = matchl.compDo()
    if result:
        print(result)
