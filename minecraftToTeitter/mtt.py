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
        return self.req.status_code

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

    def compDo(self):

        ma = self.infoPa.match(self.source)
        if ma:
            msay = self.infoPallsay.match(self.source)
            if msay:
                result = self.infoPallsay.sub(
                    r"\2: \3", self.source)
                return result
            for i, j in zip(self.patternl, self.outl):
                pattern = i.match(self.source)
                if pattern:
                    result = i.sub(j, self.source)
                    return result

        return False

    def SetComp(self):
        [self.patternl.append(re.compile(i)) for i in self.patternls]

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
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)has just earned the achievement (\[.+])", r"\2は\3の実績を達成した\n\1")

    def SetDeathMes(self):
        #self.addPattern(r"(\[..:..:..]) \[Server thread/INFO]: (.+)",r"\1は")

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)got finished off by(.+)using(.+)", r"\2は\3の\4でとどめを刺された\n\1")  # 他殺1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was slain by(.+)using(.+)", r"\2は\3の\4で殺害された\n\1")  # 他殺2
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)shot by(.+)using(.+)", r"\2は\3の\4で射抜かれた\n\1")  # 他殺3

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was fireballed by(.+)", r"\2は\3に火だるまにされた\n\1")  # 他殺4
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was killed by(.+)using magic", r"\2は魔法を使う\3に殺された\n\1")  # 他殺5
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was slain by(.+)", r"\2は\3に殺害された\n\1")  # 他殺6
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was shot by(.+)", r"\2は\3に射抜かれた\n\1")  # 他殺7
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was killed by magic", r"\2は魔法で殺された\n\1")  # 他殺8

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was squashed by a falling anvil", r"\2は落下してきた金床に押しつぶされた\n\1")  # 金床

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was pricked to death", r"\2は刺されて死んでしまった\n\1")  # サボテン1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)walked into a cactus whilst trying to escape(.+)", r"\2は\3から逃げようとしてサボテンにぶつかってしまった\n\1")  # サボテン2

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was shot by arrow", r"\2は矢に射抜かれた\n\1")  # ディスペンサー

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)drowned whilst trying to escape(.+)", r"\2は\3から逃れようとして溺れ死んでしまった\n\1")  # 溺死1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)drowned", r"\2は溺れ死んでしまった\n\1")  # 溺死2

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was blown up by(.+)", r"\2は\3に爆破されてしまった\n\1")  # 爆発1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)blew up", r"\2は爆発に巻き込まれてしまった\n\1")  # 爆発2

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)hit the ground too hard", r"\2は地面と強く激突してしまった\n\1")  # 落下1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell from a high place", r"\2は高い所から落ちた\n\1")  # 落下2
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell off a ladder", r"\2ははしごから落ちた\n\1")  # 落下3
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell off some vines", r"\2はツタから滑り落ちた\n\1")  # 落下4
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell out of the water", r"\2は水から落ちた\n\1")  # 落下5
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell into a patch of fire", r"\2は火の海に落ちた\n\1")  # 落下6
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell into a patch of cacti", r"\2はサボテンの上に落ちた\n\1")  # 落下7
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was doomed to fall by(.+)", r"\2は\3によって命が尽きて落下した\n\1")  # 落下8
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was doomed to fall", r"\2は命が尽きて落下した\n\1")  # 落下9
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was shot off some vines by(.+)", r"\2は\3によってツタから撃ちだされた\n\1")  # 落下10
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was shot off a ladder by(.+)", r"\2は\3によってはしごから撃ちだされた\n\1")  # 落下11
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was blown from a high place by(.+)", r"\2は\3によって空中へ吹き飛ばされた\n\1")  # 落下12

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)went up in flames", r"\2は炎に巻かれてしまった\n\1")  # 火1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)walked into a fire whilst fighting(.+)", r"\2は\3と戦いながら火の中へ踏み入れてしまった\n\1")  # 火2
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)burned to death", r"\2はこんがりと焼けてしまった\n\1")  # 火3
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was burnt to a crisp whilst fighting(.+)", r"\2は\3と戦いながらカリカリに焼けてしまった\n\1")  # 火4

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)tried to swim in lava while trying to escape(.+)", r"\2は\3から逃れようと溶岩遊泳を試みた\n\1")  # lava1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)tried to swim in lava", r"\2は溶岩遊泳を試みた\n\1")  # lava2

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)died", r"\2は死んでしまった\n\1")  # etc1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was squashed by a falling block", r"\2は落下してきたブロックに押しつぶされた\n\1")  # etc2

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)starved to death", r"\2は飢え死にしてしまった\n\1")  # 餓死

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)suffocated in a wall", r"\2は壁の中で窒息してしまった\n*かべのなかにいる*\n\1")  # 窒息

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was killed while trying to hurt(.+)", r"\2は\3を傷つけようとして殺されました。\n\1")  # エンチャント

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was pummeled by(.+)", r"\2は\3によってぺしゃんこにされた\n\1")  # nouse?

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell out of the world", r"\2は奈落の底へ落ちてしまった\n\1")  # void1
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)fell from a high place and fell out of the world", r"\2は高いところから落ちてそのまま奈落へと落ちていった\n\1")  # void2
        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)was knocked into the void by(.+)", r"\2は\3によって奈落へと突き落とされた\n\1")  # void3

        self.addPattern(
            r"(\[..:..:..]) \[Server thread/INFO]: (.+)withered away", r"\2は枯れ果ててしまった\n\1")  # ウィザー
