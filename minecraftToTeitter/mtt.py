#!/usr/bin/python3
"""
minecraft twitter 連携tools
"""
from requests_oauthlib import OAuth1Session
import re


class tweetOAuth():

    def __init__(self, CK, CS, AT, AS):
        self.CK = CK
        self.CS = CS
        self.AT = AT
        self.AS = AS
        self.header = ""
        self.payload = ""
        self.footer = ""

    def tweetDo(self):
        self.url = "https://api.twitter.com/1.1/statuses/update.json"
        self.params = {
            "status": self.header + "\n" + self.payload + "\n" + self.footer}
        self.twitter = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        self.req = self.twitter.post(self.url, params=self.params)
        return self.req

    def SetHeader(self, text):
        self.header = text

    def SetPayload(self, text):
        self.payload = text

    def SetFooter(self, text):
        self.footer = text

    def SetText(self, head, payload, footer):
        self.header = head
        self.payload = payload
        self.footer = footer


class encLog():

    def __init__(self):
        self.patternl = list()
        self.patternls = list()
        self.outl = list()
        self.SetPatternSource()
        self.infoPa = re.compile(r"(\[..:..:..]) \[Server thread/INFO]:")
        self.infoPallsay = re.compile(
            r"(\[..:..:..]) \[Server thread/INFO]: \<(.+)\>\s+@all@(.+)")

    def getResult(self):
        return self.result

    def compDo(self):

        self.ma = self.infoPa.match(self.source)
        if self.ma:
            self.msay = self.infoPallsay.match(self.source)
            if self.msay:
                self.result = self.infoPallsay.sub(
                    r"\3\n\2 より \1", self.source)
                return self.result
            for i, j in zip(self.patternl, self.outl):
                self.pattern = i.match(self.source)
                if self.pattern:
                    self.result = i.sub(j, self.source)
                    return self.result

        return False

    def SetComp(self):
        for i in self.patternls:
            self.patternl.append(re.compile(i))

    def SetSource(self, text):
        self.source = text

    def SetPatternSource(self):
        self.SetLoginout()

        self.SetComp()

    def SetLoginout(self):
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)joined the game", r"\2は \1 からゲームに参加した")
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)left the game", r"\2は \1 にゲームから退場した")

    def addPattern(self, befor, after):
        self.patternls.append(befor)
        self.outl.append(after)


#patten = r"(\[..:..:..]) \[Server thread/INFO]: (.+)joined the game"
#olist = r"\2は \1 からゲームに参加した"
