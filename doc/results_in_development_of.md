Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

---------------Text extracted from ontology: DO NOT EDIT---------------

## results_in_development_of
* OWL ID: RO_0002296
* label: results in development of
* synonyms
[]

### Definition
p 'results in development of' c if and only if p is a developmental process and p results in the state of c changing from its initial state as a primordium or anlage through its mature state and to its final state.

### Usage
The relationship linking an entity and its participation in a process that changes it through time from the formation of the entity to the resultant mature state.

### Comment
Example of use: an annotation of gene X to cell development with results_in_development_of CL:0000540 (neuron) means that gene x is involved in a process where a cell that has an identity of a neuron has gone through a progression from its formation to the resulting mature neuron.

### Subsets
[display_for_curators, AE_cellular_component, AE_cell_or_anatomical]

##local domain
{u'BFO:0000007': u'BFO:0000007'}

## local range
{u'GO:0005575': u'cellular_component', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'CL:0000000': u'cell'}

---------------END AUTO GENERATED SECTION---------------









Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the cell or tissue type which are under going the developmental process

**1. Development of a particular tissue:**

Statement from paper:

*Periostin is critically required for maintenance of the integrity of the periodontal ligament..*

| Gene Name (col 2)                                 | GO ID (col 5)                                                    | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                  |
|---------------------------------------------------|------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------------------|
| MGI:1926321<span style="color:green">Postn</span> | <GO:0009888> <span style="color:green">tissue development</span> | <PMID:16314533>   | IMP              | results\_in\_development\_of(MA:0002467 <span style="color:green">periodontal ligament</span>) |

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship results\_in\_development\_of
----------------------------------------------------------------------------------------------------------------------------------------------------------

**1. Differentiation of a particular cell type:**

| Folded/unfolded | Gene Name (col 2)                                  | GO ID (col 5)                                                                | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                    | Parent terms of new folded GO term                       |
|-----------------|----------------------------------------------------|------------------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------------------|----------------------------------------------------------|
| Unfolded        | MGI:1926321 <span style="color:green">Postn</span> | <GO:0009888> <span style="color:green">tissue development</span>             | <PMID:16314533>   | IMP              | results\_in\_development\_of(CL:0000540 <span style="color:green">neuron</span>) |                                                          |
| Folded          | MGI:1926321 <span style="color:green">Postn</span> | New GO ID <span style="color:green"> periodontal ligament development</span> | <PMID:16314533>   | IMP              |                                                                                  | is\_a <span style="color:red"> tissue development</span> |

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
