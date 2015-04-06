"""
dependencias: 
    sudo pip install dopy pyopenssl ndg-httpsclient pyasn1
"""

import os
from dopy.manager import DoManager
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


cliend_id = os.getenv("DO_CLIENT_ID")
api_key=os.getenv("DO_API_KEY")

do = DoManager(cliend_id, api_key)

keys = do.all_ssh_keys()
print "Nome da chave ssh\tid"
for key in keys:
    print "%s\t%d" % (key["name"], key["id"])

print "Nome da imagem\tid"
imgs = do.all_images()
for img in imgs:
    if img["slug"] == "ubuntu-14-04-x64":
        print "%s\t%d" % (img["name"], img["id"])

print "Nome da regiao\tid"
regions = do.all_regions()
for region in regions:
    if region["slug"] == "nyc2":
        print "%s\t%d" % (region["slug"], region["id"])
        
print "Nome do tamanho\tid"
sizes = do.sizes()
for size in sizes:
    if size["slug"] == "512mb":
        print "%s\t%d" % (size["slug"], size["id"])

