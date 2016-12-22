Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## produced_by
* OWL ID: RO_0003001
* label: produced by
* synonyms
[]

### Definition
a produced_by b iff some process that occurs_in b has_output a.

### Usage
Use this relation to link a cell component that is the product of a cell, to the cell-type that produced it. Examples include recording the cell type that produces an exosome, an LDL, or a secreted ECM component.

### Comment


### Subsets
[valid_for_annotation_extension, ro-eco, AE_cell_or_anatomical, display_for_curators]

##local domain
{u'GO:0005575': u'cellular_component'}

## local range
{u'CL:0000000': u'cell'}

---------------END AUTO GENERATED SECTION---------------



Annotation Extension Usage Examples
-----------------------------------

**1. Recording the cell type from which a cellular component is derived**

| Gene Name (col 2) | GO ID (col 5)                           | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)              |
|-------------------|-----------------------------------------|-------------------|------------------|--------------|--------------------------------------------|
| URS000015930E\_10116            | <GO:0070062> extracellular exosome |     PMID:24743145              | ECO:0000314      |              | produced\_by(CL:0002548) cardiac fibroblast |



Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship has\_agent
---------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                           | Reference (Col 6) | Extension (Col 16) | Parent terms for new folded GO term                        |
|-----------------|------------|----------------|-----------------------------------------|-------------------|--------------------|------------------------------------------------------------|
| Unfolded        |     RNAcentral       | URS000015930E\_10116         | <GO:0070062> extracellular exosome |       PMID:24743145            |        produced\_by(CL:0002548) cardiac fibroblast             |                 |
| Folded          |      RNAcentral      | URS000015930E\_10116         | New GO term: extracellular exosome of cardiac fibroblast                                     |         PMID:24743145          |                    | is\_a <GO:0070062> extracellular exosome |
||

**OWL class expression:**

extracellular exosome and produced\_by some 'cardiac fibroblast'

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)





