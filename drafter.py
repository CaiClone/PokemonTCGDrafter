import eel
from pokemontcgsdk import Card,Set
import numpy as np
eel.init('web')

#probs pokemon,trainer,energy
probs= [("Pokemon",0.35),("Trainer",0.5),("Energy",0.15)]
#rarities = [("Common",0.4),("Uncommon",0.20),("Rare",0.15),("Rare Ultra",0.1)]


team = []
options = []
chosenSets =[]
NOPTIONS=3
def getTeam():
    teamNames,teamImages,count = zip(*[((str(c.count)+" "+c.name+" "+c.id),c.image_url_hi_res,c.count) for c in team])
    return [teamNames,teamImages,sum(count)]

@eel.expose
def selectOption(opt):
    sel = options[int(opt)]
    try:
        pos = [t.id for t in team].index(sel.id)
        team[pos].count+=1
    except ValueError:
        sel.count=1
        team.append(sel)
    eel.updateTeam(getTeam())
    return getOptions()

@eel.expose
def getOptions():
    global options
    global chosenSets
    global probs
    recalc=0
    while(recalc<20):
        cset = np.random.choice(chosenSets,1)
        ctype = np.random.choice([p[0] for p in probs],p=[p[1] for p in probs])
        try:
            options = np.random.choice(Card.where(set=cset[0], supertype=ctype),NOPTIONS,replace=False)
            recalc+=100
        except ValueError:
            recalc+=1
    return [card.image_url_hi_res for card in options]

@eel.expose
def getSets():
    sets= [(s.name,s.symbol_url) for s in Set.all()]
    return sets
@eel.expose
def setSets(sets):
    global chosenSets
    chosenSets = sets
    copt= getOptions()
    return copt
eel.start('index.html', options ={'chromeFlags':["--start-fullscreen"]})