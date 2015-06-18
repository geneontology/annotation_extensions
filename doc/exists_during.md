Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

## Text extracted from ontlogy: DO NOT EDIT
* OWL ID: GOREL_0000032
* shorthand: exists_during
* label: exists_during
### Definition

### Usage
Identifies a process or life stage during which a cellular component is present
### Subsets
[display_for_curators, AE_biological_process, AE_developmental_stages]
### synonyms
[]
=== local domain ===
{u'BFO:0000004': ''}
=== local range ===
{u'WBls:0000075': '', u'ZFS:0100000': '', u'GO:0008150': ''}

---------------END AUTO GENERATED SECTION---------------


Annotation Extension Usage Examples
-----------------------------------

### Enhancing Cell Component Annotations

Cellular component annotations can be enhanced by specifying that localization is observed during a cell cycle or developmental stage, or in the context of a specific biological process.

1. If a gene product is localized to the nuclear periphery in S phase, G2, and mitosis (S. pombe Ulp1; <PMID:11884512>):

`ÃÂ colÃÂ 5:ÃÂ `[`GO:0034399`](GO:0034399)`ÃÂ !ÃÂ nuclearÃÂ periphery`
`ÃÂ colÃÂ 16:ÃÂ exists_during(GO:0000084)|exists_during(GO:0000085)|exists_during(GO:0007067)ÃÂ !ÃÂ SÃÂ phaseÃÂ ofÃÂ mitoticÃÂ cellÃÂ cycle,`
`ÃÂ G2ÃÂ phaseÃÂ ofÃÂ mitoticÃÂ cellÃÂ cycle,ÃÂ andÃÂ mitosisÃÂ respectively`

2. If a gene product is localized to the spindle pole body (SPB) and nucleolus in interphase and to the actin contractile ring, the mitotic spindle, and kinetochores during mitosis (S. pombe Clp1; <PMID:16085490>):

`ÃÂ colÃÂ 5:ÃÂ `[`GO:0005816`](GO:0005816)`ÃÂ !ÃÂ spindleÃÂ poleÃÂ body`
`ÃÂ colÃÂ 16:ÃÂ exists_during(GO:0051329)ÃÂ !ÃÂ interphaseÃÂ ofÃÂ mitoticÃÂ cellÃÂ cycle`

`ÃÂ colÃÂ 5:ÃÂ `[`GO:0005730`](GO:0005730)`ÃÂ !ÃÂ nucleolus`
`ÃÂ colÃÂ 16:ÃÂ exists_during(GO:0051329)ÃÂ !ÃÂ interphaseÃÂ ofÃÂ mitoticÃÂ cellÃÂ cycle`

`ÃÂ col5:ÃÂ `[`GO:0005826`](GO:0005826)`ÃÂ !ÃÂ actomyosinÃÂ contractileÃÂ ring`
`ÃÂ colÃÂ 16:ÃÂ exists_during(GO:0007067)ÃÂ !ÃÂ mitosis`

`ÃÂ col5:ÃÂ `[`GO:0000777`](GO:0000777)`ÃÂ !ÃÂ condensedÃÂ chromosomeÃÂ kinetochore`
`ÃÂ colÃÂ 16:ÃÂ exists_during(GO:0007067)ÃÂ !ÃÂ mitosis`

Note that an experiment that supports 'CC exists\_during BP' may also support an annotation of the ['BP occurs\_in CC'](Annotation_Cross_Products#Specifying_the_location_in_which_a_process_happens "wikilink") pattern.

Also see the [go-discuss mailing list](http://fafner.stanford.edu/pipermail/go-discuss/2011-March/005560.html) for more information.

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship exists\_during
-------------------------------------------------------------------------------------------------------------------------------

**Specifying that a gene product is localized to the spindle pole body (SPB) and nucleolus in interphase.** <PMID:16085490>

| Folded/unfolded | DB (Col 2)   | Object (Col 3) | GO ID (Col 5)                                                                                          | Reference (Col 6) | Extension (Col 16)                                                                           | Parent terms for new folded GO term                                 |
|-----------------|--------------|----------------|--------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Unfolded        | SPAC1782.09c | Clp1           | <GO:0005816> <span style="color:green">spindle pole body</span>                                        | <PMID:16085490>   | exists\_during(GO:0051329 <span style="color:green">interphase of mitotic cell cycle</span>) |                                                                     |
| Folded          | SPAC1782.09c | Clp1           | New GO term <span style="color:green">spindle pole body during interphase of mitotic cell cycle</span> | <PMID:16085490>   |                                                                                              | is\_a <GO:0005816> <span style="color:red">spindle pole body</span> |
||

**OWL class expression:** <GO:0005816> <span style="color:red">spindle pole body</span> AND exists\_during SOME <GO:0051329> <span style="color:red">interphase of mitotic cell cycle</span>

| Folded/unfolded | DB (Col 2)   | Object (Col 3) | GO ID (Col 5)                                                                                  | Reference (Col 6) | Extension (Col 16)                                                                           | Parent terms for new folded GO term                         |
|-----------------|--------------|----------------|------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Unfolded        | SPAC1782.09c | Clp1           | <GO:0005730> <span style="color:green">nucleolus</span>                                        | <PMID:16085490>   | exists\_during(GO:0051329 <span style="color:green">interphase of mitotic cell cycle</span>) |                                                             |
| Folded          | SPAC1782.09c | Clp1           | New GO term <span style="color:green">nucleolus during interphase of mitotic cell cycle</span> | <PMID:16085490>   |                                                                                              | is\_a <GO:0005730> <span style="color:red">nucleolus</span> |
||

**OWL class expression:** <GO:0005730> <span style="color:red">nucleolus</span> AND exists\_during SOME <GO:0051329> <span style="color:red">interphase of mitotic cell cycle</span>

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
