Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

## Text extracted from ontlogy: DO NOT EDIT
* OWL ID: BFO_0000050
* shorthand: part_of
* label: part of

### Definition
a core relation that holds between a part and its whole

### Usage
This relation has two uses in annotation extension.  It may be used to relate a cellular component to some cellular component, cell or anatomical structure that it is part of.  It may also be used to relate a molecular function or biological process to a biological process or developmental stage of which it is a part.  It may not be used to relate cellular components to functions, processes or stages, or to relate processes or functions to cellular components, cells or anatomical structures.

### Subsets
[display_for_curators, AE_cellular_component, AE_biological_process, AE_cell_or_anatomical, AE_developmental_stages]

### synonyms
[u'part_of']

##local domain
{u'BFO:0000001': ''}

## local range
{u'WBls:0000075': '', u'GO:0005575': u'cellular_component', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy', u'PO:0009012': '', u'ZFS:0100000': '', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'GO:0008150': '', u'CL:0000000': u'cell'}

---------------END AUTO GENERATED SECTION---------------


Comment
-------

Consider using TermGenie to create a new biological process GO term. Only use this term when the role of the gene product in the process is clearly known to be involved, not just occurring during the process. Consider the use of the relationship [happens\_during](http://wiki.geneontology.org/index.php/Annotation_Extension_Relation:happens_during) if the process is not definitely part of the biological process

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Cell Component Annotations

#### Localization

#### Specifying that a gene product is located in a cellular component of a specific cell or tissue type

1. Toll-like receptor 4 (TLR4) (O00206) is located intracellularly in the perinuclear region (GO:0048471 perinuclear region of cytoplasm) only in dendritic cells (CL:0000451), <PMID:15027902>

So the annotation would be;

| DB (Col 2) | Object (Col 3) | GO ID (Col 5) | Reference (Col 6) | Extension (Col 16)   |
|------------|----------------|---------------|-------------------|----------------------|
| O00206     | TLR4           | <GO:0048471>  | <PMID:15027902>   | part\_of(CL:0000451) |
||

2. TLR4 is located on the cell surface (GO:0009986) in monocytes (CL:0000576), <PMID:15027902>

So the annotation would be;

| DB (Col 2) | Object (Col 3) | GO ID (Col 5) | Reference (Col 6) | Extension (Col 16)   |
|------------|----------------|---------------|-------------------|----------------------|
| O00206     | TLR4           | <GO:0009986>  | <PMID:15027902>   | part\_of(CL:0000576) |
||

Further examples of these usages of part\_of can be found on the documentation page for [Column\_16:\_Cell\_Type](Column_16:_Cell_Type "wikilink")

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the developmental stage at which a process occurs

We can use a developmental stage ontology and the [part\_of](part_of "wikilink") relation. part\_of is used because both the process/function and the developmental stages are things with temporal parts (they are occurrents in bfo-speak).

For example, apoptosis during Segmentation:1-4 somites in zebrafish

`ÃÂ col5:ÃÂ `[`GO:0006915`](GO:0006915)
`ÃÂ col16:ÃÂ part_of(ZFS:0000023)`

#### Functions carried out as part of a process

We use the [part\_of](part_of "wikilink") relation to link function and process (this relation is already used for the inter-ontology links)

For example, if a gene product is observed to have GTPase activity as a part of the nerve growth factor receptor signaling pathway, you would annotate:

`ÃÂ col5:ÃÂ `[`GO:0003924`](GO:0003924)`ÃÂ ÃÂ ÃÂ ÃÂ ÃÂ ÃÂ GTPaseÃÂ activity`
`ÃÂ col16:ÃÂ part_of(GO:0048011ÃÂ neurotrophinÃÂ TRKÃÂ receptorÃÂ signalingÃÂ pathway)`

AND the additional annotation col5: <GO:0048011> neurotrophin TRK receptor signaling pathway)

Note you should also include a separate annotation in which <GO:0048011> is in col5, so that people who are not using col 16 will not be worse off than they are now. See guidelines.

Note that you would not say something like this:

`ÃÂ col5:ÃÂ `[`GO:0016301`](GO:0016301)
`ÃÂ col16:ÃÂ part_of(GO:0016310)`

-   <GO:0016301> - kinase activity
-   <GO:0016310> - phosphorylation

This is harmless but pointless, because we know that kinase activity is part\_of phosphorylation from gene\_ontology\_ext

### Function-Process-Component threesomes

`ÃÂ col5:ÃÂ GOÃÂ FunctionÃÂ ID`
`ÃÂ col16:ÃÂ part_of(GOÃÂ PROCESSÃÂ ID),occurs_in(GOÃÂ CCÃÂ ID)`

Also include 2 redundant annotation lines

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship part\_of
--------------------------------------------------------------------------------------------------------------------------------------

**1. Specifying that a gene product is located in a cellular component of a specific cell or tissue type**

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                              | Reference (Col 6) | Extension (Col 16)                                                   | Parent terms of new folded GO term                                                |
|-----------------|------------|----------------|--------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Unfolded        | O00206     | TLR4           | <GO:0048471> <span style="color:green">perinuclear region of cytoplasm</span>              | <PMID:15027902>   | part\_of(CL:0000451 <span style="color:green">dendritic cell</span>) |                                                                                   |
| Folded          | O00206     | TLR4           | New GO ID <span style="color:green"> dendritic cell perinuclear region of cytoplasm</span> | <PMID:15027902>   |                                                                      | is\_a <GO:0048471> <span style="color:red">perinuclear region of cytoplasm</span> |
||

**OWL class expression:** <GO:0060070> <span style="color:red">perinuclear region of cytoplasm</span> AND part\_of SOME CL:0000451 <span style="color:red">dendritic cell</span>

**2. Specifying the developmental process which a more specific process is involved in** No usage examples for this currently exist

| Folded/unfolded       | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                | Reference (Col 6) | Extension (Col 16)                                                       | Parent terms of new folded GO term                                                                                                                            |
|-----------------------|------------|----------------|--------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded              | ID         | Protein A      | <GO:0060070> <span style="color:green">canonical Wnt signaling pathway</span>                                | PMID: ID          | part\_of(GO:0035108 <span style="color:green">limb morphogenesis</span>) |                                                                                                                                                               |
| Additional annotation | ID         | Protein A      | <GO:0035108> <span style="color:green">limb morphogenesis</span>                                             | PMID: ID          |                                                                          |                                                                                                                                                               |
| Folded                | ID         | Protein A      | New GO term <span style="color:green">canonical Wnt signaling pathway involved in limb morphogenesis </span> | PMID: ID          |                                                                          | is\_a <GO:0060070> <span style="color:red">canonical Wnt signaling pathway</span> AND part\_of <GO:0035108> <span style="color:red">limb morphogenesis</span> |
||

**OWL class expression:** <GO:0060070> <span style="color:red">canonical Wnt signaling pathway</span> AND part\_of SOME <GO:0035108> <span style="color:red">limb morphogenesis</span>

**3. Functions carried out as part of a process** No usage examples for this currently exist **NOTE** Wnt-activated receptor activity is already part\_of Wnt signaling pathway. Here we are making a more specific statement that the Wnt-activated receptor activity is part\_of a CANONICAL Wnt signaling pathway

| Folded/unfolded       | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                             | Reference (Col 6) | Extension (Col 16)                                                                    | Parent terms of new folded GO term                                                                                                                                         |
|-----------------------|------------|----------------|---------------------------------------------------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded              | ID         | Protein B      | <GO:0042813> <span style="color:green">Wnt-activated receptor activity</span>                                             | PMID: ID          | part\_of(GO:0060070 <span style="color:green">canonical Wnt signaling pathway</span>) |                                                                                                                                                                            |
| Additional annotation | ID         | Protein B      | <GO:0060070> <span style="color:green">canonical Wnt signaling pathway</span>                                             | PMID: ID          |                                                                                       |                                                                                                                                                                            |
| Folded                | ID         | Protein B      | New GO term <span style="color:green">Wnt-activated receptor activity involved in canonical Wnt signaling pathway </span> | PMID: ID          |                                                                                       | is\_a <GO:0042813> <span style="color:red">Wnt-activated receptor activity</span> AND part\_of <GO:0060070> <span style="color:red">canonical Wnt signaling pathway</span> |
||

**OWL class expression:** is\_a <GO:0042813> <span style="color:red">Wnt-activated receptor activity</span> AND part\_of SOME <GO:0060070> <span style="color:red">canonical Wnt signaling pathway</span>

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
