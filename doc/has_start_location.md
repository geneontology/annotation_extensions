Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## has_start_location
* OWL ID: RO_0002231
* label: has start location
* synonyms
[]

### Definition
x 'has starts location' y if and only if there exists some process z such that x 'starts with' z and z 'occurs in' y

### Usage
Use this relation to relate a biological process to its start location.  Note, if the entire process occurs in a particular location, use 'occurs in' instead.

### Comment


### Subsets
[valid_for_annotation_extension, ro-eco, AE_cell_or_anatomical, AE_cellular_component, display_for_curators]

##local domain
{u'BFO:0000015': u'process'}

## local range
{u'CL:0000000': u'cell', u'NCBITaxon:1': u'', u'GO:0005575': u'cellular_component', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy'}

---------------END AUTO GENERATED SECTION---------------


Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)
