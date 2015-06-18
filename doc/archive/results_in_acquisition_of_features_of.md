Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDE

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the cell or tissue type which acquires new features following a specific process or function

**1. Differentiation of a particular cell type:**

Statement from paper:

*REN promoted neuronal differentiation of neural committed progenitor cells of CNS (ST14A cells, Fig. 7 A) or PNS (N2a cells, Fig. 7 B) origin.*

| Gene Name (col 2)                                | GO ID (col 5)                                                      | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                              |
|--------------------------------------------------|--------------------------------------------------------------------|-------------------|------------------|--------------------------------------------------------------------------------------------|
| MGI:2448712 <span style="color:green">Ren</span> | <GO:0030154> <span style="color:green">cell differentiation</span> | <PMID:12186855>   | IDA              | results in acquisition of features of (CL:0000540 <span style="color:green">neuron</span>) |

**2. A protein's involvement in changing a particular cell's shape:**

Statement from paper:

*Eotaxin, eotaxin-2, and MCP-4 were the most potent inducers of eosinophil shape change, followed by MCP-3, while MCP-1 and IL-8 were inactive. MCP-4 alone showed a bell-shaped eosinophil dose-response curve over the dose range tested. Eotaxin and eotaxin-2 were inactive on monocytes (Fig. 2âB), whereas MCP-1, -3, and -4 all induced monocyte shape change, with MCP-3 exhibiting the highest potency.*

| Gene Name (col 2)                            | GO ID (col 5)                                                          | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                                                    |
|----------------------------------------------|------------------------------------------------------------------------|-------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q99616 <span style="color:green">MCP4</span> | <GO:0008360> <span style="color:green">regulation of cell shape</span> | <PMID:10072545>   | IDA              | results in acquisition of features of(CL:0000771 <span style="color:green">eosinophil</span>) 'pipe' results in acquisition of features of(CL:0000576 <span style="color:green">monocyte</span>) |

Note the use of the pipe to create a multiple annotation extensions. The interpretation of this annotation is MCP4 is involved in the regulation of eosinophil cell shape and monocyte cell shape.

Using examples (from above) to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship results\_in\_acquisition\_of\_features\_of
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Specifying the cell or tissue type which acquires new features following a specific process

**1. Differentiation of a particular cell type:**

| Folded/unfolded | Gene Name (col 2)                                | GO ID (col 5)                                                           | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                  | Parent terms of new folded GO term                                      |
|-----------------|--------------------------------------------------|-------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Unfolded        | MGI:2448712 <span style="color:green">Ren</span> | <GO:0030154> <span style="color:green">cell differentiation</span>      | <PMID:12186855>   | IDA              | results\_in\_acquisition\_of\_features\_of(CL:0000540 <span style="color:green">neuron</span>) |                                                                         |
| Folded          | MGI:2448712 <span style="color:green">Ren</span> | New GO ID <span style="color:green"> neuron cell differentiation</span> | <PMID:12186855>   | IDA              |                                                                                                | is\_a <GO:0030154> <span style="color:red"> cell differentiation</span> |

**OWL class expression:** <GO:0005515> <span style="color:red">cell differentiation</span> results\_in\_acquisition\_of\_features\_of SOME CL:0000540 <span style="color:red">neuron</span>

**2. A protein's involvement in changing a particular cell's shape:**

Note the use of the pipe to create a multiple annotation extensions.

| Folded/unfolded | Gene Name (col 2)                            | GO ID (col 5)                                                                  | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                                                                                                              | Parent terms of new folded GO term                                         |
|-----------------|----------------------------------------------|--------------------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Unfolded        | Q99616 <span style="color:green">MCP4</span> | <GO:0008360> <span style="color:green">regulation of cell shape</span>         | <PMID:10072545>   | IDA              | results\_in\_acquisition\_of\_features\_of(CL:0000771 <span style="color:green">eosinophil</span>) 'pipe' occurs\_in(CL:0000576 <span style="color:green">monocyte</span>) |                                                                            |
| Folded          | Q99616 <span style="color:green">MCP4</span> | New GO ID <span style="color:green">regulation of eosinophil cell shape</span> | <PMID:10072545>   | IDA              |                                                                                                                                                                            | is\_a <GO:0008360> <span style="color:red">regulation of cell shape</span> |
| Folded          | Q99616 <span style="color:green">MCP4</span> | New GO ID <span style="color:green">regulation of monocyte cell shape</span>   | <PMID:10072545>   | IDA              |                                                                                                                                                                            | is\_a <GO:0008360> <span style="color:red">regulation of cell shape</span> |

**OWL class expression:** <GO:0008360> <span style="color:red">regulation of cell shape</span> results\_in\_acquisition\_of\_features\_of SOME CL:0000771 <span style="color:red">eosinophil</span> AND occurs\_in SOME CL:0000576 <span style="color:red">monocyte</span>

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
