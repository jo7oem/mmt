#!/usr/bin/python3
"""
minecraft twitter 連携tools
"""
from requests_oauthlib import OAuth1Session
from docutils.languages import cs


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
