'''
Created on 2016/08/02

@author: su-2
'''
import os
import mtt
import configparser
import sys


class mlogtot():

    def __init__(self):
        self.CONFIGPATH = "./mmt.conf"
        if os.path.exists(self.CONFIGPATH):
            self.configRead()
        else:
            self.CreatConfig()
        self.main()

    def main(self):
        tweet = mtt.tweetOAuth(self.CK, self.CS, self.AT, self.AS)
        tweet.SetFooter(self.footer)
        tweet.SetHeader(self.header)
        matchl = mtt.encLog()
        while True:
            try:
                inputtext = input()
            except EOFError:
                break
            matchl.SetSource(inputtext)
            result = matchl.compDo()
            if result:
                if self.NOTWEET:
                    print(result)
                else:
                    tweet.SetPayload(result)
                    tweet.tweetDo()

    def configRead(self):
        config = configparser.ConfigParser()
        config.read(self.CONFIGPATH)
        self.CK = config["API Key"]["ck"]
        self.CS = config["API Key"]["cs"]
        self.AT = config["Access Token"]["at"]
        self.AT = config["Access Token"]["as"]
        self.header = config["Tweet Config"]["header"]
        self.footer = config["Tweet Config"]["footer"]
        self.NOTWEET = config["DEBUG"].getboolean("notweet")
        print(self.header)

    def CreatConfig(self):
        config = configparser.ConfigParser()
        config["API Key"] = {
            "ck": "Consumer Key (API Key)", "cs": "Consumer Secret (API Secret)"}
        config["Access Token"] = {
            "at": "Access Token", "as": "Access Token Secret"}
        config["Tweet Config"] = {"header": "H", "footer": ""}
        config["DEBUG"] = {"notweet": "True"}
        with open(self.CONFIGPATH, 'w') as configfile:
            config.write(configfile)
        print("No Config")
        sys.exit()
mlogtot()
