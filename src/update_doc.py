from uk.ac.ebi.brain.core import Brain
from owltools.graph import OWLGraphWrapper
import re
import warnings
from urllib2 import urlopen
import codecs
import json
from subprocess import check_output
from subprocess import CalledProcessError
import os

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

# Should really split this class out into a separate file!
class om():
    
    def __init__(self, uri_or_fp):
       self.b = Brain()
       self.b.learn(uri_or_fp)
       self.o = self.b.getOntology()
       self.bsfp = self.b.getBidiShortFormProvider() # uses .getEntity(<string> shortForm), .getShortForm(OWLEntity entity)
       self.ogw = OWLGraphWrapper(self.o)
       self.start_auto_text = "---------------Text extracted from ontology: DO NOT EDIT---------------"
       self.end_auto_text = "---------------END AUTO GENERATED SECTION---------------"

    def get_valid_OP_list(self):
        """Returns a list of relations in the display_for_curators subset"""
        s = self.o.getObjectPropertiesInSignature()
        out = []
        for r in s:
            # Slightly dodgy hard-wiring of validity criterion
            if 'display_for_curators' in self.ogw.getSubsets(r):
                out.append(self.bsfp.getShortForm(r))
        return out
    
    def test_then_get_annotation(self, entity_sfid, AP):
        content = ''
        try: 
            content = self.b.getAnnotation(entity_sfid, AP)
        except: 
            warnings.warn("%s has no annotations with %s" % (entity_sfid, AP))
            pass
        return content
        
    def gen_includes_md(self, r, id_name):
        """Generate markdown for inclusion in wiki page
        r = relation_shortFormId
        id_name = and id_name dict lookup to use for domain and range
        """
        # Be carful
        auto_text =  "%s\n" % self.start_auto_text
        auto_text += "\n## %s\n" % self.test_then_get_annotation(r, "shorthand")
        auto_text += "* OWL ID: %s\n" % r
        auto_text += "* label: %s\n" % self.test_then_get_annotation(r, 'label')
        auto_text += "* synonyms\n%s\n" % str(list(self.ogw.getOBOSynonymStrings(self.bsfp.getEntity(r), []))) # could be prettified
        auto_text += "\n### Definition\n%s\n" % self.test_then_get_annotation(r, "IAO_0000115")
        auto_text += "\n### Usage\n%s\n" % self.test_then_get_annotation(r, "usage") #
        auto_text += "\n### Comment\n%s\n" % self.test_then_get_annotation(r, "comment") #  
        auto_text += "\n### Subsets\n%s\n" % str(self.ogw.getSubsets(self.bsfp.getEntity(r))) # Perhaps only display AE_
        # Finding child and parent relations would take a reasoner object call.  Better for annotators to reply on graph.
        # MIght be useful to give some record of how often used in ontology

        local_domain = self.test_then_get_annotation(r, "local_domain")
        local_range = self.test_then_get_annotation(r, "local_range")
        ldd = {}    
        if local_domain:
            for ld in local_domain.split(" "):
                if ld in id_name.keys():
                    ldd[ld] = id_name[ld]
                else:
                    ldd[ld] = ''
                    id_name[ld] = ''
        auto_text += "\n##local domain\n%s\n" % str(ldd)
        lrd = {}           
        if local_range:
            for lr in local_range.split(" "):
                if lr in id_name.keys():
                    lrd[lr] = id_name[lr]
                else:
                    lrd[lr] = ''
                    id_name[lr] = ''

        auto_text += "\n## local range\n%s\n" % str(lrd)
        auto_text += "\n%s\n" % self.end_auto_text
        return auto_text

def test_includes():
    gorel_m = om("http://purl.obolibrary.org/obo/go/extensions/gorel.owl")
    id_name = load_json("../data/id_name.json")
    rels = gorel_m.get_valid_OP_list()
    return gorel_m.gen_includes_md(rels[0], id_name)

def remove_section(wiki, section):
    # Perhaps better done using json markup from pandoc. Seems a bit heavyweight, but regex is hairy.
    # Assumes all sections to clean up are header level 2 to header level2/3
    # Tried to do level2 to level2 but stymied by what appears to be weirdly broken regex sub. Python backref malfuction?  No gp 2!
    return re.sub(pattern = "== *?%s *?==.+?==" % section, repl = r'==', string = wiki, flags = re.DOTALL|re.I)
    
def wiki_cleanup(wiki):
    wiki = re.sub(pattern = "^(back to.+?)==", repl = r'\1!INCLUDE\n\n==', string = wiki, flags = re.DOTALL|re.I)
    wiki = remove_section(wiki, "Definition")
    wiki = remove_section(wiki, "Scope of use")
    wiki = remove_section(wiki, "=domain") # assumes level 3.  Deals with regex deficiencies
    wiki = remove_section(wiki, "=range") # ditto
    wiki = remove_section(wiki, "synonym.")
    wiki = remove_section(wiki, "child terms")
    return wiki


def wiki2md(r):
    # Check if on site.
    sprint_url = 'http://wiki.geneontology.org/api.php?format=json&action=query&titles=Annotation_Extension_Relation:%s&prop=revisions&rvprop=content'
    url = sprint_url % r
    print "Proccessing: %s\n" % url
    uo = urlopen(url)
    wiki_out = codecs.open("../doc/archive/%s.wiki" % r, 'w', 'utf-8')
    j = json.load(uo)
    # Does the page exist on the wiki.  
    if not "-1" in j['query']['pages'].keys():
        # If yes
        wiki = j['query']['pages'].values()[0]['revisions'][0].values()[0]
        # convert
    else:
        wiki = open("../doc/archive/generic.wiki").read()
    #Archive + need to save to disk for external pandoc call
    wiki_out.write(wiki)
    wiki_out.close()
    # Cleanup
    wiki = wiki_cleanup(wiki)
    wiki_clean = codecs.open("../doc/archive/%s-cleaned.wiki" % r, 'w', 'utf-8')
    wiki_clean.write(wiki)
    wiki_clean.close()
    md = ''
    try:
        md = check_output(["pandoc", "--read=mediawiki", "--write=markdown_github", "../doc/archive/%s-cleaned.wiki" % r]) # simplest to write file here.
#    except CalledProcessError, e:
        # Should really capture any errors here!
 #       warnings.warn("conversion failed with error code %s and output %s", e.returncode, e.output)
    except:
        pass
    # if conversion is good
    if md:
        #archive
        archive_md_out = codecs.open("../doc/archive/%s.md" % r, 'w', 'utf-8')
        archive_md_out.write(md)
        archive_md_out.close()
        return md
    else: 
        warnings.warn("Conversion of %s failed" % r)

def include(sub_pattern, auto_text, mdin):
        return re.sub(pattern = sub_pattern.encode('utf-8'), 
                      repl = auto_text.encode('utf-8'), string = mdin.encode('utf-8'), flags = re.DOTALL)


def first_pass(r, auto_text):
    """First pass conversion from wiki
    r = shorthand,
    """
    md = wiki2md(r)
    if md: return include(sub_pattern = '!INCLUDE', auto_text = auto_text, mdin = md)
        

        


def __main__():
    gorel_m = om("http://purl.obolibrary.org/obo/go/extensions/gorel.owl")
#   gorel_m = om("/repos/go_trunk_ont/extensions/gorel.owl")
    rels = gorel_m.get_valid_OP_list()
    rels.remove('RO_0002411')  # Temporary expedient to deal with translation issued for this page
    id_name = load_json("../data/id_name.json")
    for sfid in rels:
        auto_content = gorel_m.gen_includes_md(sfid, id_name)
        r = gorel_m.test_then_get_annotation(sfid, 'shorthand')
        if not os.path.exists("../doc/%s.md" % r):
            generic = codecs.open("../doc/archive/generic.md", 'r', 'utf-8')
            existing_content = generic.read()
            generic.close()
        else:   
            file = codecs.open("../doc/%s.md" % r, 'r', 'utf-8')
            existing_content = file.read()
            file.close()
            old_auto_text = "-+Text extracted from ontology: DO NOT EDIT-+.+-+END AUTO GENERATED SECTION-+"
            existing_content = re.sub(old_auto_text, '!INCLUDE', existing_content, flags = re.DOTALL)
      # md = first_pass(r, auto_content) # Use this for first set of runs
        print "Processing %s.md" % r
        # But need to check first if file exists !
        md_out = codecs.open("../doc/%s.md" % r, 'w', 'utf-8')
        md = include(sub_pattern = "!INCLUDE", auto_text = auto_content, mdin = existing_content)
        md_out.write(md)
        md_out.close()
    write_json(id_name, "../data/id_name.json")
    


#print test_includes()

__main__()
