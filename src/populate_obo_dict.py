#!/usr/bin/env python

import osa
import re
import json
import warnings

def get_name(ID, ols):
    m = re.match('(\w+):\d+', ID)
    if m:    
        oName = m.group(1)
        return ols.service.getTermById(termId=ID, ontologyName=oName)
    else:
        warnings.warn("ID %s, doesn't look like an OBO ID. Not looking up."  % ID)

def load_json(path):
    json_file = open(path, "r")
    json_string = json_file.read()
    json_file.close()
    return json.loads(json_string)


def write_json(json_var, path):
    """Writes json_var to file (path) with a nicely serialised layout."""
    json_file = open(path, "w")
    json_file.write(json.dumps(json_var ,sort_keys=True, indent=4, separators=(',', ': ')))
    json_file.close()

ols = osa.Client("http://www.ebi.ac.uk/ontology-lookup/OntologyQuery.wsdl")

id_name = load_json("../data/id_name.json")
ids = id_name.keys()

for i in ids:
    name = get_name(i, ols)
    if not name == i:
        id_name[i] = name
    
write_json(json_var= id_name, path = "../data/id_name.json")    