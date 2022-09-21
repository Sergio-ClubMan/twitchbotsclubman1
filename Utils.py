import Config
import urllib2
import json
import time
import thread
from time import sleep


def mess(sock, message):
    sock.send("PRIVMSG #{} :{}\r\n".format(Config.CHAN,message))


def ban(sock, user):
    mess(sock, ".ban {}".format(user))


def timeout(sock, user, seconds=500):
    mess(sock, ".timeout {}".format(user,seconds))


#http://tmi.twitch.tv/group/user/sergio_clubman/chatters
#req = request
#res = response
def fill0plist():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/sergio_clubman/chatters"
            req = urllib2.Request(url, headers={"accept": "*/*"})
            res = urllib2.urlopen(req).read()
            if res.find("502 bad gateway") == - 1:
                Config.oplist.clear()
                data = json.loads(res)
                for p in data ["chatters"]["moderators"]:
                    Config.oplist[p] = "mod"
                for p in data["chatters"]["global_mods"]:
                     Config.oplist[p] = "global_mod"
                for p in data["chatters"]["admins"]:
                    Config.oplist[p] = "admin"
                for p in data["chatters"]["staff"]:
                    Config.oplist[p] = "staff"
        except: "Something wrong... do nothing"
        sleep(5)

        def is0p(user):
            return user in Config.oplist