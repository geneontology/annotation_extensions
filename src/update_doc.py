from uk.ac.ebi.brain.core import Brain
from owltools.graph import OWLGraphWrapper
import re
import warnings
from urllib2 import urlopen
import codecs
import json
from subprocess import check_output

def load_json(path):
    json_file = open(path, "r")
    json_string = json_file.read()
    json_file.close()
    return json.loads(json_string)


class om():
    
    def __init__(self, uri_or_fp):
       self.b = Brain()
       self.b.learn(uri_or_fp)
       self.o = self.b.getOntology()
       self.bsfp = self.b.getBidiShortFormProvider() # uses .getEntity(<string> shortForm), .getShortForm(OWLEntity entity)
       self.ogw = OWLGraphWrapper(self.o)

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
        auto_text =  "## Text extracted from ontlogy: DO NOT EDIT\n"
        auto_text += "* OWL ID: %s\n" % r
        auto_text += "* shorthand: %s\n" % self.test_then_get_annotation(r, "shorthand")
        auto_text += "* label: %s\n" % self.test_then_get_annotation(r, 'label')
        auto_text += "### Definition\n%s\n" % self.test_then_get_annotation(r, "IAO_0000115")
        auto_text += "### Usage\n%s\n" % self.test_then_get_annotation(r, "usage")
        auto_text += "### Subsets\n%s\n" % str(self.ogw.getSubsets(self.bsfp.getEntity(r)))
        local_domain = self.test_then_get_annotation(r, "local_domain")
        local_range = self.test_then_get_annotation(r, "local_range")
        ldd = {}    
        if local_domain:
            for ld in local_domain.split(" "):
                if ld in id_name.keys():
                    ldd[ld] = id_name[ld]
                else:
                    ldd[ld] = ''
        auto_text += "=== local domain ===\n%s\n" % str(ldd)
        lrd = {}           
        if local_range:
            for lr in local_range.split(" "):
                if lr in id_name.keys():
                    lrd[lr] = id_name[lr]
                else:
                    lrd[lr] = ''
        auto_text += "=== local range ===\n%s\n" % str(lrd)
        auto_text += "\n---------------END AUTO GENERATED SECTION---------------\n"
        return auto_text

def test_includes():
    gorel_m = om("http://purl.obolibrary.org/obo/go/extensions/gorel.owl")
    id_name = load_json("../data/id_name.json")
    rels = gorel_m.get_valid_OP_list()
    return gorel_m.gen_includes_md(rels[0], id_name)

def __main__():
    gorel_m = om("http://purl.obolibrary.org/obo/go/extensions/gorel.owl")
    rels = gorel_m.get_valid_OP_list()
    id_name = load_json("../data/id_name.json")
    for sfid in rels:
        auto_content = gorel_m.gen_includes_md(sfid, id_name)
        r = gorel_m.test_then_get_annotation(sfid, 'shorthand')
        first_pass(r, auto_content) # Use this for first set of runs
#       update(r, auto_content) # Uncomment once editing moves to GitHub

def first_pass(r, auto_text):
    """First pass conversion from wiki
    r = shorthand,
    auto_text = auto gen to insert
    """

    sprint_url = 'http://wiki.geneontology.org/api.php?format=json&action=query&titles=Annotation_Extension_Relation:%s&prop=revisions&rvprop=content'
    url = sprint_url % r
    print "Proccessing: %s\n" % url
    uo = urlopen(url)
    wiki_out = codecs.open("../doc/archive/%s.wiki" % r, 'w', 'utf-8')
    j = json.load(uo)
    # Does the page exist on the wiki.  
    if not "-1" in j['query']['pages'].keys():
        # If yes
        content = j['query']['pages'].values()[0]['revisions'][0].values()[0]
        wiki_out.write(content)
        wiki_out.close()
        try:
            md = check_output(["pandoc", "--read=mediawiki", "--write=markdown_github", "../data/%s.wiki" % r]) # simplest to write file here.
        except:
            # Should really capture any errors here!
            pass
        if md:
            archive_md_out = codecs.open("../doc/archive/%s.md" % r, 'w', 'utf-8')
            archive_md_out.write(md)
            archive_md_out.close()
            md = re.sub("Definition\n\-+\n.+Comment", auto_text + "\n\nComment", md, flags=re.DOTALL) # Check this pattern
            md = re.sub("Scope of use.+Annotation Extension Usage Examples", 'Annotation Extension Usage Examples', md, flags=re.DOTALL)
    else: 
        # if no open template.
        
        template = codecs.open("template.", "r", "utf-8")
        old_auto_text = "## Text extracted from ontlogy: DO NOT EDIT.+ -+END AUTO GENERATED SECTION-+"
        md = re.sub(pattern = old_auto_text, repl = auto_text, string = md, flags = re.DOTALL)
        template.close()   
        md_out = codecs.open("../doc/%s.md" % r, 'w', 'utf-8')
        md_out.write(md)
        md_out.close()
        
def  update(r, auto_text):
    """Update markdown
    r = shorthand,
    auto_text = auto gen to insert
    """
    md_out = codecs.open("../doc/archive/%s.md" % r, 'rw', 'utf-8')
    md = md_out.read()
    old_auto_text = "## Text extracted from ontlogy: DO NOT EDIT.+ -+END AUTO GENERATED SECTION-+"
    md = re.sub(pattern = old_auto_text, repl = auto_text, string = md, flags = re.DOTALL)
    md_out.write(md)
    md_out.close()    
     # Now to filter down - use subset ?

print test_includes()
__main__()
