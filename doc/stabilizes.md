Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## stabilizes
* OWL ID: GOREL_0000018
* label: stabilizes
* synonyms
[u'stabilizes']

### Definition
Identifies specific gene product stabilized in a protein stabilization process (or regulation thereof)

### Usage
Identifies specific gene product stabilized in a protein stabilization process (or regulation thereof)

### Comment


### Subsets
[AE_sequence_or_complex, display_for_curators]

##local domain
GO:0031647 : regulation of protein stability

## local range
CHEBI:33697 : ribonucleic acid; GO:0032991 : macromolecular complex; MI:0315 : protein complex; PR:000000001 : protein; SO:0000673 : transcript; SO:0000704 : gene

---------------END AUTO GENERATED SECTION---------------























Annotation Extension Usage Examples
-----------------------------------

| Gene Name (col 2) | GO ID (col 5)                                                       | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                          |
|-------------------|---------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------|
| PARK7             | <GO:0050821> <span style="color:green">protein stabilization</span> | <PMID:24947010>   | IDA              | stabilizes: UniProtKB:P63244 <span style="color:green"> GNB2L1 </span> |

Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship results\_in\_determination\_of
-----------------------------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                       | Reference (Col 6) | Extension (Col 16)                                                     | Parent terms for new folded GO term                     |
|-----------------|------------|----------------|---------------------------------------------------------------------|-------------------|------------------------------------------------------------------------|---------------------------------------------------------|
| Unfolded        | Q99497     | PARK7          | <GO:0050821> <span style="color:green">protein stabilization</span> | PMID: 24947010    | stabilizes: UniProtKB:P63244 <span style="color:green"> GNB2L1 </span> |                                                         |
| Folded          | Q99497     | PARK7          | <GO:0050821> <span style="color:green">protein stabilization</span> | PMID: 24947010    | stabilizes: UniProtKB:P63244 <span style="color:green"> GNB2L1 </span> | <span style="color:red"> No new GO term created </span> |
||

No new term will be created in this example because this is outside of the scope of GO.

**OWL class expression:** <GO:0050821> <span style="color:red">protein stabilization</span> AND stabilizes SOME UniProtKB:P63244 <span style="color:red">GNB2L1</span>

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
