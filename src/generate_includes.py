#!/usr/bin/env jython

from uk.ac.ebi.brain.core import Brain
import json

gorel = Brain()
gorel.learn("http://purl.obolibrary.org/obo/go/extensions/gorel.owl")

# Load json file containined name:ID dict of (or use YAML?) AEs

# Iterate over list, pulling usage,

ID = "GOREL_1234567"
usage = ""

usage = gorel.getAnnotation(ID, usage)

usage_md = open(usage + ".md", "w") 


