Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Cell Component Annotations

Cellular component annotations can be enhanced by specifying that localization is observed during a cell cycle or developmental stage, or in the context of a specific biological process.

1. If a gene product is localized to the nuclear periphery in S phase, G2, and mitosis (S. pombe Ulp1; <PMID:11884512>):

`Â colÂ 5:Â `[`GO:0034399`](GO:0034399)`Â !Â nuclearÂ periphery`
`Â colÂ 16:Â exists_during(GO:0000084)|exists_during(GO:0000085)|exists_during(GO:0007067)Â !Â SÂ phaseÂ ofÂ mitoticÂ cellÂ cycle,`
`Â G2Â phaseÂ ofÂ mitoticÂ cellÂ cycle,Â andÂ mitosisÂ respectively`

2. If a gene product is localized to the spindle pole body (SPB) and nucleolus in interphase and to the actin contractile ring, the mitotic spindle, and kinetochores during mitosis (S. pombe Clp1; <PMID:16085490>):

`Â colÂ 5:Â `[`GO:0005816`](GO:0005816)`Â !Â spindleÂ poleÂ body`
`Â colÂ 16:Â exists_during(GO:0051329)Â !Â interphaseÂ ofÂ mitoticÂ cellÂ cycle`

`Â colÂ 5:Â `[`GO:0005730`](GO:0005730)`Â !Â nucleolus`
`Â colÂ 16:Â exists_during(GO:0051329)Â !Â interphaseÂ ofÂ mitoticÂ cellÂ cycle`

`Â col5:Â `[`GO:0005826`](GO:0005826)`Â !Â actomyosinÂ contractileÂ ring`
`Â colÂ 16:Â exists_during(GO:0007067)Â !Â mitosis`

`Â col5:Â `[`GO:0000777`](GO:0000777)`Â !Â condensedÂ chromosomeÂ kinetochore`
`Â colÂ 16:Â exists_during(GO:0007067)Â !Â mitosis`

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
