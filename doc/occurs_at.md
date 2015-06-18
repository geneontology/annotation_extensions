Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

## Text extracted from ontlogy: DO NOT EDIT
* OWL ID: GOREL_0000501
* shorthand: occurs_at
* label: occurs at

### Definition


### Usage
Identifies the Cellular Component or sequence feature adjacent to or in the vicinity of which the Molecular Function or Biological Process is executed

### Subsets
[display_for_curators, AE_cellular_component, AE_sequence_feature]

### synonyms
[]

##local domain
{u'BFO:0000007': u'BFO:0000007'}

## local range
{u'GO:0005575': u'cellular_component', u'SO:0000110': ''}

---------------END AUTO GENERATED SECTION---------------


Annotation Extension Usage Examples
-----------------------------------

**Specifying the sequence feature at which chromatin silencing occurs:**

Statement from paper:

*Mutation of hip3+ alleviates transcriptional silencing at several heterochromatic loci, including in the outer (otr) centromeric repeats, indicating that Hip3 is required for the integrity of pericentric heterochromatin...deletion of hip3+ in this background resulted in the formation of light pink colonies, demonstrating that transcriptional silencing in the otr centromeric repeats is reduced, indicating that Hip3 is required for the integrity of pericentric heterochromatin (Fig. 7A).*

| Gene Name (col 2)                                   | GO ID (col 5)                                                                   | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                   |
|-----------------------------------------------------|---------------------------------------------------------------------------------|-------------------|------------------|-------------------------------------------------------------------------------------------------|
| SPBC31F10.14c <span style="color:green">hip3</span> | <GO:0030702> <span style="color:green">chromatin silencing at centromere</span> | <PMID:16428807>   | IDA              | occurs\_at(SO:0001799 <span style="color:green">regional centromere outer repeat region</span>) |

**Endocytosis in S. pombe occurs at the cell division site:**

Statement from paper:

*We also investigated the relationship of equatorial endocytosis to the exocyst, a complex of proteins associated with exocytosis that has a specific role in cytokinesis in fission yeast (Wang et al., 2002)...We therefore added FM4-64 to sec8-1 labelled with DAPI and scored the percentage of cells showing FM4-64 fluorescence between the dividing nuclei at both the permissive and restrictive temperatures. Equatorial endocytosis was inhibited in this mutant (Fig. 8A), although endocytosis at the cell poles was apparently normal (data not shown)... Thus, endocytosis at the division plane may serve to balance exocytosis specifically at this site and at this stage of the cell cycle.*

| Gene Name (col 2)                                | GO ID (col 5)                                             | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                              |
|--------------------------------------------------|-----------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------------|
| SPCC970.09 <span style="color:green">sec8</span> | <GO:0006897> <span style="color:green">endocytosis</span> | <PMID:16141239>   | IMP              | occurs\_at(GO:0032153 <span style="color:green">cell division site</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship occurs\_at
---------------------------------------------------------------------------------------------------------------------------

**Endocytosis in S. pombe occurs at the cell division site:**

Statement from paper:

*We also investigated the relationship of equatorial endocytosis to the exocyst, a complex of proteins associated with exocytosis that has a specific role in cytokinesis in fission yeast (Wang et al., 2002)...We therefore added FM4-64 to sec8-1 labelled with DAPI and scored the percentage of cells showing FM4-64 fluorescence between the dividing nuclei at both the permissive and restrictive temperatures. Equatorial endocytosis was inhibited in this mutant (Fig. 8A), although endocytosis at the cell poles was apparently normal (data not shown)... Thus, endocytosis at the division plane may serve to balance exocytosis specifically at this site and at this stage of the cell cycle.*

| Folded/unfolded | DB (Col 2)                                       | GO ID (Col 5)                                                                   | Reference (Col 6) | Extension (Col 16)                        | Parent terms for new folded GO term                           |
|-----------------|--------------------------------------------------|---------------------------------------------------------------------------------|-------------------|-------------------------------------------|---------------------------------------------------------------|
| Unfolded        | SPCC970.09 <span style="color:green">sec8</span> | <GO:0006897> <span style="color:green">endocytosis</span>                       | <PMID:16141239>   | occurs\_at(GO:0032153 cell division site) |                                                               |
| Folded          | SPCC970.09 <span style="color:green">sec8</span> | new GO term <span style="color:green">endocytosis at cell division site </span> | <PMID:16141239>   |                                           | is\_a <GO:0006897> <span style="color:red">endocytosis</span> |
||

**OWL class expression:** <GO:0006897> <span style="color:red">endocytosis</span> occurs\_at SOME <GO:0032153> <span style="color:red">cell division site</span>

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink") <Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
