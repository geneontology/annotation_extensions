Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

## Text extracted from ontlogy: DO NOT EDIT
* OWL ID: RO_0002218
* shorthand: has_agent
* label: has active participant

### Definition
x has participant y if and only if x realizes some active role that inheres in y

### Usage
The relationship that links an entity with a process in which the entity participates in the process by serving as the continuant that is responsible for the execution of the process.

### Subsets
[display_for_curators, AE_cellular_component, AE_cell_or_anatomical, ro-eco]

### synonyms
[u'has agent']

##local domain
{u'GO:0008150': ''}

## local range
{u'GO:0005575': u'cellular_component', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'CL:0000000': u'cell'}

---------------END AUTO GENERATED SECTION---------------


Comment
-------

### Local Range

CL:0000000 (cell), <GO:0005575> (cellular component), PO:0025131 (plant anatomical entity), UBERON:0001062 (anatomical entity), WBbt:0004017 (cell), WBbt:0005766 (anatomy)

Annotation Extension Usage Examples
-----------------------------------

Annotation Extension Usage Examples
-----------------------------------

1. Recording the cell type that is the agent in a secretion process

| Gene Name (col 2) | GO ID (col 5)                           | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)              |
|-------------------|-----------------------------------------|-------------------|------------------|--------------|--------------------------------------------|
| A2A7Q8            | <GO:0072643> interferon-gamma secretion |                   | ECO:0000315      |              | has\_agent(CL:0000623 natural killer cell) |

2. Recording the agent involved in a transport process

| Gene Name (col 2) | GO ID (col 5)                                               | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)            |
|-------------------|-------------------------------------------------------------|-------------------|------------------|--------------|------------------------------------------|
| F1PRN2            | <GO:0061502> early endosome to recycling endosome transport |                   | ECO:0000314      |              | has\_agent(GO:0005884; (actin filament)) |

(Question - could this be better recorded in the ontology?)

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship has\_agent
---------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                           | Reference (Col 6) | Extension (Col 16) | Parent terms for new folded GO term                        |
|-----------------|------------|----------------|-----------------------------------------|-------------------|--------------------|------------------------------------------------------------|
| Unfolded        |            | A2A7Q8         | <GO:0072643> interferon-gamma secretion |                   |                    | has\_agent(CL:0000623 natural killer cell)                 |
| Folded          |            | A2A7Q8         | ??                                      |                   |                    | is\_a <GO:0002370> natural killer cell cytokine production |
||

**OWL class expression:**

interferon-gamma secretion and has\_agent some 'naural killer cell'

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")