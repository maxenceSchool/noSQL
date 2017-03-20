#!/usr/bin/env python

#Gestion des imports
import json
import requests
import pymongo
from xml.dom import minidom
## Initialisation

client = pymongo.MongoClient()
db = client.mydb
health = db.health
art = db.art
subway = db.sub
home = db.home
inter = db.inter

# On telecharge les bases de donnees

dataH = requests.get("https://data.cityofnewyork.us/resource/ymhw-9cz9.json").json()
dataA = requests.get("https://data.cityofnewyork.us/resource/43hw-uvdj.json").json()
dataS = requests.get("https://data.cityofnewyork.us/resource/kk4q-3rt2.json").json()






#On insere les donnees sur les centres hospitalies de type  
# {  "location_1" : {
#    "latitude" : "40.73962320748018",
#    "human_address" : "{\"address\":\"462 First Avenue\",\"city\":\"New York\",\"state\":\"NY\",\"zi\":\"10016\"}",
#    "needs_recoding" : false,
#    "longitude" : "-73.97657284664467"
#  },
#  "phone" : "212-562-4141",
#  "facility_type" : "Acute Care Hospital",
#  "borough" : "Manhattan",
#  "facility_name" : "Bellevue Hospital Center"
# }  On conserve le nom les coordonnees et e type d etablissement.

for c in dataH:
    health.insert_one({'name' : c['facility_name'], 'latitude' : c['location_1']['latitude'], 'longitude': c['location_1']['longitude'], 'type' : c['facility_type'], })


# on insere les donnees sur les galleries d'art de type : {"address1":"52 E 76th St","address2":"","city":"New York","name":"O'reilly William & Co Ltd","tel":"(212) 396-1822","the_geom":{"type":"Point","coordinates":[-73.96273074561996,40.773800871637576]},"url":"http://www.nyc.com/arts__attractions/oreilly_william__co_ltd.806/whats_nearby.aspx","zip":"10021.0"} on conserve le nom et les coordonnees.

for c in dataA:
    art.insert_one({'name' : c['name'], 'latitude' : c['the_geom']['coordinates'][1], 'longitude': c['the_geom']['coordinates'][0] })


# On insere les donnees du metro du type {"line":"4-6-6 Express","name":"Astor Pl","notes":"4 nights, 6-all times, 6 Express-weekdays AM southbound, PM northbound","objectid":"1","the_geom":{"type":"Point","coordinates":[-73.99106999861966,40.73005400028978]},"url":"http://web.mta.info/nyct/service/"} on conserve le nom de l'arret la ligne et les coordonnees.

for c in dataS:
    subway.insert_one({'name' : c['name'], 'latitude' : c['the_geom']['coordinates'][1], 'longitude': c['the_geom']['coordinates'][0],'line' : c['line'] })

# On ajoute les coordonnees des maisons et appartements qui nous interessere,t.

dataH = [{"name": "maison1", 
"latitude": 40.5,
"longitude": -73.9},
{"name": "maison2", 
"latitude": 40.6,
"longitude": -73.9},
{"name": "maison3", 
"latitude": 40.7,
"longitude": -73.9},
{"name": "maison4", 
"latitude": 40.8,
"longitude": -73.9},
{"name": "maison5", 
"latitude": 40.5,
"longitude": -74},
{"name": "maison6", 
"latitude": 40.6,
"longitude": -74},
{"name": "maison7", 
"latitude": 40.7,
"longitude": -74},
{"name": "maison8", 
"latitude": 40.8,
"longitude": -74},
{"name": "maison9", 
"latitude": 40.5,
"longitude": -74.1},
{"name": "maison10", 
"latitude": 40.6,
"longitude": -74.1},
{"name": "maison11", 
"latitude": 40.7,
"longitude": -74.1},
{"name": "maison12", 
"latitude": 40.8,
"longitude": -74.1},
]
 
home.insert_many(dataH)




	

