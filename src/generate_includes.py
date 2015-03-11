#!/usr/bin/env jython

from uk.ac.ebi.brain.core import Brain
import json

gorel = Brain()
gorel.learn("http://purl.obolibrary.org/obo/go/extensions/gorel.owl")

# Declaring AE rels as list for now.
relations = [ "GOREL_0001006" ]
# Would be better to pull list of AE rels automatically from file.
#With current structure, thus would require pulling subproperties.  Can't do that with Brain.

# Iterate over list, pulling usage and saving to file named for relation:

for r in relations:
    label = gorel.getLabel(r)
    usage = gorel.getAnnotation(r, "usage")
    usage_md = open(label + "_usage.md", "w")
    usage_md.write(usage)
    usage_md.close()

gorel.sleep()


