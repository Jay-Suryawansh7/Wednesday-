from aivoice import *
import os
import commands
import datetime


def run():
    commands.greatings()
    while True:
        os.system("clear")
        query = wednesday_listen()

        if "wikipedia" in query:
            wednesday_speak("Searching on wikipedia")
            commands.ar_wiki(query)

        elif "google" in query:
            commands.goosearch(query)

        elif "youtube" in query:
            commands.youtube(query)

        elif "open" in query or "launch" in query or "start" in query:
            commands.open_app(query)

        elif "sing" in query or "song" in query:
            commands.sing_a_song()

        elif "time" in query and "what" in query:
            commands.tell_time()

        elif "date" in query or "day" in query:
            commands.tell_date()

        elif "joke" in query:
            commands.tell_joke()

        elif "system" in query and ("report" in query or "info" in query):
            commands.system_report()

        elif "note" in query or "write" in query or "remember" in query:
            commands.take_note()

        elif "flip" in query and "coin" in query:
            commands.flip_coin()

        elif "fine" in query:
            wednesday_speak("Good to hear Jay!")

        elif "goodbye" in query or "good by" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 20:
                wednesday_speak("As you wish Jay! But may I know your next plan?")
                tik = wednesday_listen()
                if "sleep" in tik:
                    wednesday_speak("Alright then")
                    wednesday_speak("Well, good night Jay. Rest well and dream big!")
                    tik = wednesday_listen()
                    if "shut up" in tik or "shutup" in tik:
                        wednesday_speak("Haha, alright alright, good night Jay!")
                        tik = wednesday_listen()
                        if "hmm hmm" in tik or "that's true" in tik or "ok" in tik:
                            wednesday_speak("Sleep well Jay, see you tomorrow. Bye bye!")
                else:
                    wednesday_speak("Well, wish you good luck with your next work Jay!")
                    tik = wednesday_listen()
                    if "thanks" in tik or "thank you" in tik:
                        wednesday_speak("You're welcome Jay, see you soon. Bye bye!")
            else:
                wednesday_speak("As you wish Jay! See you again, bye bye!")
                os.system(exit(1))


if __name__ == "__main__":
    run()
