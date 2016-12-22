Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## has_input
* OWL ID: RO_0002233
* label: has input
* synonyms
[u'has_target', u'localizes']

### Definition
p has direct input c iff c is a participant in p, c is present at the start of p, and the state of c is modified during p.

### Usage
Use this relation to relate a biological process or molecular function to an entity that participates in the process/function, is present at the start of the process/function and whose state is affected by that process/function.  Change of state includes being transported, modified, consumed or destroyed.  An input may be any continuant: chemical; gene product; cell component;  cells type; organism.  For inputs to MFs that are bound by the gene product that executes the MF, the more specific relation 'has_direct_input' may be used.

### Comment
Previous definition "p has_input c if and only c participates_in p at the start of p and c is in some way bound, transported, modified, consumed or destroyed by p." If it is known whether the entity is directly or indirectly bound/acted upon by the gene product that is the subject of the annotation, then the relations has_direct_input or has_indirect_input should be alternatively considered.

### Subsets
[valid_for_annotation_extension, AE_sequence_or_complex, ro-eco, AE_chemical, display_for_curators]

##local domain
{u'BFO:0000015': u'process'}

## local range
{u'SO:0000839': u'polypeptide_region', u'CHEBI:24431': u'chemical entity', u'NCBITaxon:1': u'', u'CHEBI:33697': u'ribonucleic acid', u'SO:0000673': u'transcript', u'GO:0032991': u'macromolecular complex', u'MI:0315': u'protein complex', u'PR:000000001': u'protein', u'SO:0000704': u'gene'}

---------------END AUTO GENERATED SECTION---------------

























Comment
-------

[**More details on the limited use of has\_input with biological process annotations**](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_participant.md)

**If you know that the target is bound by the annotated gene product then consider using this child relationship**

-   [has\_direct\_input](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_direct_input.md)

For *Molecular Function* GO terms such as [endopeptidase activity](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0004175) use the relationship ['has\_direct\_input'](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_direct_input.md) <span style="color:red">substrate</span> (possibly has\_substrate if this relationship is made available). The substrate included in the annotation extension should be known to bind the protein annotated.

The endopeptidase, in the example above, would also have the *Biological Process* GO term annotation (eg [proteolysis](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0006508) with the annotation extension relationship 'has\_input' <span style="color:red">substrate</span>.

For *Molecular Function* GO terms such as endopeptidase inhibitor activity use the relationship ['has\_direct\_input'](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_direct_input.md) <span style="color:red">endopeptidase</span>, the protein included in the annotation extension should be known to bind the annotated inhibitor.

**If the annotation associated with the gene product is a regulation of *Biological Process* then consider using the child relationship**

-   ['has\_regulation\_target'](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_regulation_target.md)<span style="color:red">target of biological process</span>

eg: [negative regulation of proteolysis](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0045861) with the annotation extension relationship ['has\_regulation\_target'](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_regulation_target.md) <span style="color:red">target of proteolysis</span>, with the substrate of the endopeptidase that is regulated by the inhibitor included in the annotation extension field

**If the annotation associated with the gene product is a regulation of *Molecular Function* (eg if the gene product is an enzyme regulator) then consider using the child relationship**

-   'has\_input'<span style="color:red">endopeptidase</span>

eg: [negative regulation of endopeptidase activity](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0010951), with the annotation relationship 'has\_input' <span style="color:red">endopeptidase</span>, the endopeptidase that is inhibited by (in this case) the endopeptidase inhibitor is included in the annotation extension field

<span style="color:blue">Therefore the endopeptidase inhibitor would have two *Biological Process* GO term annotations and one *Molecular Function* annotation eg:</span>

-   [negative regulation of proteolysis](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0045861) with the annotation extension relationship ['has\_regulation\_target'](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_regulation_target.md) <span style="color:red">substrate</span>, with the substrate of the inhibited endopeptidase included in the annotation extension field
-   [negative regulation of endopeptidase activity](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0010951), with the annotation relationship 'has\_input' <span style="color:red">endopeptidase</span>, with the endopeptidase that is inhibited in the annotation extension field
-   [endopeptidase inhibitor activity](http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0004866), with the annotation relationship ['has\_direct\_input'](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_direct_input.md) <span style="color:red">endopeptidase</span>, with the endopeptidase included in the annotation extension known to bind the annotated inhibitor.

| Folded/unfolded | Gene Name (col 2)                                | GO ID (col 5)                                                        | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                     | Parent terms of new folded GO term                    |
|-----------------|--------------------------------------------------|----------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | <span style="color:green">Endopeptidase A</span> | <GO:0004175> <span style="color:green">endopeptidase activity</span> | <PMID:1234567>    | IDA              | has\_direct\_input(<span style="color:green">substrate of endopeptidase A</span>) |                                                       |
| Folded          | <span style="color:green">Endopeptidase A</span> | <GO:0004175> <span style="color:green">endopeptidase activity</span> | <PMID:1234567>    | IDA              |                                                                                   | <span style="color:red">No new GO term created</span> |

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the chemical that was applied and induced a 'response to chemicals'

GOC policy is not to use the annotation extension field to capture the input to the process (eg a chemical/protein), instead new GO terms are requested (using Term Genie).

**Cellular response to drug**

Statement from paper: *incubation of cells with low concentrations of phenformin and depletion of Ppm1E increased AMPK phosphorylation*

So one of the annotations would be:

| DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                           | Reference (Col 6) | Evidence (Col 7) | Extension (Col 16)                                                |
|------------|----------------|-------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------|
| Q8WY54     | PPM1E          | <GO:0035690> <span style="color:green">cellular response to drug</span> | <PMID:20801214>   | IDA              | has\_input(CHEBI:6801 <span style="color:green">metformin</span>) |
||

#### Specifying the protein which is a target of a Biological Process

**Proteolysis targets**

Statement from paper: *MICA shedding by tumor cells was inhibited by silencing of the related ADAM10 and ADAM17 proteases*.

**No direct binding of MICA to ADAM10 and ADAM17 was shown therefore the relationship 'has\_direct\_input' was not applied.**

So one of the annotations would be:

| DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                         | Reference (Col 6) | Evidence (Col 7) | Extension (Col 16)                                               |
|------------|----------------|---------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------|
| O14672     | ADAM10         | <GO:0006509> <span style="color:green">membrane protein ectodomain proteolysis</span> | <PMID:18676862>   | IMP              | has\_input(UNIPROT:Q29983 <span style="color:green">MICA</span>) |
||

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship has\_input
----------------------------------------------------------------------------------------------------------------------------------------

#### Specifying the protein which is a target of a Biological Process

**Proteolysis targets**

Statement from paper: *MICA shedding by tumor cells was inhibited by silencing of the related ADAM10 and ADAM17 proteases*

| Folded/unfolded | Gene Name (col 2)                              | GO ID (col 5)                                                                         | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                    | Parent terms of new folded GO term                    |
|-----------------|------------------------------------------------|---------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | O14672 <span style="color:green">ADAM10</span> | <GO:0006509> <span style="color:green">membrane protein ectodomain proteolysis</span> | <PMID:18676862>   | IMP              | has\_input(UNIPROT:Q29983 <span style="color:green">MICA</span>) |                                                       |
| Folded          | O14672 <span style="color:green">ADAM10</span> | <GO:0006509> <span style="color:green">membrane protein ectodomain proteolysis</span> | <PMID:18676862>   | IMP              |                                                                  | <span style="color:red">No new GO term created</span> |

**OWL class expression:** <GO:0006509> <span style="color:red">membrane protein ecodomain proteolysis</span> AND has\_input SOME UNIPROT:Q29983 <span style="color:red">MICA</span>

No new term will be created in this example because this is outside of the scope of GO, although tools using GO could use the relationship to create the following:

| Folded/unfolded | Gene Name (col 2)                              | GO ID (col 5)                                                                                | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                    | Parent terms of new folded GO term                                                  |
|-----------------|------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Unfolded        | O14672 <span style="color:green">ADAM10</span> | <GO:0006509> <span style="color:green">membrane protein ectodomain proteolysis</span>        | <PMID:18676862>   | IMP              | has\_input(UNIPROT:Q29983 <span style="color:green">MICA</span>) |                                                                                     |
| Folded          | O14672 <span style="color:green">ADAM10</span> | New GO term <span style="color:green">membrane protein ectodomain proteolysis of MICA</span> | <PMID:18676862>   | IMP              |                                                                  | <GO:0006509> <span style="color:red">membrane protein ectodomain proteolysis</span> |

**OWL class expression:** <GO:0006509> <span style="color:red">membrane protein ecodomain proteolysis</span> AND has\_input SOME UNIPROT:Q29983 <span style="color:red">MICA</span>

#### Specifying the gene which is a target of a transcription factor

**gene transcription targets** <span style="color:red">**This example is still under discussion.** </span>

Statement example:

*DNA binding transcription factor A binds the promoter of Polo2 and increases transcription of Polo2*

| Folded/unfolded | Gene Name (col 2)                                            | GO ID (col 5)                                                                                                                                                                                                | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                               | Parent terms of new folded GO term                    |
|-----------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | Pxxx <span style="color:green">transcription factor A</span> | <GO:0001228> <span style="color:green">RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription</span> | <PMID:xxx>        | IDA              | has\_regulation\_target(UNIPROT:Qxxx <span style="color:green">Polo2</span>)                                                                                                |                                                       |
| Folded          | Pxxx <span style="color:green">transcription factor A</span> | <GO:0001228> <span style="color:green">RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription</span> | <PMID:xxx>        | IDA              |                                                                                                                                                                             | <span style="color:red">No new GO term created</span> |
| Unfolded        | Pxxx <span style="color:green">transcription factor A</span> | <GO:0044212> <span style="color:green">transcription regulatory region DNA binding</span>                                                                                                                    | <PMID:xxx>        | IDA              | has\_direct\_input(UNIPROT:Qxxx <span style="color:green">Polo2</span>) (could include a feature ID to specify the specific motif eg a SO ID or Ensembl ID for the gene ID) |                                                       |
| Folded          | Pxxx <span style="color:green">transcription factor A</span> | <GO:0044212> <span style="color:green">transcription regulatory region DNA binding</span>                                                                                                                    | <PMID:xxx>        | IDA              |                                                                                                                                                                             | <span style="color:red">No new GO term created</span> |

No new term will be created in this example because this is outside of the scope of GO, although tools using GO could use the relationship to create the following:

| Folded/unfolded | Gene Name (col 2)                                            | GO ID (col 5)                                                                                                                                                                                                        | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                   | Parent terms of new folded GO term                                                                                                                                                                         |
|-----------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | Pxxx <span style="color:green">transcription factor A</span> | <GO:0001228> <span style="color:green">RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription</span>         | <PMID:xxx>        | IDA              | has\_input(UNIPROT:Qxxx <span style="color:green">Polo2</span>) |                                                                                                                                                                                                            |
| Folded          | Pxxx <span style="color:green">transcription factor A</span> | New GO term <span style="color:green">RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription of Polo2</span> | <PMID:xxx>        | IDA              |                                                                 | <GO:0001228> <span style="color:red">RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription</span> |

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
