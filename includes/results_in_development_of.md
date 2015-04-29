Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

Definition
----------

The relationship linking an entity and its participation in a process that changes it through time from the formation of the entity to the resultant mature state.

Identifies the cell, tissue, or anatomical entity which is under going the developmental process.

Child terms
-----------

-   None.

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
