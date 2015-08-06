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
[display_for_curators, AE_sequence_or_complex]

##local domain
{u'GO:0031647': u'regulation of protein stability'}

## local range
{u'SO:0000704': u'gene', u'PR:000000001': u'protein', u'GO:0032991': u'macromolecular complex', u'CHEBI:33697': u'ribonucleic acid', u'MI:0315': u'protein complex', u'SO:0000673': u'transcript'}

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
