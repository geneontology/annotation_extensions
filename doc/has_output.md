Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
---------------Text extracted from ontology: DO NOT EDIT---------------

## has_output
* OWL ID: RO_0002234
* label: has output
* synonyms
[]

### Definition
p has output c iff c is a participant in p, c is present at the end of p, and c is not present at the beginning of p.

### Usage
Identifies an entity that is changed or created after participation in a molecular function or biological process

### Comment
Previous definition "p has_output c if c participates_in p at  the end of p and c is in some way changed by p or created by p." []

### Subsets
[AE_sequence_or_complex, ro-eco, AE_chemical, display_for_curators]

##local domain
BFO:0000015 : process

## local range
CHEBI:24431 : chemical entity; CHEBI:33697 : ribonucleic acid; GO:0032991 : macromolecular complex; MI:0315 : protein complex; PR:000000001 : protein; SO:0000673 : transcript; SO:0000704 : gene

---------------END AUTO GENERATED SECTION---------------



















Comment
-------

[**More details on the limited use of has\_output with biological process annotations**](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_participant.md)

Annotation Extension Usage Examples
-----------------------------------

**1. FGF production in response to stimulation of protein A**

| Gene Name (col 2) | GO ID (col 5) | Reference (col 6)                                                                 | Evidence (col 7) | Annotation Extension (col 16)                                       |
|-------------------|---------------|-----------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------|
| Pxxxx             | Protein A     | <GO:0090269> <span style="color:green">fibroblast growth factor production</span> | <PMID:xxx>       | has\_output (UniProt:Q9GZV9 <span style="color:green">FGF23</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship has\_output
----------------------------------------------------------------------------------------------------------------------------

**1. FGF production in response to stimulation of protein A**

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                                   | Reference (Col 6) | Extension (Col 16)                                                  | Parent terms for new folded GO term                                                   |
|-----------------|------------|----------------|-------------------------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Unfolded        | Pxxxx      | Protein A      | <GO:0090269> <span style="color:green">fibroblast growth factor production</span>               | <PMID:xxx>        | has\_output (UniProt:Q9GZV9 <span style="color:green">FGF23</span>) |                                                                                       |
| Folded          | Pxxxx      | Protein A      | New GO term <span style="color:green">FGF23 fibroblast growth factor cytokine production</span> | <PMID:xxx>        |                                                                     | is\_a <GO:0090269> <span style="color:red">fibroblast growth factor production</span> |
||

**OWL class expression:** <GO:0090269> <span style="color:red">fibroblast growth factor production</span> AND has\_output SOME UniProt:Q9GZV9 <span style="color:red">FGF23</span>

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

