#from owl2pdm_tools import ont_manager
#from owltools.graph import OWLGraphWrapper
from uk.ac.ebi.brain.core import Brain
#from tsv2pdm import tab
import warnings
#import re
import json

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

class om():
    
    def __init__(self, uri_or_fp):
       self.b = Brain()
       self.b.learn(uri_or_fp)
       self.o = self.b.getOntology()
       self.bsfp = self.b.getBidiShortFormProvider() # uses .getEntity(<string> shortForm), .getShortForm(OWLEntity entity)

    def get_OP_list(self):
        s = self.o.getObjectPropertiesInSignature()
        out = []
        for r in s:
            out.append(self.bsfp.getShortForm(r))
        return out
        
    def roll_pdm(self, id_name):
        # TODO - get subsets + regular domain and range
        out = {}
        relations = self.get_OP_list()
        local_domains = []
        local_ranges = []
        for r in relations:
            #Assumes everything in file has a shorthand! # Better to key primary model on shortFormID and then re-key after reading.
            shorthand = self.b.getAnnotation(r, "shorthand")
            out[shorthand] = {}
            out[shorthand]['label'] = self.b.getLabel(r)
            try:
                out[shorthand]['usage'] = self.b.getAnnotation(r, "usage")
                out[shorthand]['defn'] = self.b.getAnnotation(r, "IAO_0000115")
                local_domains = self.b.getAnnotation(r, "local_domain").split(" ")
                local_ranges = self.b.getAnnotation(r, "local_range").split(" ")
            except:
                pass
            if local_domains:
                ldd = {}
                for ld in local_domains:
                    if ld in id_name.keys():
                        ldd[ld] = id_name[ld]
                    else:
                        ldd[ld] = ''
                out[shorthand]['local_domain'] = str(ldd)
            if local_ranges:
                lrd = {}           
                for lr in local_ranges:
                    if lr in id_name.keys():
                        lrd[lr] = id_name[lr]
                    else:
                        lrd[lr] = ''
                out[shorthand]['local_range'] = str(lrd)
        return out
        
gorel = om(uri_or_fp = 'http://purl.obolibrary.org/obo/go/extensions/gorel.owl')
id_name = load_json("../data/id_name.json") # load from json
pdm = gorel.roll_pdm(id_name)
write_json(pdm, "../data/gorel.json")



              