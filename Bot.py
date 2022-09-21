import Config
import Utils
import socket
import re
import time
import thread
from time import sleep
import os




def main():
    s = socket.socket()
    s.connect((Config.HOST, Config.PORT))
    s.send("PASS {}\r\n".format(Config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(Config.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(Config.CHAN).encode("utf-8"))

    chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    Utils.mess(s, "Hello, peoples")

    thread.start_new_thread(Utils.fill0plist,())
    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("POND :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = chat_message.sub("", response)
            print(response)

            if message.strip() == "!time":
                Utils.mess(s, "Stream is alive " +time.strftime("%I:%M %p %Z on %A %B %d %Y"))

            if message.strip() == "loh" or message.strip() == "Loh":
                Utils.mess(s, "A ti chmo")

                if message.strip() == "sosi" or message.strip() == "Sosi":
                    Utils.mess(s, "sam sosi")

            if message.strip() == "!Oru":
                os.system("start C:\For_twitch\Sounds\Oru.mp3")

            if message.strip() == "!Sami" or message.strip() == "!sami":
                os.system("start C:\For_twitch\Sounds\sami.mp3")

            if message.strip() == "!ebanutsa":
                os.system("start C:\For_twitch\Sounds\Ebanutsa.mp3")

            if message.strip() == "!uspokoisa":
                os.system("start C:\For_twitch\Sounds\uspokoisa.mp3")

            if message.strip() == "!nani":
                os.system("start C:\For_twitch\Sounds\Nani.mp3")

            if message.strip() == "!omae":
                os.system("start C:\For_twitch\Sounds\omae.mp3")

            if message.strip() == "!dich":
                os.system("start C:\For_twitch\Sounds\dich.mp3")

            if message.strip() == "!hahaha":
                os.system("start C:\For_twitch\Sounds\hahaha.mp3")

            if message.strip() == "!tlen":
                os.system("start C:\For_twitch\Sounds\Tlen.mp3")

            if message.strip() == "!poshutil":
                os.system("start C:\For_twitch\Sounds\poshutil.mp3")

            if message.strip() == "!pipec":
                os.system("start C:\For_twitch\Sounds\pipec.mp3")

            if message.strip() == "!net":
                os.system("start C:\For_twitch\Sounds\Net.mp3")

            if message.strip() == "!da":
                os.system("start C:\For_twitch\Sounds\da.mp3")

            if message.strip() == "!nepoluchilos":
                os.system("start C:\For_twitch\Sounds\Pacan_K_Uspehu_shel.mp3")

            if message.strip() == "!nebombi":
                os.system("start C:\For_twitch\Sounds\Bombit.mp3")

            if message.strip() == "!lol":
                os.system("start C:\For_twitch\Sounds\lol.mp3")

            if message.strip() == "!tupoi":
                os.system("start C:\For_twitch\Sounds\Tupoi.mp3")

            if message.strip() == "!virubil":
                os.system("start C:\For_twitch\Sounds\Virubil.mp3")

            if message.strip() == "!zdorovo":
                os.system("start C:\For_twitch\Sounds\zdorovo.mp3")

            if message.strip() == "!zatknis":
                os.system("start C:\For_twitch\Sounds\zatknis.mp3")

            if message.strip() == "!ya_tozhe":
                os.system("start C:\For_twitch\Sounds\ya_tozhe.mp3")

            if message.strip() == "!slozhno":
                os.system("start C:\For_twitch\Sounds\slozhno.mp3")

            if message.strip() == "!slish":
                os.system("start C:\For_twitch\Sounds\slish.mp3")

            if message.strip() == "!shumish":
                os.system("start C:\For_twitch\Sounds\shumish.mp3")

            if message.strip() == "!sama_vinovata":
                os.system("start C:\For_twitch\Sounds\sama_vinovata.mp3")

            if message.strip() == "!rasist":
                os.system("start C:\For_twitch\Sounds\Rasist.mp3")

            if message.strip() == "!privet":
                os.system("start C:\For_twitch\Sounds\privet.mp3")

            if message.strip() == "!ne_sudba":
                os.system("start C:\For_twitch\Sounds\Ne_sudba.mp3")

            if message.strip() == "!narkoman":
                os.system("start C:\For_twitch\Sounds\Narkoman.mp3")

            if message.strip() == "!mudak":
                os.system("start C:\For_twitch\Sounds\mudak.mp3")

            if message.strip() == "!molis":
                os.system("start C:\For_twitch\Sounds\molis.mp3")

            if message.strip() == "!mnogo_bukv":
                os.system("start C:\For_twitch\Sounds\mnogo_bukv.mp3")

            if message.strip() == "!hvatit":
                os.system("start C:\For_twitch\Sounds\hvatit.mp3")

            if message.strip() == "!horoshaya_shutka":
                os.system("start C:\For_twitch\Sounds\horoshaya_shutka.mp3")

            if message.strip() == "!ehai_normalno":
                os.system("start C:\For_twitch\Sounds\ehai_normalno.mp3")

            if message.strip() == "!durak":
                os.system("start C:\For_twitch\Sounds\durak.mp3")

            if message.strip() == "!ahuenno":
                os.system("start C:\For_twitch\Sounds\Ahuenno.mp3")

            if message.strip() == "!ahaha":
                os.system("start C:\For_twitch\Sounds\hahaha.mp3")

            if message.strip() == "!vosem_chasov":
                os.system("start C:\For_twitch\Sounds\Vosem_chasov.mp3")

            if message.strip() == "!NeSovpadenie":
                os.system("start C:\For_twitch\Sounds\NeSovpadenie.mp3")

            if message.strip() == "!zhri":
                os.system("start C:\For_twitch\Sounds\zhri.mp3")

            if message.strip() == "!uhodite":
                os.system("start C:\For_twitch\Sounds\uhodite.mp3")

            if message.strip() == "!ebanutsa":
                os.system("start C:\For_twitch\Sounds\ebanutsa.mp3")


                sleep(5)

if __name__ == "__main__": main()