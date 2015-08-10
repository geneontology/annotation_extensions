Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html )

---------------Text extracted from ontology: DO NOT EDIT---------------

## occurs_in
* OWL ID: BFO_0000066
* label: occurs in
* synonyms
[u'in']

### Definition
b occurs_in c =def b is a process and c is a material entity or immaterial entity& there exists a spatiotemporal region r and b occupies_spatiotemporal_region r.& forall(t) if b exists_at t then c exists_at t & there exist spatial regions s and sâ where & b spatially_projects_onto s at t& c is occupies_spatial_region sâ at t& s is a proper_continuant_part_of sâ at t

### Usage
Identifies the cell, tissue, cellular component or anatomical entity within which all parts of the molecular function or biological process occurs

### Comment
Paraphrase of definition: a relation between a process and an independent continuant, in which the process takes place entirely within the independent continuant

### Subsets
[AE_cell_or_anatomical, AE_cellular_component, display_for_curators]

##local domain
BFO:0000015 : process

## local range
CL:0000000 : cell; GO:0005575 : cellular_component; PO:0025131 : plant anatomical entity; UBERON:0001062 : anatomical entity; WBbt:0004017 : Cell; WBbt:0005766 : Anatomy

---------------END AUTO GENERATED SECTION---------------



















Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the cell or tissue type in which a process happens

**1. Differentiation of a particular cell type:**

Statement from paper:

*REN promoted neuronal differentiation of neural committed progenitor cells of CNS (ST14A cells, Fig. 7 A) or PNS (N2a cells, Fig. 7 B) origin.*

More examples of this usage of occurs\_in can be found on the documentation page for [Column\_16:\_Cell\_Type](Column_16:_Cell_Type "wikilink")

#### Specifying the subcellular location in which a process happens

1. **Protein interaction in a particular location in the cell:**

Statement from paper:

*Canine cardiac junctional SR vesicles were solubilized with 2% Triton X-100 and loaded on the affinity column equilibrated in EGTA-containing buffer (Fig.1). Calsequestrin-binding proteins were then eluted in buffer containing 20 mm CaCl2, a calcium concentration sufficient to disrupt all calsequestrin protein-binding interactions. Immunoblotting of the eluted fractions with triadin antibody revealed that triadin bound completely to the column and was eluted as a discrete peak in Ca2+-containing buffer (Fig. 1 A, upper)*

| Gene Name (col 2)                             | GO ID (col 5)                                                 | Reference (col 6) | Evidence (col 7) | With (col 8)                                 | Annotation Extension (col 16)                                                  |
|-----------------------------------------------|---------------------------------------------------------------|-------------------|------------------|----------------------------------------------|--------------------------------------------------------------------------------|
| P12637 <span style="color:green">CASQ2</span> | <GO:0005515> <span style="color:green">protein binding</span> | <PMID:9287354>    | IPI              | P82179 <span style="color:green">TRDN</span> | occurs\_in(GO:0016529 <span style="color:green">sarcoplasmic reticulum</span>) |

2. **Sequestering of calcium ion at a particular location in the cell:**

Statement from paper:

*To characterize the effects of the new CASQ2 mutations on SR Ca2+ handling in vivo, we performed experiments in adult rat ventricular myocytes infected with adenoviral constructs. Caffeine (10 mmol/L) was applied to myocytes expressing either WT or mutant CASQ2 to evaluate the SR Ca2+-storing capacity by measurement of fluo-3 fluorescence and of Na+/Ca2+ exchange current (INCX; Figure 4A; Table 1).21 Expression of WT increased the SR Ca2+ content by 50%, whereas CASQ2 G112+5X reduced the SR content, not only as compared with WT expression but also as compared with native cells (Ad-control).*

| Gene Name (col 2)                             | GO ID (col 5)                                                             | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                               |
|-----------------------------------------------|---------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O14958 <span style="color:green">CASQ2</span> | <GO:0051208> <span style="color:green">sequestering of calcium ion</span> | <PMID:16908766>   | IMP              | occurs\_in(GO:0016529 <span style="color:green">sarcoplasmic reticulum</span>), occurs\_in(CL:0000746 <span style="color:green">cardiac muscle cell</span>) |

Note the use of the comma to create a compound annotation extension. The interpretation of this annotation is CASQ2 is involved in sequestering calcium ions in the sarcoplasmic reticulum of cardiac muscle cell.

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship occurs\_in
----------------------------------------------------------------------------------------------------------------------------------------

**2. A protein's involvement in changing a particular cell's shape:**

#### Specifying the subcellular location in which a process happens

1. **Protein interaction in a particular location in the cell:**

Statement from paper:

*Canine cardiac junctional SR vesicles were solubilized with 2% Triton X-100 and loaded on the affinity column equilibrated in EGTA-containing buffer (Fig.1). Calsequestrin-binding proteins were then eluted in buffer containing 20 mm CaCl2, a calcium concentration sufficient to disrupt all calsequestrin protein-binding interactions. Immunoblotting of the eluted fractions with triadin antibody revealed that triadin bound completely to the column and was eluted as a discrete peak in Ca2+-containing buffer (Fig. 1 A, upper)*

| Folded/unfolded | Gene Name (col 2)                             | GO ID (col 5)                                                 | Reference (col 6) | Evidence (col 7) | With (col 8)                                 | Annotation Extension (col 16)                                                  | Parent terms of new folded GO term                    |
|-----------------|-----------------------------------------------|---------------------------------------------------------------|-------------------|------------------|----------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------|
| Unfolded        | P12637 <span style="color:green">CASQ2</span> | <GO:0005515> <span style="color:green">protein binding</span> | <PMID:9287354>    | IPI              | P82179 <span style="color:green">TRDN</span> | occurs\_in(GO:0016529 <span style="color:green">sarcoplasmic reticulum</span>) |                                                       |
| Folded          | P12637 <span style="color:green">CASQ2</span> | <GO:0005515> <span style="color:green">protein binding</span> | <PMID:9287354>    | IPI              | P82179 <span style="color:green">TRDN</span> |                                                                                | <span style="color:red">No new GO term created</span> |

**OWL class expression:** <GO:0005515> <span style="color:red">protein binding</span> occurs\_in SOME <GO:0016529> <span style="color:red">sarcoplasmic reticulum</span>

2. **Sequestering of calcium ion at a particular location in the cell:**

Statement from paper:

*To characterize the effects of the new CASQ2 mutations on SR Ca2+ handling in vivo, we performed experiments in adult rat ventricular myocytes infected with adenoviral constructs. Caffeine (10 mmol/L) was applied to myocytes expressing either WT or mutant CASQ2 to evaluate the SR Ca2+-storing capacity by measurement of fluo-3 fluorescence and of Na+/Ca2+ exchange current (INCX; Figure 4A; Table 1).21 Expression of WT increased the SR Ca2+ content by 50%, whereas CASQ2 G112+5X reduced the SR content, not only as compared with WT expression but also as compared with native cells (Ad-control).*

| Folded/unfolded | Gene Name (col 2)                             | GO ID (col 5)                                                                                                             | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                               | Parent terms of new folded GO term                                                                                                                                                                                                                                                         |
|-----------------|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | O14958 <span style="color:green">CASQ2</span> | <GO:0051208> <span style="color:green">sequestering of calcium ion</span>                                                 | <PMID:16908766>   | IMP              | occurs\_in(GO:0016529 <span style="color:green">sarcoplasmic reticulum</span>), occurs\_in(CL:0000746 <span style="color:green">cardiac muscle cell</span>) |                                                                                                                                                                                                                                                                                            |
| Folded          | O14958 <span style="color:green">CASQ2</span> | New GO term <span style="color:green">sequestering of calcium ion in sarcoplasmic reticulum</span>                        | <PMID:16908766>   | IMP              |                                                                                                                                                             | is\_a <GO:0016529> <span style="color:red">sequestering of calcium ion</span>                                                                                                                                                                                                              |
| Folded          | O14958 <span style="color:green">CASQ2</span> | New GO term <span style="color:green">sequestering of calcium ion in cardiac muscle cell</span>                           | <PMID:16908766>   | IMP              |                                                                                                                                                             | is\_a <GO:0016529> <span style="color:red">sequestering of calcium ion</span>                                                                                                                                                                                                              |
| Folded          | O14958 <span style="color:green">CASQ2</span> | New GO term <span style="color:green">sequestering of calcium ion in sarcoplasmic reticulum of cardiac muscle cell</span> | <PMID:16908766>   | IMP              |                                                                                                                                                             | is\_a <GO:0016529> <span style="color:red">sequestering of calcium ion</span>, is\_a New GO term <span style="color:red">sequestering of calcium ion in sarcoplasmic reticulum</span>, is\_a New GO term <span style="color:red">sequestering of calcium ion in cardiac muscle cell</span> |

**OWL class expression:** <GO:0016529> <span style="color:red">sequestering of calcium ion</span> occurs\_in SOME <GO:0016529> <span style="color:red">sarcoplasmic reticulum</span>

**OWL class expression:** <GO:0016529> <span style="color:red">sequestering of calcium ion</span> occurs\_in SOME CL:0000746 <span style="color:red">cardiac muscle cell</span>

**OWL class expression:** <GO:0016529> <span style="color:red">sequestering of calcium ion</span> occurs\_in SOME ( CL:0000746 <GO:0016529> <span style="color:red">sarcoplasmic reticulum</span> AND part\_of SOME <span style="color:red">cardiac muscle cell</span>

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
