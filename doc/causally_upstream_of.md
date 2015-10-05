Back to [Annotation usage examples for each annotation extension relation]

Definition
----------

Process A is causally\_upstream of process B if process A occurs first, and process A causes process B to happen. Processes A and B do not overlap.

Child terms
-----------

-   None

Scope of use
------------

### Domain

BFO:0000007 ! process (Biological Process or Molecular Function)

### Range

<GO:0008150> ! <GO:Biological> Process

<GO:0003674> ! <GO:Molecular> Function

Annotation Extension Usage Examples
-----------------------------------

**1. Specifying the biological process upstream of the regulation of mRNA expression levels.**

Summary of paper, [<PMID:11875061>]:

*Transfection of mouse Foxa2 into rat INS-r3 cells results in blunted glucose-stimulated insulin secretion and drastically decreased mRNA levels of insulin, GLUT2 and glucokinase. In contrast, loss of Foxa2 function leads to up-regulation of hexokinase (HK) I and II and glucokinase (HK-IV) mRNA expression and down-regulation of KATP Channel Subunits Sur1 and Kir6.2 mRNA expression. High levels of the glucose transporter Glut2, enable rapid equilibration of glucose across the plasma membrane, whereas low levels of high affinity hexokinase isoforms (hexokinases I, II, and III) optimize glucose sensing in the physiological blood glucose range. Glucokinase (hexokinase IV) is rate-limiting enzyme for glucose metabolism, and determines the glucose sensing in pancreatic β-cells.* Expressed in LEGO: <http://go-genkisugi.rhcloud.com/seed/model/gomodel:taxon_10090-5437882f0000010>

| DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                                                  | Reference (Col 6) | Evidence (Col 7) | Extension (Col 16)                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------|----------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P35583     | Foxa2          | <GO:0000433> <span style="color:green"> negative regulation of transcription from RNA polymerase II promoter by glucose</span> | 11875061          | IDA              | causally\_upstream\_of <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span> has\_regulation\_target(UniProtKB:P14246 Slc2a2) <span style="color:green">Glut2</span>| causally\_upstream\_of <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span> has\_regulation\_target(UniProtKB:P52792 GCK) <span style="color:green">Glucokinase</span> |
| P35583     | Foxa2          | <GO:2000971> <span style="color:green"> negative regulation of detection of glucose</span>                                     | 11875061          | IDA              |                                                                                                                                                                                                                                                                                                                                                                                                                         |
||

**2. Specifying the biological process downstream of regulation of protein levels.**

Summary of paper, [<PMID:24553947>]:

*Loss of PINK1 in PINK1-/- knockout mice decreased HIF-1alpha translation, thus resulting in a lower HIF-1alpha level. PINK-/- mice exhibited significantly reduced induction of HIF-1aplha protein, HIF-1alpha transcriptional activity, and hypoxia-responsive gene up regulation*

Expressed in LEGO: <http://go-genkisugi.rhclou>

  [Annotation usage examples for each annotation extension relation]: http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation
  [<PMID:11875061>]: http://www.ncbi.nlm.nih.gov/pubmed/11875061
  [<PMID:24553947>]: http://www.ncbi.nlm.nih.gov/pubmed/24553947
