import eel
from pokemontcgsdk import Card
import numpy as np
eel.init('web')

team = []
options = []
NOPTIONS=3
def getTeamNames():
    return [str(c.count)+" "+c.name+" "+c.id for c in team]

@eel.expose
def selectOption(opt):
    sel = options[int(opt)]
    try:
        pos = [t.id for t in team].index(sel.id)
        print(pos)
        team[pos].count+=1
    except ValueError:
        sel.count=1
        team.append(sel)
    eel.updateTeam(getTeamNames())
    return getOptions()

@eel.expose
def getOptions():
    global options
    options = np.random.choice(Card.where(set='generations', supertype='pokemon'),NOPTIONS,replace=False)
    return [card.image_url_hi_res for card in options]

eel.start('index.html', options ={'chromeFlags':["--start-fullscreen"]})