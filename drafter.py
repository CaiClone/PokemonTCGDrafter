import eel
from pokemontcgsdk import Card,Set
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
        team[pos].count+=1
    except ValueError:
        sel.count=1
        team.append(sel)
    eel.updateTeam(getTeamNames())
    return getOptions()

@eel.expose
def getOptions():
    global options
    options = np.random.choice(Card.where(setCode='sm6', supertype='pokemon'),NOPTIONS,replace=False)
    return [card.image_url_hi_res for card in options]

@eel.expose
def getSets():
    sets= [(s.code,s.name,s.symbol_url) for s in Set.all()]
    return sets

eel.start('index.html')#, options ={'chromeFlags':["--start-fullscreen"]})