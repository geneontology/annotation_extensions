#!/usr/bin/env python

import warnings
import simplemediawiki
wiki = simplemediawiki.MediaWiki('http://gocwiki.geneontology.org/api.php?')
import json

def load_json(path):
    json_file = open(path, "r")
    json_string = json_file.read()
    json_file.close()
    return json.loads(json_string)


example_call = {u'query': {u'normalized': [{u'from': u'Api_test', u'to': u'Api test'}],
  u'pages': {u'7820': {u'contentmodel': u'wikitext',
    u'counter': 1,
    u'edittoken': u'ee8c94746e781cf718c3c5b6ac039304+\\',
    u'lastrevid': 57161,
    u'length': 459,
    u'new': u'',
    u'ns': 0,
    u'pageid': 7820,
    u'pagelanguage': u'en',
    u'starttimestamp': u'2015-05-22T11:07:44Z',
    u'title': u'Api test',
    u'touched': u'2015-05-22T11:05:56Z'}}}}


def edit_page(wiki, shorthand, pdm):
    # get an API key to edit: http://www.mediawiki.org/wiki/Manual:Edit_token
    # Do I need to get per page?
    contents = pdm[shorthand]
    token_call = wiki.call({'action': 'query', 'prop' : 
                            'info', 'intoken' : 'edit',
                            'titles' : 'Annotation_Extension_Relation:' + shorthand })  #  pwd from argv
    pages = token_call['query']['pages']
    if not len(pages) == 1:
        warnings.warn("Multiple pages with name '%s'" % shorthand)
    else:
        pv = pages.values()
        token = pv[0]['edittoken']
    auto_text = "== Text extracted from ontlogy: DO NOT EDIT ==\n"
    auto_text += "* shorthand: %s\n" % shorthand
#    auto_text += "* id: %s\n" % contents['']
    auto_text += "* label: %s\n" % contents['label']
    auto_text += "=== Definition ===\n%s" % contents['defn']
    auto_text += "=== Usage ===\n%s" % contents['usage']
#   auto_text += "=== Comment ===\n%s" % contents['']
#   auto_text += "=== subsets ===\n%s" % contents['']
    auto_text += "=== local domain ===\n%s" % contents['local_domain']
    auto_text += "=== local range ===\n%s" % contents['local_range']
    auto_text += "\n-----\nEND AUTO GENERATED SECTION\n-----\n"
        
    cargo = {'action': 'edit', 'token' : token ,
             'title' : 'Annotation_Extension_Relation:' + shorthand, 'section' : 1,
             'text' : auto_text, 'contentmodel' : 'wikitext' }
    edit_page = wiki.call(cargo)
    
pdm = load_json("../data/gorel_test.json")
for r in pdm:
    # check that page already exists
    edit_page(wiki = wiki, shorthand = r, pdm = pdm)
    
