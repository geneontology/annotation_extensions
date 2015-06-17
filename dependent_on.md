# Dependent_on 

This has been used in [1800 annotations](https://docs.google.com/spreadsheets/d/1EMOPz40-ArYlNBPJa9dfeIXXiPKmo8HpPH4o61TQgDM/edit#gid=0)

It has been proposed that this relationship is depreciated
Suggestions need to be made to:
* 1. explain how to capture the current annotations to this term in GO AE field
* 2. document whether or not the information should be in GO at all

## Examples 

Many of these look like the extension information cannot be covered using the AE current relationships, and may be out of the scope of GO. Considerable guidance is required in order to ensure edits follow consistent approach, ie improved documentation 							
### ChEBI ID
SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|
SGD | P25632 | GO:0015616 | DNA translocase activity | dependent_on(CHEBI:15422: ATP | IDA | PMID | 17918861

wide range of BP and MFs with ChEBI IDs. Possible activated\_by or has\_input?  							
							
### GO ID
SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|
PARL | O75460 | GO:0006379 | mRNA cleavage | dependent_on(GO:0042803 protein homodimerization activity | IDA | PMID | 21317875
PARL | Q02948 | GO:0000045 | autophagic vacuole assembly | dependent_on(GO:0031667) response to nutrient levels  | IGI | PMID | 23878393
SWIS | Q7TS55 | GO:0045785 | positive regulation of cell adhesion | dependent_on(GO:0032496 response to lipopolysaccharide | IMP | PMID | 23892569
SWIS | P07108 | GO:0046983 | protein dimerization activity | dependent_on(GO:0036042) long-chain fatty acyl-CoA binding  | IDA | PMID | 21079819
BHFL | O43474 | GO:0045944 | positive regulation of transcription from RNA polymerase II promoter | dependent_on(GO:0000165 MAPK cascade | IGI | PMID | 20551324

all BP and MF annotations C16 dependent_on GO IDs, consider changing to part\_of, or reversing extension and using causally\_upstream\_of	

SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|					
SWIS | Q60855 | GO:0097527 | necroptotic signaling pathway | dependent_on(GO:0004672) protein kinase activity | IMP | PMID | 21876153
would this one work in reverse, stating protein kinase activity part of necroptotic signaling pathway?				

SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|					
SWIS | Q15485 | GO:0001867 | complement activation, lectin pathway | dependent_on(GO:0003823 antigen binding | IDA | PMID | 14707097
would this one work in reverse, stating antigen binding part of complement activation, lectin pathway?				

SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|
SGD | P04147 | GO:0010494 | cytoplasmic stress granule | dependent_on(GO:0034605) cellular response to heat | IDA | PMID | 24291094
SWIS | P07737 | GO:0005938 | cell cortex | dependent_on(GO:0006939) smooth muscle contraction | IDA | PMID | 24700464
SWIS | D4ABB2 | GO:0005783 | endoplasmic reticulum | dependent_on(GO:0000226 microtubule cytoskeleton organization | IDA | PMID | 19931615
all CC annotations C16 dependent_on GO IDs, consider changing to exists_during

SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|					BHFL | Q13635 | GO:0072661 | protein targeting to plasma membrane | dependent_on(GO:0005119) smoothened binding  | IDA | PMID | 11278759
SGD | P38144 | GO:0016887 | ATPase activity | dependent_on(GO:0000786) nucleosome | IDA | PMID | 12482963
SPOM | U3H042 | GO:0000778 | condensed nuclear chromosome kinetochore | dependent_on(GO:0000818) nuclear MIS12/MIND complex | IDA | PMID | 22711988
SWIS | Q99829 | GO:0016020 | membrane | dependent_on(GO:0005509) calcium ion binding | IDA | PMID | 25450385
No idea what to suggest with these							
							
### Pfam IDs
SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|
SPOM | O60132 | GO:0005515 | protein binding | dependent_on(Pfam:PF00018) SH3 domain | IPI | PMID | 24554432
this hasn't been annotated to SH3 domain binding, so presumably this means that the protein annotated needs to have the SH3 domain to bind the target, is it necessary to state this? Is the the reciprocal annotation to SH3 binding							
							
### Protein IDs
SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|
SPOM | Q9US03 | GO:0036449 | microtubule minus-end | dependent_on(PomBase:SPAC18G6.15) mal3 | IDA | PMID | 24039245
PARL | Q9C0C7 | GO:0043552 | positive regulation of phosphatidylinositol 3-kinase activity | dependent_on(UniProtKB:O60260) | IDA | PMID | 21753002
is this suggesting that we list all proteins involved in a process in C16?	

SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|					
SWIS | Q9ESD1 | GO:0005615 | extracellular space | dependent_on(UniProtKB:O70362) | IDA | PMID | 16822939
annotate the reverse ie O70362 protein localization to extracellular space C16 transports Q9ESD1							
							
### SO IDs
SOURCE| ANNOTATED| GO_ID | GO_NAME | ANNOTATION EXTENSIONS | EVIDENCE | PUB TYPE | PUB ACC |
------|----------|-------|---------|-----------------------|----------|----------|---------|
WB | G5EDK8 | GO:0042826 | histone deacetylase binding | dependent_on(SO:0000170 RNApol_II_promoter  | IPI | PMID | 23437011
WB | O17695 | GO:0001103 | RNA polymerase II repressing transcription factor binding | dependent_on(SO:0000170 RNApol_II_promoter  | IPI | PMID | 23437011
could this be Occurs_at?							
