Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Comment
-------

[**More details on the limited use of has\_regulation\_target with regulation of biological process annotations**](http://wiki.geneontology.org/index.php/Annotation_Extension_Relation:has_participant#Comment)

Annotation Extension Usage Examples
-----------------------------------

**Loss of transcription factor activity affects gene expression:**

Statements from paper:

*Indeed, LGG-1 was massively upregulated in atf-2(tm467) mutant embryos, as compared with the wild type (Fig. 6A). We observed a similar extent of BEC-1 upregulation in the atf-2-deficient background (data not shown).*

Expressed in LEGO: <http://go-genkisugi.rhcloud.com/seed/model/gomodel:taxon_6239-548253760000031>

| Gene Name (col 2)           | GO ID (col 5)                                                                                                      | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                             |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WBGene00000220 atf-2(tm467) | <GO:0000122> <span style="color:green">negative regulation of transcription from RNA polymerase II promoter</span> | <PMID:21502138>   | IMP              | has\_regulation\_target(WB:WBGene00000247 <span style="color:green">bec-1</span>) 'pipe' has\_regulation\_target(WB:WBGene00002980 <span style="color:green">lgg-1</span> |

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship has\_regulation\_target
-----------------------------------------------------------------------------------------------------------------------------------------------------

#### Specifying the gene which is a target of a transcription factor

**gene transcription targets**

Statement example:

*Indeed, LGG-1 was massively upregulated in atf-2(tm467) mutant embryos, as compared with the wild type (Fig. 6A). We observed a similar extent of BEC-1 upregulation in the atf-2-deficient background (data not shown).*

| Folded/unfolded | Gene Name (col 2)                                            | GO ID (col 5)                                                                                                      | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                            | Parent terms of new folded GO term                    |
|-----------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | WBGene00000220 <span style="color:green">atf-2(tm467)</span> | <GO:0000122> <span style="color:green">negative regulation of transcription from RNA polymerase II promoter</span> | <PMID:21502138>   | IMP              | has\_regulation\_target(WB:WBGene00000247 <span style="color:green">bec-1</span>)'pipe' has\_regulation\_target(WB:WBGene00002980 <span style="color:green">lgg-1</span> |
| Folded          | WBGene00000220 <span style="color:green">atf-2(tm467)</span> | <GO:0000122> <span style="color:green">negative regulation of transcription from RNA polymerase II promoter</span> | <PMID:21502138>   | IMP              |                                                                                                                                                                          | <span style="color:red">No new GO term created</span> |
||

**OWL class expression:** <GO:0000122> <span style="color:red">negative regulation of transcription from RNA polymerase II promoter</span> AND has\_regulation\_target SOME WB:WBGene00000247 <span style="color:red">bec-1</span> **OWL class expression:** <GO:0000122> <span style="color:red">negative regulation of transcription from RNA polymerase II promoter</span> AND has\_regulation\_target SOME WB:WBGene00002980 <span style="color:red">lgg-1</span>

Back to [Annotation Extension: Capturing participants](http://wiki.geneontology.org/index.php/Annotation_Extension:_Capturing_participants)

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
