Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the cell or tissue type which are under going the morphogenic process

**1. A protein's involvement in changing a particular cell's shape:**

Statement from paper:

*Eotaxin, eotaxin-2, and MCP-4 were the most potent inducers of eosinophil shape change, followed by MCP-3, while MCP-1 and IL-8 were inactive. MCP-4 alone showed a bell-shaped eosinophil dose-response curve over the dose range tested. Eotaxin and eotaxin-2 were inactive on monocytes (Fig. 2âB), whereas MCP-1, -3, and -4 all induced monocyte shape change, with MCP-3 exhibiting the highest potency.*

| Gene Name (col 2)                            | GO ID (col 5)                                                          | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                                      |
|----------------------------------------------|------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q99616 <span style="color:green">MCP4</span> | <GO:0008360> <span style="color:green">regulation of cell shape</span> | <PMID:10072545>   | IDA              | results\_in\_morphogenesis\_of(CL:0000771 <span style="color:green">eosinophil</span>) 'pipe' results\_in\_morphogenesis\_of(CL:0000576 <span style="color:green">monocyte</span>) |

Note the use of the pipe to create a multiple annotation extensions. The interpretation of this annotation is MCP4 is involved in the regulation of eosinophil cell shape and monocyte cell shape.

More examples of this usage of occurs\_in can be found on the documentation page for [Column\_16:\_Cell\_Type](Column_16:_Cell_Type "wikilink")

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship results\_in\_morphogenesis\_of
------------------------------------------------------------------------------------------------------------------------------------------------------------

**1. A protein's involvement in changing a particular cell's shape:**

Note the use of the pipe to create a multiple annotation extensions.

| Folded/unfolded | Gene Name (col 2)                            | GO ID (col 5)                                                                  | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                                      | Parent terms of new folded GO term                            |
|-----------------|----------------------------------------------|--------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Unfolded        | Q99616 <span style="color:green">MCP4</span> | <GO:0008360> <span style="color:green">regulation of cell shape</span>         | <PMID:10072545>   | IDA              | results\_in\_morphogenesis\_of(CL:0000771 <span style="color:green">eosinophil</span>) 'pipe' results\_in\_morphogenesis\_of(CL:0000576 <span style="color:green">monocyte</span>) |                                                               |
| Folded          | Q99616 <span style="color:green">MCP4</span> | New GO ID <span style="color:green">regulation of eosinophil cell shape</span> | <PMID:10072545>   | IDA              |                                                                                                                                                                                    | is\_a <span style="color:red">regulation of cell shape</span> |
| Folded          | Q99616 <span style="color:green">MCP4</span> | New GO ID <span style="color:green">regulation of monocyte cell shape</span>   | <PMID:10072545>   | IDA              |                                                                                                                                                                                    | is\_a <span style="color:red">regulation of cell shape</span> |

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
