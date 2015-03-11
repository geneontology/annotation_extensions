Usage
----------

Identifies a process or stage during which a cellular component is present.

Child terms
-----------

-   None.

Scope of use
------------

### Domain

BFO:0000004 ! independent continuant (Cellular Component)

### Range

<GO:0008150> ! Biological Process, WBls:0000075 ! nematode life stage, ZFS:0100000 ! Zebrafish stage

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Cell Component Annotations

Cellular component annotations can be enhanced by specifying that localization is observed during a cell cycle or developmental stage, or in the context of a specific biological process.

1. If a gene product is localized to the nuclear periphery in S phase, G2, and mitosis (S. pombe Ulp1; <PMID:11884512>):

` col 5: `[`GO:0034399`][]` ! nuclear periphery`
` col 16: exists_during(GO:0000084)|exists_during(GO:0000085)|exists_during(GO:0007067) ! S phase of mitotic cell cycle,`
` G2 phase of mitotic cell cycle, and mitosis respectively`

2. If a gene product is localized to the spindle pole body (SPB) and nucleolus in interphase and to the actin contractile ring, the mitotic spindle, and kinetochores during mitosis (S. pombe Clp1; <PMID:16085490>):

` col 5: `[`GO:0005816`][]` ! spindle pole body`
` col 16: exists_during(GO:0051329) ! interphase of mitotic cell cycle`

` col 5: `[`GO:0005730`][]` ! nucleolus`
` col 16: exists_during(GO:0051329) ! interphase of mitotic cell cycle`

` col5: `[`GO:0005826`][]` ! actomyosin contractile ring`
` col 16: exists_during(GO:0007067) ! mitosis`

` col5: `[`GO:0000777`][]` ! condensed chromosome kinetochore`
` col 16: exists_during(GO:0007067) ! mitosis`

Note that an experiment that supports 'CC exists\_during BP' may also support an annotation of the ['BP occurs\_in CC'][] pattern.

Also see the [go-discuss mailing list][] for more information.

Using examples to demonstrate [Folding\_and\_Unfolding][] using the relationship exists\_during
-----------------------------------------------------------------------------------------------

**Specifying that a gene product is localized to the spindle pole body (SPB) and nucleolus in interphase.** <PMID:16085490>

| Folded/unfolded | DB (Col 2)   | Object (Col 3) | GO ID (Col 5)                                                                                          | Reference (Col 6) | Extension (Col 16)                                                                           | Parent terms for new folded GO term                                 |
|-----------------|--------------|----------------|--------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Unfolded        | SPAC1782.09c | Clp1           | <GO:0005816> <span style="color:green">spindle pole body</span>                                        | <PMID:16085490>   | exists\_during(GO:0051329 <span style="color:green">interphase of mitotic cell cycle</span>) |                                                                     |
| Folded          | SPAC1782.09c | Clp1           | New GO term <span style="color:green">spindle pole body during interphase of mitotic cell cycle</span> | <PMID:16085490>   |                                                                                              | is\_a <GO:0005816> <span style="color:red">spindle pole body</span> |
||

**OWL class expression:** <GO:0005816> <span style="color:red">spindle pole

  [Annotation usage examples for each annotation extension relation]: http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation
  [`GO:0034399`]: GO:0034399
  [`GO:0005816`]: GO:0005816
  [`GO:0005730`]: GO:0005730
  [`GO:0005826`]: GO:0005826
  [`GO:0000777`]: GO:0000777
  ['BP occurs\_in CC']: Annotation_Cross_Products#Specifying_the_location_in_which_a_process_happens "wikilink"
  [go-discuss mailing list]: http://fafner.stanford.edu/pipermail/go-discuss/2011-March/005560.html
  [Folding\_and\_Unfolding]: Folding_and_Unfolding "wikilink"
