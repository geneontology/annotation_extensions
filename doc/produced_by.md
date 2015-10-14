Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## produced_by
* OWL ID: RO_0003001
* label: produced by
* synonyms
[]

### Definition


### Usage
Use this relation to link an extracellular cellular_component that is a product of a cell, to a cell that produced it. Examples include exosomes, LDLs, secreted ECM components.

### Comment


### Subsets
[ro-eco, AE_cellular_component, display_for_curators]

##local domain
CL:0000000 : cell

## local range
GO:0005575 : cellular_component

---------------END AUTO GENERATED SECTION---------------

Annotation Extension Usage Examples
-----------------------------------

**1. Recording the cell type from which a cellular component is derived**

| Gene Name (col 2) | GO ID (col 5)                           | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)              |
|-------------------|-----------------------------------------|-------------------|------------------|--------------|--------------------------------------------|
| URS000015930E\_10116            | <GO:0070062> extracellular exosome |                   | ECO:0000314      |              | produced\_by(CL:0002548) cardiac fibroblast |



Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship has\_agent
---------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                           | Reference (Col 6) | Extension (Col 16) | Parent terms for new folded GO term                        |
|-----------------|------------|----------------|-----------------------------------------|-------------------|--------------------|------------------------------------------------------------|
| Unfolded        |            | URS000015930E\_10116         | <GO:0070062> extracellular exosome |                   |                    | produced\_by(CL:0002548) cardiac fibroblast                 |
| Folded          |            | URS000015930E\_10116         | New GO term: extracellular exosome of cardiac fibroblast                                     |                   |                    | is\_a <GO:0070062> extracellular exosome |
||

**OWL class expression:**

extracellular exosome and produced\_by some 'cardiac fibroblast'

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)





