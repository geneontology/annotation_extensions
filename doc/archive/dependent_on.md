Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Annotation Extension Usage Examples
-----------------------------------

**1. IAP2-dependent regulation of NF-kB activity:**

Statement from paper:

*To test whether RIP3 and RIP4 have to be ubiquitinated by cIAP1/2 in order to mediate NF-kB activation, we compared RIP-mediated NF-kB luciferase reporter activity when ectopically expressed in HEK293T cells in the presence or absence of the IAP inhibitor BV6, a treatment that induces rapid auto-ubiquitination and degradation of endogenous cIAP1/2[41]. As shown in Figure 4A, BV6 treatment greatly impaired TNF and RIP1âRIP4-induced NF-kB activation but had no impact on TAK1-mediated NF-kB induction (Figure 4A). Those results, which indicate that cIAP1/2 act upstream of TAK1, are consistent with a role for cIAP1/2 as E3 ligases regulating RIP1â4-mediated activation of NF-kB.*

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

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
