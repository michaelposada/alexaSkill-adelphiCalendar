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
lastDay = " Last Day of "
lastSemester = ""
lastDayTwo = " Term                                "
l = True
while t == True:
    new_dict = {}
    try:
        semestar = tree.xpath('//td//h3["fall 2019"]/text()')[i]
        print(semestar)
        while l == True:
            for counter2 in nameEvent:
                dataOfEvent = tree.xpath('//tr//td//strong["fall 2019"]/text()')[j]
                x = nameEvent.index(counter2)
                str = nameEvent[x]
                test = lastDay + semestar[i] + lastDayTwo

                if str.startswith(lastDay):
                    l = False
                    counter = counter2

                    app_json = json.dumps(new_dict)
                    with open(semestar + ".json", "w") as outfile:
                        json.dump(app_json, outfile)

                    break
                else:
                    print("Data goes here " + dataOfEvent)
                    new_dict[dataOfEvent] = str
                    j = j + 1
                    l = False
        i = i + 1
        l= True
    except IndexError:
        t = False

