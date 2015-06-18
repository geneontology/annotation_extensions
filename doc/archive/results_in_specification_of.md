Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

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

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
