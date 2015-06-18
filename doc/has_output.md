Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

## Text extracted from ontlogy: DO NOT EDIT
* OWL ID: RO_0002234
* shorthand: has_output
* label: has output
### Definition
p has direct input c iff c is a participant in p, c is present at the end of p, and c is not present at the beginning of c.
### Usage
Identifies an entity that is changed or created after participation in a molecular function or biological process
### Subsets
[display_for_curators, AE_chemical, AE_sequence_or_complex, ro-eco]
### synonyms
[u'produces']
=== local domain ===
{u'BFO:0000007': u'BFO:0000007'}
=== local range ===
{u'SO:0000704': u'gene', u'PR:000000001': u'PR:000000001', u'GO:0032991': u'macromolecular complex', u'CHEBI:33697': u'ribonucleic acid', u'CHEBI:24431': u'chemical entity', u'MI:0315': u'protein complex', u'SO:0000673': u'transcript'}

---------------END AUTO GENERATED SECTION---------------


Comment
-------

[**More details on the limited use of has\_output with biological process annotations**](http://wiki.geneontology.org/index.php/Annotation_Extension_Relation:has_participant#Comment)

Annotation Extension Usage Examples
-----------------------------------

**1. FGF production in response to stimulation of protein A**

| Gene Name (col 2) | GO ID (col 5) | Reference (col 6)                                                                 | Evidence (col 7) | Annotation Extension (col 16)                                       |
|-------------------|---------------|-----------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------|
| Pxxxx             | Protein A     | <GO:0090269> <span style="color:green">fibroblast growth factor production</span> | <PMID:xxx>       | has\_output (UniProt:Q9GZV9 <span style="color:green">FGF23</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship has\_output
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

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink") [Category:LEGO examples](Category:LEGO examples "wikilink")
