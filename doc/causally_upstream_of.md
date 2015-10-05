Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

..

---------------END AUTO GENERATED SECTION---------------

Annotation Extension Usage Examples
-----------------------------------

**1. Specifying the biological process upstream of the regulation of mRNA expression levels.**

Summary of paper, [<PMID:11875061>](http://www.ncbi.nlm.nih.gov/pubmed/11875061):

*Transfection of mouse Foxa2 into rat INS-r3 cells results in blunted glucose-stimulated insulin secretion and drastically decreased mRNA levels of insulin, GLUT2 and glucokinase. In contrast, loss of Foxa2 function leads to up-regulation of hexokinase (HK) I and II and glucokinase (HK-IV) mRNA expression and down-regulation of KATP Channel Subunits Sur1 and Kir6.2 mRNA expression. High levels of the glucose transporter Glut2, enable rapid equilibration of glucose across the plasma membrane, whereas low levels of high affinity hexokinase isoforms (hexokinases I, II, and III) optimize glucose sensing in the physiological blood glucose range. Glucokinase (hexokinase IV) is rate-limiting enzyme for glucose metabolism, and determines the glucose sensing in pancreatic β-cells.* Expressed in LEGO: <http://go-genkisugi.rhcloud.com/seed/model/gomodel:taxon_10090-5437882f0000010>

| DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                                  | Reference (Col 6) | Evidence (Col 7) | Extension (Col 16)                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P35583     | Foxa2          | <GO:0000433> <span style="color:green"> negative regulation of transcription from RNA polymerase II promoter by glucose</span> | 11875061          | IDA              | causally\_upstream\_of <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span> has\_regulation\_target(UniProtKB:P14246 Slc2a2) <span style="color:green">Glut2</span>| causally\_upstream\_of <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span> has\_regulation\_target(UniProtKB:P52792 GCK) <span style="color:green">Glucokinase</span> |
| P35583     | Foxa2          | <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span>                                     | 11875061          | IDA              |                                                                                                                                                                                                                                                                                                                                                                                                                         |
||

**2. Specifying the biological process downstream of regulation of protein levels.**

Summary of paper, [<PMID:24553947>](http://www.ncbi.nlm.nih.gov/pubmed/24553947):

*Loss of PINK1 in PINK1-/- knockout mice decreased HIF-1alpha translation, thus resulting in a lower HIF-1alpha level. PINK-/- mice exhibited significantly reduced induction of HIF-1aplha protein, HIF-1alpha transcriptional activity, and hypoxia-responsive gene up regulation*

Expressed in LEGO: <http://go-genkisugi.rhcloud.com/seed/model/gomodel:taxon_9606-5437882f0000001>

Background, and paper in more detail

*HIF-alpha is a transcription factor that under hypoxia binds to hypooxia-response elements (HREs) in the promoter, and up regulates HRE-containing genes that govern a multitude of cellular functions. In PMID 24553947, the inductions of three HRE genes (GLUT-1, BNIP3 and VEGFalpha) were examined. BNIP3 and VEGFalpha mRNA increased more dramatically in PINK+/+ than PINK -/- primary neurons treated with 1%O2. And PINK+/+ MEFs had significantly higher levels of GLUT-1 and BNIP3 mRNA. Luciferase assays demonstrate reduced HIF-1alpha activity in PINK1-/- knockout MEFs*

| DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                                    | Reference (Col 6) | Evidence (Col 7) | Extension (Col 16)                                                                                                                                                                                                                                 |
|------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q99MQ3     | Pink1          | <GO:0045727> <span style="color:green">positive regulation of translation</span>                                                 | <PMID:24553947>   | IMP              | causally\_upstream\_of <GO:0051091> <span style="color:green">positive regulation of sequence-specific DNA binding transcription factor activity</span> has\_regulation\_target(UniProtKB:Q61221 Hif1a) <span style="color:green">HIF1alpha</span> |
| Q99MQ3     | Pink1          | <GO:0051091> <span style="color:green">positive regulation of sequence-specific DNA binding transcription factor activity</span> | <PMID:24553947>   | IMP              | has\_regulation\_target(UniProtKB:Q61221 Hif1a)                                                                                                                                                                                                    |
||

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship causally\_upstream\_of
----------------------------------------------------------------------------------------------------------------------------------------------------

 **1. Specifying the biological process upstream of the regulation of mRNA expression levels.**

Summary of paper, [<PMID:11875061>](http://www.ncbi.nlm.nih.gov/pubmed/11875061):

*Transfection of mouse Foxa2 into rat INS-r3 cells results in blunted glucose-stimulated insulin secretion and drastically decreased mRNA levels of insulin, GLUT2 and glucokinase. In contrast, loss of Foxa2 function leads to up-regulation of hexokinase (HK) I and II and glucokinase (HK-IV) mRNA expression and down-regulation of KATP Channel Subunits Sur1 and Kir6.2 mRNA expression. High levels of the glucose transporter Glut2, enable rapid equilibration of glucose across the plasma membrane, whereas low levels of high affinity hexokinase isoforms (hexokinases I, II, and III) optimize glucose sensing in the physiological blood glucose range. Glucokinase (hexokinase IV) is rate-limiting enzyme for glucose metabolism, and determines the glucose sensing in pancreatic β-cells.*

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                                  | Reference (Col 6) | Evidence (Col 7) | Extension (Col 16)                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | P35583     | Foxa2          | <GO:0000433> <span style="color:green"> negative regulation of transcription from RNA polymerase II promoter by glucose</span> | 11875061          | IDA              | causally\_upstream\_of <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span> has\_regulation\_target(UniProtKB:P14246 Slc2a2) <span style="color:green">Glut2</span>| causally\_upstream\_of <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span> has\_regulation\_target(UniProtKB:P52792 GCK) <span style="color:green">Glucokinase</span> |
| Folded          | P35583     | Foxa2          | <GO:0000433> <span style="color:green"> negative regulation of transcription from RNA polymerase II promoter by glucose</span> | 11875061          | IDA              | <span style="color:red">No new GO term created</span>                                                                                                                                                                                                                                                                                                                                                                   |
||

|}

**OWL class expression:** <GO:0000433> <span style="color:red">negative regulation of transcription from RNA polymerase II promoter by glucose</span> AND causally\_upstream\_of SOME <GO:2000971> <span style="color:red">negative regulation of detection of glucose</span> AND has\_regulation\_target SOME UniProtKB:P52792 <span style="color:red">Glucokinase</span>


Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

