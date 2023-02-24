import os
from datetime import datetime
import webbrowser
import requests
import json

# basic variables, sets the days of the week and the current day
weekDays = [1, 2, 3, 4, 5]
weekEnds = [6, 7]
today = datetime.now().isoweekday()
hour = datetime.now().hour
os.system('cls')

# programs paths, you can add more if you want
discord = ['C:/Users/gabri/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord.lnk', "Discord"]
vscode = [
    'C:/Users/gabri/AppData/Local/Programs/Microsoft VS Code/bin/code.cmd', "VS Code"]
slack = ['C:/Users/gabri/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Slack Technologies Inc/Slack.lnk', "Slack"]
steam = ['C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Steam/Steam.lnk', "Steam"]
spotify = [
    'C:/Users/gabri/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify.lnk', "Spotify"]


# web browser paths, you can add more if you want
clockify = ['https://app.clockify.me/tracker', "Clockify"]
jira = ['https://tiimsrevolution.atlassian.net/jira/your-work', "Jira"]
github = ['https://github.com/Tiims-Revolution', "Github"]
gmail = ['https://mail.google.com/mail/u/0/#inbox', "Gmail"]
facebook = ['https://www.facebook.com/?_rdr=p', "Facebook"]
whatsapp = ['https://web.whatsapp.com/', "Whatsapp"]
youtube = ['https://www.youtube.com/', "Youtube"]


# Arrays with the links and programs associated with
workLinks = [clockify, jira, github, gmail]
workProgramsPaths = [slack, discord, vscode, spotify]

gamesLinks = [youtube, facebook, whatsapp, gmail]
gamesProgramsPaths = [steam, discord, spotify]

# Functions


def getQuote():
    response = requests.get("https://zenquotes.io/api/today")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote


def openChromeTabs(links):
    for link in links:
        try:
            webbrowser.open(link[0])

        except:
            print('\033[91m' + '[Error] Could not open: ' +
                  '\033[96m'+link[1] + '\033[0m')

        finally:
            print('\033[94m' + '[Info] Opening: ' +
                  '\033[96m' + link[1] + '\033[0m')


def openVariousPrograms(programsPaths):
    for path in programsPaths:
        try:
            os.startfile(path[0])

        except:
            print('\033[91m' + '[Error] Could not open: ' +
                  '\033[96m'+path[1] + '\033[0m')

        finally:
            print('\033[94m' + '[Info] Opening: ' +
                  '\033[96m'+path[1] + '\033[0m')


lineBreak = '\033[95m' + '\n' + \
    '--------------------------------------------------------------------------------' + \
    '\n' + '\033[0m'

try:
    # Checks the day of the week and opens the links and programs
    if today in weekDays and hour < 14:
        print('\033[94m' + '[Info] Opening your work stuff...' + '\033[0m')
        print(lineBreak)
        openChromeTabs(workLinks)
        openVariousPrograms(workProgramsPaths)

    elif today in weekEnds:
        print('\033[94m' + '[Info] Opening your games stuff...' + '\033[0m')
        print(lineBreak)
        openChromeTabs(gamesLinks)
        openVariousPrograms(gamesProgramsPaths)

    elif today in weekDays and hour >= 14:
        print('\033[94m' + '[Info] Opening your games stuff...' + '\033[0m')
        print(lineBreak)
        openChromeTabs(gamesLinks)
        openVariousPrograms(gamesProgramsPaths)

    else:
        print('\033[91m' + '[Error] Could not open anything' + '\033[0m')

except:
    print('\033[91m' + '[Error] Could not open anything' + '\033[0m')

print(lineBreak)
print('\033[93m' + '[Quote] ' + getQuote() + '\n'+'\033[0m')
print('\033[92m' + '[Message] Enjoy your day!' + '\033[0m')
print(lineBreak)
input('\033[96m' + 'Press ENTER to exit...' + '\033[0m')
