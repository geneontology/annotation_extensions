Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDES "part_of_inc.md"

Comment
-------

Consider using TermGenie to create a new biological process GO term. Only use this term when the role of the gene product in the process is clearly known to be involved, not just occurring during the process. Consider the use of the relationship [happens\_during](http://wiki.geneontology.org/index.php/Annotation_Extension_Relation:happens_during) if the process is not definitely part of the biological process

Child terms
-----------

-   None

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

` col5: `[`GO:0006915`](GO:0006915)
` col16: part_of(ZFS:0000023)`

#### Functions carried out as part of a process

We use the [part\_of](part_of "wikilink") relation to link function and process (this relation is already used for the inter-ontology links)

For example, if a gene product is observed to have GTPase activity as a part of the nerve growth factor receptor signaling pathway, you would annotate:

` col5: `[`GO:0003924`](GO:0003924)`      GTPase activity`
` col16: part_of(GO:0048011 neurotrophin TRK receptor signaling pathway)`

AND the additional annotation col5: <GO:0048011> neurotrophin TRK receptor signaling pathway)

Note you should also include a separate annotation in which <GO:0048011> is in col5, so that people who are not using col 16 will not be worse off than they are now. See guidelines.

Note that you would not say something like this:

` col5: `[`GO:0016301`](GO:0016301)
` col16: part_of(GO:0016310)`

-   <GO:0016301> - kinase activity
-   <GO:0016310> - phosphorylation

This is harmless but pointless, because we know that kinase activity is part\_of phosphorylation from gene\_ontology\_ext

### Function-Process-Component threesomes

` col5: GO Function ID`
` col16: part_of(GO PROCESS ID),occurs_in(GO CC ID)`

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

<Category:Relations> <Category:Reasoning> <Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
