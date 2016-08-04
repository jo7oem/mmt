'''
Created on 2016/08/02

@author: su-2
'''
import mtt
intext = "[23:53:52] [Server thread/INFO]: jo7oem joined the game"
matchl = mtt.encLog()
matchl.SetSource(intext)
print(matchl.compDo())
