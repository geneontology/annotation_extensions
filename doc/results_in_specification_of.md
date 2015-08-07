Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
---------------Text extracted from ontology: DO NOT EDIT---------------

## results_in_specification_of
* OWL ID: RO_0002356
* label: results in specification of
* synonyms
[]

### Definition
The relationship linking a cell and its participation in a process that results in the fate of the cell being specified. Once specification has taken place, a cell will be committed to differentiate down a specific pathway if left in its normal environment. 

### Usage
The relationship linking a cell and its participation in a process that results in the transition of a cell such that is can only develop into a single cell type when left in its environment.

### Comment
Example of use: an annotation of gene X to cell determination with results_in_determination_of CL:0000540 (neuron) means that at the end of the process an unspecified cell will develop into a neuron if left in its environment. If the cell is moved, it may develop into a cell type other than a neuron.

### Subsets
[AE_cell_or_anatomical, display_for_curators]

##local domain
{u'GO:0008150': u'biological_process'}

## local range
{u'CL:0000000': u'cell', u'WBbt:0004017': u'Cell'}

---------------END AUTO GENERATED SECTION---------------














Comment
-------

Annotation Extension Usage Examples
-----------------------------------

**Indicating the cell or cell type specified by the activity of a gene product**

Statement from paper:

*However, the strong loss-of-function allele of eya-1, ok654 (Furuya et al., 2005), displayed M lineage phenotypes similar to ceh-34(RNAi-P): loss of M-derived CCs and variable loss of embryonic CCs (Table 1, Fig. 3A). Thus, both ceh-34 and eya-1 are required for specifying the embryonic and M-derived CCs.*

Note that in the above sentence, M refers to the M mesoblast and CCs refers to coelomocytes.

| Gene Name (col 2)                              | GO ID (col 5)                                                                    | Reference (col 6) | Evidence (col 7) | With (col 8)      | Annotation Extension (col 16)                                                             |
|------------------------------------------------|----------------------------------------------------------------------------------|-------------------|------------------|-------------------|-------------------------------------------------------------------------------------------|
| Q94165 <span style="color:green">ceh-34</span> | <GO:0007501> <span style="color:green">mesodermal cell fate specification</span> | <PMID:19427847>   | IMP              | WB:WBRNAi00101780 | results\_in\_specification\_of(WBbt:0005751 <span style="color:green">coelomocyte</span>) |
| O17670 <span style="color:green">eya-1</span>  | <GO:0007501> <span style="color:green">mesodermal cell fate specification</span> | <PMID:19427847>   | IMP              | WB:WBVar00091938  | results\_in\_specification\_of(WBbt:0005751 <span style="color:green">coelomocyte</span>) |
||

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship results\_in\_specification\_of
-----------------------------------------------------------------------------------------------------------------------------------------------

**Indicating the cell or cell type specified by the activity of a gene product**

Statement from paper:

*However, the strong loss-of-function allele of eya-1, ok654 (Furuya et al., 2005), displayed M lineage phenotypes similar to ceh-34(RNAi-P): loss of M-derived CCs and variable loss of embryonic CCs (Table 1, Fig. 3A). Thus, both ceh-34 and eya-1 are required for specifying the embryonic and M-derived CCs.*

| Folded/unfolded | Gene Name (col 2)                              | GO ID (col 5)                                                                                                              | Reference (col 6) | Evidence (col 7) | With (col 8)      | Annotation Extension (col 16)                                                             | Parent terms of new folded GO term                                      |
|-----------------|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Unfolded        | Q94165 <span style="color:green">ceh-34</span> | <GO:0007501> <span style="color:green">mesodermal cell fate specification</span>                                           | <PMID:19427847>   | IMP              | WB:WBRNAi00101780 | results\_in\_specification\_of(WBbt:0005751 <span style="color:green">coelomocyte</span>) |                                                                         |
| Unfolded        | O17670 <span style="color:green">eya-1</span>  | <GO:0007501> <span style="color:green">mesodermal cell fate specification</span>                                           | <PMID:19427847>   | IMP              | WB:WBVar00091938  | results\_in\_specification\_of(WBbt:0005751 <span style="color:green">coelomocyte</span>) |                                                                         |
| Folded          | Q94165 <span style="color:green">ceh-34</span> | <GO:0007501> <span style="color:green">mesodermal cell fate specification resulting in specification of coelomocyte</span> | <PMID:19427847>   | IMP              | WB:WBRNAi00101780 |                                                                                           | is\_a <span style="color:red">mesodermal cell fate specification</span> |
| Folded          | O17670 <span style="color:green">eya-1</span>  | <GO:0007501> <span style="color:green">mesodermal cell fate specification resulting in specification of coelomocyte</span> | <PMID:19427847>   | IMP              | WB:WBVar00091938  |                                                                                           | is\_a <span style="color:red">mesodermal cell fate specification</span> |
||

**OWL class expression:**

------------------------------------------------------------------------

**OWL class expression:** <GO:0007501> <span style="color:red">mesodermal cell fate specification</span> results\_in\_specification\_of SOME WBbt:0005751 <span style="color:red">coelomocyte</span>

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
