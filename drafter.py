import eel
from pokemontcgsdk import Card
import numpy as np
eel.init('web')

team = []
options = []
NOPTIONS=3
def getTeamNames():
    print([card.name for card in team])
    print([card.set for card in team])
    print([card.set_code for card in team])
    print([card.number for card in team])
    print([card.id for card in team])
    return [card.name for card in team]

@eel.expose
def selectOption(opt):
    team.append(options[int(opt)])
    eel.updateTeam(getTeamNames())
    return getOptions()

@eel.expose
def getOptions():
    global options
    options = np.random.choice(Card.where(set='generations', supertype='pokemon'),NOPTIONS,replace=False)
    return [card.image_url_hi_res for card in options]

eel.start('index.html', options ={'chromeFlags':["--start-fullscreen"]})