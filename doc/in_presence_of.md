### DEPRECATION WARNING

The GO editors have agreed that this relation should be deprecated. The relation does not extend the meaning of the GO term, as annotation relations are meant to, but instead specifies conditions under which the annotation is true. This can not be expressed in OWL. Annotation extensions using this relation will never fold.

Annotation Extension Usage Examples
-----------------------------------

**1. Catabolism of hyaluronic acid by Hyal-1 only when CD44 antigen is present**

Statement from paper:

*Without CD44 expression, none of Hyal-1, Hyal-2, and Hyal-3 affected catabolism of fl-HA. Most of the fl-HA in the medium remained intact and was eluted in the void volume of the Sepharose CL-2B column (Fig. 2, AÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂD).*

| Gene Name (col 2) | GO ID (col 5)                                                              | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                            |
|-------------------|----------------------------------------------------------------------------|-------------------|------------------|--------------------------------------------------------------------------|
| Q12794            | <GO:0030214> <span style="color:green">hyaluronan catabolic process</span> | <PMID:17170110>   | IDA              | in\_presence\_of(UniProtKB:P16070 <span style="color:green">CD44</span>) |

**2. Activation of caspases by ACER2 in presence of 4-hydroxyphenyl retinamide**

Statement from paper:

*We found that ACER2 knockdown significantly inhibited both the 4-HPR-induced cleavage of PARP (Fig. 5E) and activation of caspase-3 (Fig. 5F), supporting that ACER2 knockdown inhibits the 4-HPR-induced cell death in tumor cells... ACER2 overexpression markedly augmented both 4-HPR-induced cleavage of PARP (Fig. 6D) and activation of caspase-3 (Fig. 6E), supporting the view that ACER2 overexpression sensitizes tumor cells to 4-HPR-induced cell death.*

| Gene Name (col 2) | GO ID (col 5)                                                                                                                  | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                             |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------|
| Q5QJU3            | <GO:0006919> <span style="color:green">activation of cysteine-type endopeptidase activity involved in apoptotic process</span> | <PMID:20628055>   | IMP              | in\_presence\_of(CHEBI:42588 <span style="color:green">4-hydroxyphenyl retinamide</span>) |

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
