Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
---------------Text extracted from ontology: DO NOT EDIT---------------

## has_regulation_target
* OWL ID: GOREL_0000015
* label: has_regulation_target
* synonyms
[u'regulates']

### Definition


### Usage
Use this relationship to link a regulatory process or function to an entity that (such as a gene, gene product, or complex) participates in the regulated process.

### Comment
probably want to add one or two new subtypes that capture something about directness

### Subsets
[valid_for_annotation_extension, AE_sequence_or_complex, display_for_curators]

##local domain
{}

## local range
{u'CHEBI:33697': u'ribonucleic acid', u'SO:0000673': u'transcript', u'GO:0032991': u'macromolecular complex', u'MI:0315': u'protein complex', u'PR:000000001': u'protein', u'SO:0000704': u'gene'}

---------------END AUTO GENERATED SECTION---------------
























Comment
-------

[**More details on the limited use of has\_regulation\_target with regulation of biological process annotations**](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_participant.md)

Annotation Extension Usage Examples
-----------------------------------

**Loss of transcription factor activity affects gene expression:**

Statements from paper:

*Indeed, LGG-1 was massively upregulated in atf-2(tm467) mutant embryos, as compared with the wild type (Fig. 6A). We observed a similar extent of BEC-1 upregulation in the atf-2-deficient background (data not shown).*

Expressed in LEGO: <http://model.geneontology.org/5482537600000031>

| Gene Name (col 2)           | GO ID (col 5)                                                                                                      | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                             |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WBGene00000220 atf-2(tm467) | <GO:0000122> <span style="color:green">negative regulation of transcription from RNA polymerase II promoter</span> | <PMID:21502138>   | IMP              | has\_regulation\_target(WB:WBGene00000247 <span style="color:green">bec-1</span>) 'pipe' has\_regulation\_target(WB:WBGene00002980 <span style="color:green">lgg-1</span> |

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship has\_regulation\_target
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

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
