from com.ziclix.python.sql import zxJDBC
from tsv2pdm import tab
import re
import sys
#import mygene

"""Generates usage report files for annotation extensions.  
Optionally run with a '-t' argument for testing
"""


def __main__():
    tstat = 0
    if len(sys.argv) == 2:
        if sys.argv[1] == '-t':
            tstat = 1
    con = get_con()
    report = get_all_manual_exptl_AE(con, tstat)
    #report.headers.insert(object = 'GP_NAME', index = 1)
    #for r in report.tab:
    #    r['GP_NAME'] = find_gp_name(r['GP_ID'])
    report.save_tab(path = "../includes/", file_name = "AE_unrolled.tsv", sort_keys = ('ANNOTATION_EXTENSION',))
    report = get_compact_AE(con)
    report.save_tab(path = "../includes/", file_name = "AE_compact_unrolled.tsv", sort_keys = ('ANNOTATION_EXTENSION',))
    con.close()

def dict_cursor(cursor):
    """Takes cursor as an input, following execution of a query, returns results as a list of dicts"""
    # iterate over rows in cursor.description, pulling first element
    description = [x[0] for x in cursor.description] 
    l = []
    for row in cursor: # iterate over rows in cursor
        d = dict(zip(description, row))
    #    yield dict(zip(description, row))  # This yields an iterator.  Doesn't actually run until needed.
        l.append(d)
    return l

def get_con():
    return zxJDBC.connect("jdbc:oracle:thin:@ora-vm-026.ebi.ac.uk:1531:GOAPRO",
                                 "goselect", "selectgo",
                                 "oracle.jdbc.OracleDriver")

def get_all_manual_exptl(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM (" \
                    "SELECT a.ENTITY_ID AS gp_id, a.GO_ID, t.name AS GO_name, e2g AS evidence, a.REF_DB_CODE AS ref_type, a.REF_DB_ID AS ref_acc, a.ANNOTATION_EXTENSION " \
                    "from go.v_manual_annotations a " \
                    "join go.terms t on (t.go_id = a.go_id) " \
                    "join GO.EVIDENCE2ECO e2g ON (e2g.eco_id = a.eco_id) " \
                    "where a.is_public = 'Y' " \
                    ") where ROWNUM <= 1000")
    return dict_cursor(cursor)

def get_all_manual_exptl_AE(con, tstat=0):
    """Finds all manual experimental annotations with an annotation_extension, 
    Returns a tab object of them, with all AEs unrolled to -> one per line"""
    pre = ''
    post = ''
    if tstat:
        pre = "SELECT * FROM ("
        post = ") WHERE ROWNUM <= 100"
    cursor = con.cursor()
    query = "%s SELECT a.ENTITY_ID as GP_ID, a.GO_ID, t.name as GO_NAME, e2g.code as EVIDENCE, " \
             "a.REF_DB_CODE AS REF_TYPE, a.REF_DB_ID AS REF_ACC, a.ANNOTATION_EXTENSION, a.SOURCE " \
                    "from go.v_manual_annotations a " \
                    "join go.terms t on (t.go_id = a.go_id) " \
                    "join GO.EVIDENCE2ECO e2g ON (e2g.eco_id = a.eco_id) " \
                    "where a.is_public = 'Y' " \
                    "and a.annotation_extension is not null %s" % (pre, post)
    cursor.execute(query)
    # Specify headers in order to set order of columns for printing.
    results_tab = tab(headers =  ['SOURCE', 'GP_ID', 'GO_ID', 'GO_NAME', 'ANNOTATION_EXTENSION', 'EVIDENCE', 'REF_TYPE', 'REF_ACC'])
    for r in dict_cursor(cursor):
        if r['ANNOTATION_EXTENSION']:
            results_tab.tab.extend(unroll_AE(r))
        else:
            results_tab.tab.append(r)
    results_tab.validate()
    return results_tab

def get_compact_AE(con):
    """Finds distinct set of GO + AE from manual experimental annotations with an annotation_extension, 
    Returns a tab object of them, with all AEs unrolled to -> one per line"""
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT a.GO_ID, t.name as GO_NAME, a.ANNOTATION_EXTENSION " \
                    "FROM go.v_manual_annotations a " \
                    "JOIN go.terms t ON (t.go_id = a.go_id)" \
                    "JOIN  go.eco_terms et ON (a.ECO_ID = et.ECO_ID) " \
                    "WHERE a.is_public = 'Y'" \
                    "and a.annotation_extension is not null ")
    results_tab = tab(headers =  ['GO_ID', 'GO_NAME', 'ANNOTATION_EXTENSION'])
    for r in dict_cursor(cursor):
        if r['ANNOTATION_EXTENSION']:
            results_tab.tab.extend(unroll_AE(r))
        else:
            results_tab.tab.append(r)
    results_tab.validate()
    return results_tab

def unroll_AE(r):
    """Takes a dict with a key named 'ANNOTATION EXTENSION' as arg (r).
    Assumes AEs stored as strings as they are recorded by annotators.
    Returns a list of dicts, identicial to the first by with only one AE per dict."""
    #  Note parsing good but not perfect.  Needs work.
    unrolled = []
    if not re.findall("\||\)\,", r['ANNOTATION_EXTENSION']):
        unrolled.append(r)
    else:
        AEs = re.split("\||\)\,", r['ANNOTATION_EXTENSION']) 
        for AE in AEs:
            c = r.copy()
            c['ANNOTATION_EXTENSION'] = AE
            unrolled.append(c)
    return unrolled

def AE_2_owl():
    return

def shortName_map():
    ### Needs mapping to RO!.  Easiest way is probably to merge down GOREL + imports.  Then iterate over OPs (how?)
    return

# def find_gp_name(ID):
#     mg = mygene.MyGeneInfo()
#     # Assuming uniprot for now...
#     out = mg.query(ID, scopes='uniprot', fields='symbol')
#     hits = out['hits']
#     if hits:
#         if len(hits) == 1:
#             return hits[0]['symbol']
#         else:
#             return ''
#     else:
#         return ''
__main__()
