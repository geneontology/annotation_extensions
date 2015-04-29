Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

!INCLUDES "has_agent_inc.md"

Comment
-------

Synonyms
--------

has\_active\_participant

Child terms
-----------

-   None

Annotation Extension Usage Examples
-----------------------------------

1. Recording the cell type that is the agent in a secretion process

| Gene Name (col 2) | GO ID (col 5)                           | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)              |
|-------------------|-----------------------------------------|-------------------|------------------|--------------|--------------------------------------------|
| A2A7Q8            | <GO:0072643> interferon-gamma secretion |                   | ECO:0000315      |              | has\_agent(CL:0000623 natural killer cell) |

2. Recording the agent involved in a transport process

| Gene Name (col 2) | GO ID (col 5)                                               | Reference (col 6) | Evidence (col 7) | With (col 8) | Annotation Extension (col 16)            |
|-------------------|-------------------------------------------------------------|-------------------|------------------|--------------|------------------------------------------|
| F1PRN2            | <GO:0061502> early endosome to recycling endosome transport |                   | ECO:0000314      |              | has\_agent(GO:0005884; (actin filament)) |

(Question - could this be better recorded in the ontology?)

Using examples to demonstrate [Folding\_and\_Unfolding](Folding_and_Unfolding "wikilink") using the relationship has\_agent
---------------------------------------------------------------------------------------------------------------------------

| Folded/unfolded | DB (Col 2) | Object (Col 3) | GO ID (Col 5)                           | Reference (Col 6) | Extension (Col 16) | Parent terms for new folded GO term                        |
|-----------------|------------|----------------|-----------------------------------------|-------------------|--------------------|------------------------------------------------------------|
| Unfolded        |            | A2A7Q8         | <GO:0072643> interferon-gamma secretion |                   |                    | has\_agent(CL:0000623 natural killer cell)                 |
| Folded          |            | A2A7Q8         | ??                                      |                   |                    | is\_a <GO:0002370> natural killer cell cytokine production |
||

**OWL class expression:**

interferon-gamma secretion and has\_agent some 'naural killer cell'

------------------------------------------------------------------------

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:Relations> <Category:Reasoning> <Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
