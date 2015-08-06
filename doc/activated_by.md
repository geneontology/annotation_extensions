Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
---------------Text extracted from ontology: DO NOT EDIT---------------

## activated_by
* OWL ID: GOREL_0000507
* label: activated_by
* synonyms
[u'activated by', u'activated_by_chemical', u'activated_by_substance', u'activity_increased_by']

### Definition


### Usage
Identifies a chemical substance that increases the activity of the gene product.

### Comment
This relation should not be used to annotate one gene product regulating another's activity; a regulator MF or regulation BP should be used in such cases.

### Subsets
[display_for_curators, AE_chemical]

##local domain
{u'GO:0003674': u'molecular_function'}

## local range
{u'CHEBI:24431': u'chemical entity'}

---------------END AUTO GENERATED SECTION---------------













Comment
-------

This relation should not be used to annotate one gene product regulating another's activity; a regulator Molecular Function or regulation Biological Process should be used in such cases.

Annotation Extension Usage Examples
-----------------------------------

### Specifying that a gene product is activated by a specific chemical

1. zinc activated ligand-gated ion channel (ZACN) is activated by Zn2+, <PMID:12381728>

So the annotation would be:

| DB (Col 2) | Object (Col 3) | GO ID (Col 5) | Reference (Col 6) | Extension (Col 16)                     |
|------------|----------------|---------------|-------------------|----------------------------------------|
| Q401N2     | ZACN           | <GO:0015276> ligand-gated ion channel activity | <PMID:12381728>   | activated\_by (ChEBI:29105, zinc ions) |
||

Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship activated\_by
------------------------------------------------------------------------------------------------------------------------------

1. zinc activated ligand-gated ion channel (ZACN) is activated by Zn2+, <PMID:12381728>

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                                                                   | Reference (Col 6) | Extension (Col 16)                                                      | Parent terms for new folded GO term                                                 |
|-----------------|------------|----------------|---------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Unfolded        | Q401N2     | ZACN           | <GO:0015276> <span style="color:green">ligand-gated ion channel activity</span> | <PMID:12381728>   | activated\_by (ChEBI:29105, <span style="color:green">zinc ions</span>) |                                                                                     |
| Folded          | Q401N2     | ZACN           | New GO term <span style="color:green">zinc-gated ion channel activity</span>    | <PMID:12381728>   |                                                                         | is\_a <GO:0048471> <span style="color:red">ligand-gated ion channel activity</span> |
||

**OWL class expression:** <GO:0015276> <span style="color:red">ligand-gated ion channel activity</span> AND activated\_by SOME ChEBI:29105 <span style="color:red">zinc ions</span>

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink") [Category:LEGO examples](Category:LEGO examples "wikilink")
