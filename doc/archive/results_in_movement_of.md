Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Comment
-------

Consider instead using transports\_or\_maintains\_localization\_of

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the cell or cellular component which move in response to the gene product

**Cell adhesion molecule stimulates cell mobility**

Statement from paper:

*blood vessel epicardial substance (Bves) is critical for regulation of epicardial cell directional movement, as disruption of this interaction randomizes migratory patterns.*

| Gene Name (col 2)                            | GO ID (col 5)                                                                              | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                      |
|----------------------------------------------|--------------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------|
| Q9ES83 <span style="color:green">Bves</span> | <GO:0060973> <span style="color:green">cell migration involved in heart development</span> | <PMID:24048452>   | IMP              | results\_in\_movement\_of (CL:0002494 <span style="color:green">cardiocyte</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship results\_in\_movement\_of
------------------------------------------------------------------------------------------------------------------------------------------

**Specifying that a gene product regulates the location of cardiocytes as part of heart development .** <PMID:24048452>

Statement from paper: blood vessel epicardial substance (Bves) is critical for regulation of epicardial cell directional movement, as disruption of this interaction randomizes migratory patterns.

| Folded/unfolded | DB (Col 2) | Object (Col 3)                        | GO ID (Col 5)                                                                                   | Reference (Col 6) | Extension (Col 16)                                                                 | Parent terms for new folded GO term                                                                                                                                                                                                                |
|-----------------|------------|---------------------------------------|-------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | Q9ES83     | <span style="color:green">Bves</span> | <GO:0060973> <span style="color:green">cell migration involved in heart development</span>      | <PMID:24048452>   | results\_in\_movement\_of (CL:0002494 <span style="color:green">cardiocyte</span>) |                                                                                                                                                                                                                                                    |
| Folded          | Q9ES83     | <span style="color:green">Bves</span> | New GO term <span style="color:green">cardiocyte migration involved in heart development</span> | <PMID:24048452>   |                                                                                    | is\_a <GO:0060973> <span style="color:green">cell migration involved in heart development</span> AND is\_a New GO term <span style="color:green">cardiocyte migration</span> (parent <GO:0016477> <span style="color:green">cell migration</span>) |
||

**OWL class expression:** <GO:0060973> <font color = "red">cell migration involved in heart development</font> results\_in\_movement\_of SOME CL:0002494 <font color = "red">cardiocyte</font>

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
