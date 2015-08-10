Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## in_absence_of
* OWL ID: GOREL_0000755
* label: in_absence_of
* synonyms
[]

### Definition
Identifies a chemical, gene product or complex in the absence of which an ontology term is observed to apply to the annotated gene product.

### Usage
Identifies a chemical, gene product or complex in the absence of which an ontology term is observed to apply to the annotated gene product.

### Comment
DEPRECATION WARNING: The GO editors have agreed that this relation should be deprecated. There are two main reasons for this 1. The relation does not extend the meaning of the GO term, as annotation relations are meant to, but instead specifies conditions under which the annotation is true. This can not be expressed in OWL. Annotation extensions using this relation will never fold. 2. The relation includes a hidden negation. This is problematic for a number of reasons, the most important of which is that burying negations in otherwise positive relationships can cause serious problems for inference.

### Subsets
[AE_sequence_or_complex, AE_chemical, display_for_curators]

##local domain
BFO:0000001 : entity

## local range
CHEBI:24431 : chemical entity; GO:0032991 : macromolecular complex; MI:0315 : protein complex; PR:000000001 : protein; SO:0000673 : transcript; SO:0000704 : gene

---------------END AUTO GENERATED SECTION---------------








Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)
