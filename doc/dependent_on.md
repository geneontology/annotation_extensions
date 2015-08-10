Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## dependent_on
* OWL ID: GOREL_0000004
* label: dependent_on
* synonyms
[u'dependent on']

### Definition
Identifies a requirement under which the ontology term is observed to apply to the annotated gene product.

### Usage
Identifies a requirement under which the ontology term is observed to apply to the annotated gene product.

### Comment
PomBase uses the more specific child relations, and avoids using dependent_on directly.

### Subsets
[AE_molecular_function, AE_biological_process, AE_sequence_or_complex, AE_sequence_feature, AE_chemical, display_for_curators]

##local domain
BFO:0000001 : entity

## local range
CHEBI:24431 : chemical entity; CHEBI:33697 : ribonucleic acid; GO:0003674 : molecular_function; GO:0008150 : biological_process; GO:0032991 : macromolecular complex; MI:0315 : protein complex; MOD:00000 : protein modification; PR:000000001 : protein; SO:0000110 : sequence_feature; SO:0000673 : transcript; SO:0000704 : gene

---------------END AUTO GENERATED SECTION---------------



















### DEPRECATION WARNING

The GO editors have agreed that this relation should be deprecated. The relation does not extend the meaning of the GO term, as annotation relations are meant to, but instead specifies conditions under which the annotation is true. This can not be expressed in OWL. Annotation extensions using this relation will not fold.

Annotation Extension Usage Examples
-----------------------------------

**1. IAP2-dependent regulation of NF-kB activity:**

Statement from paper:

*To test whether RIP3 and RIP4 have to be ubiquitinated by cIAP1/2 in order to mediate NF-kB activation, we compared RIP-mediated NF-kB luciferase reporter activity when ectopically expressed in HEK293T cells in the presence or absence of the IAP inhibitor BV6, a treatment that induces rapid auto-ubiquitination and degradation of endogenous cIAP1/2[41]. As shown in Figure 4A, BV6 treatment greatly impaired TNF and RIP1 RIP4-induced NF-kB activation but had no impact on TAK1-mediated NF-kB induction (Figure 4A). Those results, which indicate that cIAP1/2 act upstream of TAK1, are consistent with a role for cIAP1/2 as E3 ligases regulating RIP14-mediated activation of NF-kB.*

Expressed in LEGO: <http://go-genkisugi.rhcloud.com/seed/model/gomodel:taxon_9606-5408ded30000003>

| Gene Name (col 2)                            | GO ID (col 5)                                                                                                | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                         |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------------|
| Q9Y572 <span style="color:green">RIP3</span> | <GO:0051092> <span style="color:green">positive regulation of NF-kappaB transcription factor activity</span> | <PMID:21931591>   | IDA              | dependent\_on(UniProtKB:Q13490 <span style="color:green">IAP2</span>) |

**2. A protein's function is required for its involvement in a process:**

Statement from paper:

*As the mutant 79H/A expression level in 79H/A-transfected cells was lower than that of clone A106 that exhibited lipid droplet formation, we could not conclude if the reduction in enzyme activity affected the ability of ACTEIII/PTE-1 to induce lipid droplet formation. However, as the expression levels of the mutant 79H/A in these cell lines were much higher than those in clone A26, it became clear that the enzymatic activity of ACTEIII/PTE-1 was indispensable for peroxisome proliferation.*

Expressed in LEGO: <http://go-genkisugi.rhcloud.com/seed/model/gomodel:taxon_9606-5437882f0000021>

| Gene Name (col 2)                             | GO ID (col 5)                                                    | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                          |
|-----------------------------------------------|------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------------------------|
| O14734 <span style="color:green">ACOT8</span> | <GO:0016559> <span style="color:green">peroxisome fission</span> | <PMID:15194431>   | IDA              | dependent\_on(GO:0047617 <span style="color:green">acyl-CoA hydrolase activity</span>) |

N.B. The protein should also have an annotation to the activity term. Note also that the evidence code used for the peroxisome fission annotation is IDA since there was direct experimental evidence for this process in the paper, however the dependency of the process on the function was determined by using a mutant version: this detail cannot be captured in the current annotation format.

**3. Two proteins required for an activity:**

Statement from paper:

*To test the RuvA and RuvB proteins for DNA helicase activity, we used a simple gel electrophoretic assay which measures the displacement of a short 32P-labeled oligonucleotide (66nt long) from single-stranded circular omegaX174 DNA. Purified RuvA and RuvB catalyzed the unwinding of the oligonucleotide from the single-stranded circle (Fig.1,lane e). Neither RuvA (lanes c and d) nor RuvB (lanes f and g) alone were capable of unwinding, even at much higher protein concentrations.*

| Gene Name (col 2)                            | GO ID (col 5)                                                                     | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                         |
|----------------------------------------------|-----------------------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------------|
| P0A809 <span style="color:green">ruvA</span> | <GO:0004003> <span style="color:green">ATP-dependent DNA helicase activity</span> | <PMID:8433990>    | IDA              | dependent\_on(UniProtKB:P0A812 <span style="color:green">ruvB</span>) |

| Gene Name (col 2)                            | GO ID (col 5)                                                                     | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                         |
|----------------------------------------------|-----------------------------------------------------------------------------------|-------------------|------------------|-----------------------------------------------------------------------|
| P0A812 <span style="color:green">ruvB</span> | <GO:0004003> <span style="color:green">ATP-dependent DNA helicase activity</span> | <PMID:8433990>    | IDA              | dependent\_on(UniProtKB:P0A809 <span style="color:green">ruvA</span>) |

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

