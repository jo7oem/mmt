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

    def twittDo(self):
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

    def __init__(self, text1, text2):
        self.matchlist = text1
        self.outl = text2
        self.pattern = re.compile(self.matchlist)

    def getResult(self):
        return self.result

    def compDo(self):
        self.result = self.pattern.sub(self.outl, self.source)
        return self.result

    def SetComp(self, text):
        self.matchlist = text
        self.pattern = re.compile(self.matchlist)

    def SetOutl(self, text):
        self.outl = text

    def SetSource(self, text):
        self.source = text
