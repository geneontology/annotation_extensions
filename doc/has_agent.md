Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
---------------Text extracted from ontology: DO NOT EDIT---------------

## has_agent
* OWL ID: RO_0002218
* label: has active participant
* synonyms
[]

### Definition
x has participant y if and only if x realizes some active role that inheres in y

### Usage
Use this relation to link a process to an entity that carries out that process. The entity may be a cellular component, a cell type or an anatomical structure. Examples include recording a vesicle type that mediates a transport process, a cell type that is the agent of a secretion process or a cell adhesion process.  Do not use this to extend a molecular function: The agents of molecular functions are gene products and complexes.  Use of this relation with a molecular function therefore consistutes reverse annotation.

### Comment
Example of use: an annotation of gene X to cytokine production with has_agent of CL:0000057 (fibroblast) means that the fibroblast is producing the cytokine.

### Subsets
[valid_for_annotation_extension, ro-eco, AE_cell_or_anatomical, AE_cellular_component, display_for_curators]

##local domain
{u'GO:0008150': u'biological_process'}

## local range
{u'CL:0000000': u'cell', u'GO:0005575': u'cellular_component', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy'}

---------------END AUTO GENERATED SECTION---------------












Annotation Extension Usage Examples
-----------------------------------

**1. Recording the cell type that is the agent in a secretion process**

| Gene Name (col 2) | GO ID (col 5)                           | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)              |
|-------------------|-----------------------------------------|-------------------|------------------|--------------|--------------------------------------------|
| A2A7Q8            | <GO:0072643> interferon-gamma secretion |                   | ECO:0000315      |              | has\_agent(CL:0000623) natural killer cell |

**2. Recording the agent involved in a transport process**

| Gene Name (col 2) | GO ID (col 5)                                               | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)            |
|-------------------|-------------------------------------------------------------|-------------------|------------------|--------------|------------------------------------------|
| F1PRN2            | <GO:0061502> early endosome to recycling endosome transport |                   | ECO:0000314      |              | has\_agent(GO:0005884) actin filament |


Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship has\_agent
---------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                           | Reference (Col 6) | Extension (Col 16) | Parent terms for new folded GO term                        |
|-----------------|------------|----------------|-----------------------------------------|-------------------|--------------------|------------------------------------------------------------|
| Unfolded        |            | A2A7Q8         | <GO:0072643> interferon-gamma secretion |                   |    has\_agent(CL:0000623 natural killer cell)                |                  |
| Folded          |            | A2A7Q8         | New GO term: interferon-gamma secretion via natural killer cell                                      |                   |                    | is\_a <GO:0002370> natural killer cell cytokine production |
||

**OWL class expression:**

interferon-gamma secretion and has\_agent some 'natural killer cell'

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

