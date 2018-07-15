from pokemontcgsdk import Set
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



tree = et.ElementTree(root)
tree.write("pokemon.xml", pretty_print=True,xml_declaration=True,encoding='utf-8')