##This gets the html code from the site
##now i have to see how to paser the data
from lxml import html
import urllib
import requests
import json

url = "https://registrar.adelphi.edu/academic-calendar/"

req = requests.get(url)
tree = html.fromstring(req.content)

nameEvent = tree.xpath('//tr//td["fall 2019"]/text()')
t = True


for i in nameEvent:
    try:
        x = nameEvent.index(i)
        str = nameEvent[x]
        str = str.replace('\n\t\t\t\t', '')
        nameEvent[x] = str
        try:
            nameEvent.remove('')
            try:
                x = nameEvent.index(i)
                str = nameEvent[x]
                str = str.replace('\n\t\t\t', '')
                nameEvent[x] = str
            except ValueError:
                pass
        except ValueError:
            pass
    except ValueError:
        pass
for i in nameEvent:
    try:
        x = nameEvent.index(i)
        str = nameEvent[x]
        str = str.replace('\t', '')
        str.strip
        nameEvent[x] = str
        try:
            nameEvent.remove('')
        except ValueError:
            pass
    except ValueError:
        pass

nameOfJsonFile = ""
i = 0 ## number of semestars
j = 0 ## number of events
counter = 0
counter2 = 0
lastDay = " Last Day of "
l = True
while t == True:
    new_dict = {}
    try:
        semestar = tree.xpath('//td//h3["fall 2019"]/text()')[i]
        print(semestar)

        while l == True:
            dataOfEvent = tree.xpath('//tr//td//strong["fall 2019"]/text()')[j]
            x = nameEvent[j]
            str = x
            if(semestar.startswith("Fall") and str.startswith(lastDay)):
                l = False
                new_dict[dataOfEvent] = str
                j = j + 1
                app_json = json.dumps(new_dict,indent=4, separators=(',',':'))
                with open(semestar + ".json", "w") as outfile:
                    json.dump(app_json, outfile)

                break
            elif (semestar.startswith("Spring") and str.startswith(" Commencement")):
                l = False
                new_dict[dataOfEvent] = str
                j = j + 1
                app_json = json.dumps(new_dict)
                with open(semestar + ".json", "w") as outfile:
                    json.dump(app_json, outfile,  indent=4, separators=(',',':'))

                break
            elif (semestar.startswith("Summer") and str.startswith(lastDay)):
                l = False
                new_dict[dataOfEvent] = str
                j = j + 1
                app_json = json.dumps(new_dict)
                with open(semestar + ".json", "w") as outfile:
                    json.dump(app_json, outfile, indent=4, separators=(',',':'))
                break
            else:
                new_dict[dataOfEvent] = str
                j = j + 1
    except IndexError:
        t = False
    i = i + 1
    l = True