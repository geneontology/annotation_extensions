Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## happens_during
* OWL ID: RO_0002092
* label: happens during
* synonyms
[u'occurs_during', u'during']

### Definition


### Usage
Identifies a process or life stage during which a molecular function or biological process occurs.  This is weaker than parthood.  So, for example, some various processes occur during gastrulation without being part of that process.

### Comment
X happens_during Y iff: (start(Y) before_or_simultaneous_with start(X)) AND (end(X) before_or_simultaneous_with end(Y))

### Subsets
[display_for_curators, AE_biological_process, AE_developmental_stages, ro-eco]

##local domain
{u'BFO:0000015': u'process'}

## local range
{u'WBls:0000075': u'Nematoda Life Stage', u'ZFS:0100000': u'ZFS:0100000', u'GO:0008150': u'biological_process'}

---------------END AUTO GENERATED SECTION---------------













Comment
-------

This relationship can be used in two ways:

-   To add a **PHASE** to the annotation extension field of a biological processes the **ONLY** relationship to use is happens\_during (not part\_of)
-   To add a *biological process* to the annotation extension field when the role of the gene product in the process is unclear, but occurs during this specific *biological process*. Consider the use of the relationship [part\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/part_of.md) if it is known that the process is definitely part of the biological process.

To link a **physical entity** (*cellular component*) to a process by duration, use the relationship **exists\_during.**

Synonym
-------

occurs\_during (EXACT)

Annotation Extension Usage Examples
-----------------------------------

**1. A process occurring during cell development**

Statement from paper:

*In most cell systems that have been examined, the primary signal transduction pathway for BMPs involves phosphorylation of Smad-1 [22]... To determine if BMP-5 initiates similar signaling events in sympathetic neurons, cultured sympathetic neurons grown in the absence of glial cells were treated with BMP-5 for 30 or 60 min then analyzed by Western blotting using Abs specific for total Smad-1 or for phosphorylated Smad-1. Phosphorylation of Smad-1 is evident within 30 min after exposure to BMP-5 (Figure 4A) with significantly increased pSmad-1 levels apparent at 60min. In contrast, treatment with BMP-5 did not alter levels of total Smad-1 (Figure 4B).*

| Gene Name (col 2)                            | GO ID (col 5)                                                                                                        | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                     |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------------------------|
| P22003 <span style="color:green">BMP5</span> | <GO:0010862> <span style="color:green">positive regulation of pathway-restricted SMAD protein phosphorylation</span> | <PMID:11580864>   | IDA              | happens\_during(GO:0016358 <span style="color:green">dendrite development</span>) |

**2. A process occurring during a cell cycle phase**

Statement from paper:

We here show that the mitotic master phosphatase Cdc14 targets Yen1 to the nucleus in early anaphase through the FEAR network. In Figure 2, Yen1 re-localizes back to the nucleus in early anaphase in a Cdc14-dependent manner.

| Gene Name (col 2)                             | GO ID (col 5)                                                                 | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                 |
|-----------------------------------------------|-------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------|
| Q00684 <span style="color:green">cdc14</span> | <GO:0034504> <span style="color:green">protein localization to nucleus</span> | <PMID:24626187>   |                  | happens\_during(GO:0000090 <span style="color:green">mitotic anaphase</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship happens\_during
--------------------------------------------------------------------------------------------------------------------------------

**2. A process occurring during a cell cycle phase** Cdc14 targets Yen1 to the nucleus in early anaphase, <PMID:24626187>

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                  | Reference (Col 6) | Extension (Col 16)                                                            | Parent terms for new folded GO term                                                                                                                                                         |
|-----------------|------------|----------------|----------------------------------------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | Q00684     | cdc14          | <GO:0034504> <span style="color:green">protein localization to nucleus</span>                                  | <PMID:24626187>   | happens\_during(GO:0000090 <span style="color:green">mitotic anaphase</span>) |                                                                                                                                                                                             |
| Folded          | Q00684     | cdc14          | New GO term: <span style="color:green">protein localization to nucleus during mitotic anaphase</span> | <PMID:24626187>   |                                                                               | is a <GO:0034504> <span style="color:red">protein localization to nucleus</span> AND part\_of<span style="color:red"></span> <GO:0000090> <span style="color:red">mitotic anaphase</span> |
||

**OWL class expression:** <GO:0034504> <span style="color:red">protein localization to nucleus</span> AND happens\_during SOME <GO:0000090> <span style="color:red">mitotic anaphase</span>

**3. Specifying the developmental process during which another biological process is occurs, but where the role of the biological process in the developmental processes is unknown.**  No usage examples for this currently exist

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                           | Reference (Col 6) | Extension (Col 16)                                                               | Parent terms of new folded GO term                                                                                                                                                              |
|-----------------|------------|----------------|---------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | ID         | Protein A      | <GO:0060070> <span style="color:green">canonical Wnt signaling pathway</span>                           | PMID: ID          | happens\_during (GO:0035108 <span style="color:green">limb morphogenesis</span>) |                                                                                                                                                                                                 |
| Folded          | ID         | Protein A      | New GO term: <span style="color:green">canonical Wnt signaling pathway during limb morphogenesis </span> | PMID: ID          |                                                                                  | is\_a <GO:0060070> <span style="color:red">canonical Wnt signaling pathway</span> AND part\_of<span style="color:red"> </span> <GO:0035108> <span style="color:red">limb morphogenesis</span> |
||

**OWL class expression:** <GO:0060070> <span style="color:red">canonical Wnt signaling pathway</span> AND happens\_during SOME <GO:0035108> <span style="color:red">limb morphogenesis</span>

Note that in this example the GO term <GO:0035108> <span style="color:green">limb morphogenesis</span> is not directly associated with Protein A, whereas in the [part\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/part_of.md) example it is known that Protein A plays a role in limb morphogenesis and therefore the additional annotation <GO:0035108> <span style="color:green">limb morphogenesis</span> is directly associated with Protein A.

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
