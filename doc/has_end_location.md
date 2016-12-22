Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## has_end_location
* OWL ID: RO_0002232
* label: has end location
* synonyms
[]

### Definition
x 'has end location' y if and only if there exists some process z such that x 'ends with' z and z 'occurs in' y

### Usage
Use this relation to relate a biological process to the location (cell component, cell type, anatomical location) in which the process ends. Examples include recording the cell-type or cellular compartment in which a cell-cell signalling process ends. To record a location in which the entire process occurs, please use 'occurs in'.

### Comment


### Subsets
[valid_for_annotation_extension, ro-eco, AE_cell_or_anatomical, AE_cellular_component, display_for_curators]

##local domain
{u'BFO:0000015': u'process'}

## local range
{u'CL:0000000': u'cell', u'NCBITaxon:1': u'', u'GO:0005575': u'cellular_component', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy'}

---------------END AUTO GENERATED SECTION---------------



Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)
