from pokemontcgsdk import Set,Card
from lxml import etree as et

root = et.Element('cockatrice_carddatabase')
root.attrib["version"]="3"
xmlsets = et.SubElement(root, "sets")
xmlcards = et.SubElement(root, "cards")
#Save sets
for s in Set.all():
    nset = et.SubElement(xmlsets,"set")

    name = et.SubElement(nset,"name")
    longname = et.SubElement(nset,"longname")
    setType = et.SubElement(nset,"setType")
    releasedate = et.SubElement(nset,"releasedate")

    name.text=s.code
    longname.text = s.name
    setType.text = s.series
    releasedate.text = s.release_date

names = []
n=0
for c in Card.all():
    n+=1
    ncard = et.SubElement(xmlcards,"card")

    name = et.SubElement(ncard,"name")
    cset= et.SubElement(ncard,"set")
    color = et.SubElement(ncard,"color")
    mana = et.SubElement(ncard,"manacost")
    cmc = et.SubElement(ncard,"cmc")
    ctype = et.SubElement(ncard,"type")
    pt = et.SubElement(ncard,"pt")
    tablerow = et.SubElement(ncard,"tablerow")
    text = et.SubElement(ncard,"text")
    font = et.SubElement(ncard,"font")
    
    name.text = c.name +" "+ c.id
    cset.text = c.set_code
    cset.set('picURL',c.image_url_hi_res)
    if(c.types!=None):
        color.text = " ".join(c.types)
    ctype.text = c.supertype +" - "+c.subtype
    if(c.hp!=None and c.hp!="None"):
        pt.text="0/"+str(int(int(c.hp)/10))
    tablerow.text = "0"

print(n)


tree = et.ElementTree(root)
tree.write("pokemon.xml", pretty_print=True,xml_declaration=True,encoding='utf-8')