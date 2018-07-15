import eel
from pokemontcgsdk import Card
import numpy as np
eel.init('web')

team = []
options = []
NOPTIONS=3

@eel.expose
def selectOption(opt):
    team.append(opt)
    eel.updateTeam(team)
    return getOptions()

@eel.expose
def getOptions():
    options = Card.where(set='generations', supertype='pokemon')
    return [card.image_url_hi_res for card in np.random.choice(options,NOPTIONS,replace=False)]
    #return ["https://images.pokemontcg.io/g1/RC2.png","https://images.pokemontcg.io/g1/23.png","https://images.pokemontcg.io/g1/45.png"] 

eel.start('index.html', options ={'chromeFlags':["--start-fullscreen"]})