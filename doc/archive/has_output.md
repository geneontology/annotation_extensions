Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Comment
-------

[**More details on the limited use of has\_output with biological process annotations**](http://wiki.geneontology.org/index.php/Annotation_Extension_Relation:has_participant#Comment)

Annotation Extension Usage Examples
-----------------------------------

**1. FGF production in response to stimulation of protein A**

| Gene Name (col 2) | GO ID (col 5) | Reference (col 6)                                                                 | Evidence (col 7) | Annotation Extension (col 16)                                       |
|-------------------|---------------|-----------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------|
| Pxxxx             | Protein A     | <GO:0090269> <span style="color:green">fibroblast growth factor production</span> | <PMID:xxx>       | has\_output (UniProt:Q9GZV9 <span style="color:green">FGF23</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship has\_output
----------------------------------------------------------------------------------------------------------------------------

**1. FGF production in response to stimulation of protein A**

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                   | Reference (Col 6) | Extension (Col 16)                                                  | Parent terms for new folded GO term                                                   |
|-----------------|------------|----------------|-------------------------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Unfolded        | Pxxxx      | Protein A      | <GO:0090269> <span style="color:green">fibroblast growth factor production</span>               | <PMID:xxx>        | has\_output (UniProt:Q9GZV9 <span style="color:green">FGF23</span>) |                                                                                       |
| Folded          | Pxxxx      | Protein A      | New GO term <span style="color:green">FGF23 fibroblast growth factor cytokine production</span> | <PMID:xxx>        |                                                                     | is\_a <GO:0090269> <span style="color:red">fibroblast growth factor production</span> |
||

**OWL class expression:** <GO:0090269> <span style="color:red">fibroblast growth factor production</span> AND has\_output SOME UniProt:Q9GZV9 <span style="color:red">FGF23</span>

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink") [Category:LEGO examples](Category:LEGO examples "wikilink")
