Definition
----------

Identifies a chemical, gene product or complex in the absence of which an ontology term is observed to apply to the annotated gene product.

Child terms
-----------

-   None.

Annotation Extension Usage Examples
-----------------------------------

**Protein localization to component only occurs when substance is absent**

SCAP (P97260) acts as a SREBP escort protein to localize SREBP from the ER to the Golgi ONLY in sterol-depleted conditions.

| Gene Name (col 2) | GO ID (col 5)                                                                         | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                        |
|-------------------|---------------------------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------|
| P97260            | <GO:0090110> <span style="color:green">cargo loading into COPII-coated vesicle</span> | <PMID:15899885>   | IDA              | in\_absence\_of(CHEBI:15889 <span style="color:green">sterol</span>) |

| Gene Name (col 2) | Qualifier (col 4) | GO ID (col 5)                                                    | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                        |
|-------------------|-------------------|------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------|
| P97260            | colocalizes\_with | <GO:0030127> <span style="color:green">COPII vesicle coat</span> | <PMID:15899885>   | IDA              | in\_absence\_of(CHEBI:15889 <span style="color:green">sterol</span>) |

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
