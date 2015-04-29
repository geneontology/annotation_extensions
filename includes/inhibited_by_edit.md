Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDES "inhibited_by_inc.md"

Comment
-------

This relation should not be used to annotate one gene product regulating another's activity; a regulator Molecular Function or regulation Biological Process should be used in such cases.

Synonyms
--------

activity\_decreased\_by (EXACT)

inhibited\_by\_chemical (EXACT)

inhibited\_by\_substance (EXACT)

Child terms
-----------

-   None.

Annotation Extension Usage Examples
-----------------------------------

| Gene Name (col 2)                         | GO ID (col 5)                                                                            | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)                                                     |
|-------------------------------------------|------------------------------------------------------------------------------------------|-------------------|------------------|--------------|-----------------------------------------------------------------------------------|
| P10869, <font color = "green">HOM3</font> | <GO:0004072> <font color = "green">aspartate kinase activity</font>                      | <PMID:18626862>   | IDA              |              | inhibited\_by: CHEBI:16857<font color = "green">L-threonine </font>               |
| P32783, <font color = "green">ABD1</font> | <GO:0004482>, <font color = "green">mRNA (guanine-N7-)-methyltransferase activity</font> | PMID: 7623811     | IDA              |              | inhibited\_by: CHEBI:16680 <font color = "green">S-adenosyl-L-homocysteine</font> |
||

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship inhibited\_by
------------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | Object (Col 2)                            | GO ID (Col 5)                                                       | Reference (Col 6) | Evidence | Extension (Col 16)                                                  | Parent terms for new folded GO term                   |
|-----------------|-------------------------------------------|---------------------------------------------------------------------|-------------------|----------|---------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | P10869, <font color = "green">HOM3</font> | <GO:0004072> <font color = "green">aspartate kinase activity</font> | <PMID:18626862>   | IDA      | inhibited\_by: CHEBI:16857<font color = "green">L-threonine </font> |                                                       |
| Folded          | P10869, <font color = "green">HOM3</font> | <GO:0004072> <font color = "green">aspartate kinase activity</font> | <PMID:18626862>   | IDA      |                                                                     | <span style="color:red">No new GO term created</span> |
||

**OWL class expression:** GO: 0004072 <font color = "red">aspartate kinase activity</font> is inhibited\_by SOME CHEBI: 16857 <font color = "red">L-threonine </font>

| Folded/unfolded | Object (Col 2)                            | GO ID (Col 5)                                                                            | Reference (Col 6) | Evidence | Extension (Col 16)                                                                | Parent terms for new folded GO term                   |
|-----------------|-------------------------------------------|------------------------------------------------------------------------------------------|-------------------|----------|-----------------------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | P32783, <font color = "green">ABD1</font> | <GO:0004482>, <font color = "green">mRNA (guanine-N7-)-methyltransferase activity</font> | PMID: 7623811     | IDA      | inhibited\_by: CHEBI:16680 <font color = "green">S-adenosyl-L-homocysteine</font> |                                                       |
| folded          | P32783, <font color = "green">ABD1</font> | <GO:0004482>, <font color = "green">mRNA (guanine-N7-)-methyltransferase activity</font> | PMID: 7623811     | IDA      |                                                                                   | <span style="color:red">No new GO term created</span> |
||

**OWL class expression:** GO: 0004482, <font color = "red">mRNA (guanine-N7-)-methyltransferase activity</font> is inhibited\_by SOME CHEBI:16680 <font color = "red">S-adenosyl-L-homocysteine</font>

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
