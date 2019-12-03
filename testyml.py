from jnpr.junos import Device
from pprint import pprint
import json
import yamlordereddictloader
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml
import sys


yfile = sys.argv[1]
#print (yfile)
f = open(yfile, 'r')
yd = f.readlines()
for word in yd:
   x = word.find("Table")
   if (x != -1):
      tbl = word.split(":")
      print("tbl = " ,tbl[0])
      break

yaml_data = "".join(yd)
f.close()

dev = Device(host="X.X.X.X", user="X", passwd="X")
dev.open()

globals().update(FactoryLoader().load(yaml.load(yaml_data, Loader=yamlordereddictloader.Loader)))
possibles = globals().copy()
possibles.update(locals())
method = possibles.get(tbl[0])
stats = method(dev)

stats = stats.get()
#print(stats)
pprint(stats)
pprint(json.loads(stats.to_json()))
