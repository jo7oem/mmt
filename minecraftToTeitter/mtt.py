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
                    r"\2: \3", self.source)
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
        self.SetPerformance()
        self.SetDeathMes()

        self.SetComp()

    def SetLoginout(self):
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)joined the game", r"\2は \1 からゲームに参加した")
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)left the game", r"\2は \1 にゲームから退場した")

    def addPattern(self, befor, after):
        self.patternls.append(befor)
        self.outl.append(after)

    def SetPerformance(self):
        self.addPattern(
            r".+\[Server thread/INFO]: (.+)has just earned the achievement (\[.+])", r"\1は\2の実績を達成した")

    def SetDeathMes(self):
        #self.addPattern(r".+\[Server thread/INFO]: (.+)",r"")
        self.addPattern(
            r".+\[Server thread/INFO]: (.+)was squashed by a falling anvil", r"\1は落下してきた金床に押しつぶされた")  # 金床

        self.addPattern(
            r".+\[Server thread/INFO]: (.+)was pricked to death", r"\1は刺されて死んでしまった")  # サボテン1
        self.addPattern(
            r".+\[Server thread/INFO]: (.+)walked into a cactus whilst trying to escape(.+)", r"\1は\2から逃げようとしてサボテンにぶつかってしまった")  # サボテン2

        self.addPattern(
            r".+\[Server thread/INFO]: (.+)was shot by arrow", r"\1は矢に射抜かれた")  # ディスペンサー

        self.addPattern(
            r".+\[Server thread/INFO]: (.+)drowned whilst trying to escape(.+)", r"\1は\2から逃れようとして溺れ死んでしまった")  # 溺死1
        self.addPattern(
            r".+\[Server thread/INFO]: (.+)drowned", r"\1は溺れ死んでしまった")  # 溺死2

        self.addPattern(
            r".+\[Server thread/INFO]: (.+)was blown up by(.+)", r"\1は\2に爆破されてしまった")  # 爆発1
        self.addPattern(
            r".+\[Server thread/INFO]: (.+)blew up", r"\1は爆発に巻き込まれてしまった")  # 爆発2

        self.addPattern(r".+\[Server thread/INFO]: (.+)", r"")  # 落下1


#patten = r"(\[..:..:..]) \[Server thread/INFO]: (.+)joined the game"
#olist = r"\2は \1 からゲームに参加した"
