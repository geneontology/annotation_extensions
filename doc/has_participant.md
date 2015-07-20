## Definition

Identifies an entity affected by the gene product's participation in a molecular function or biological process 

Comment
-------

**Do not use this relation directly in annotation. Instead use one of the child terms.**

**Limited use of has\_participant child relationships with biological process annotations**

Basically, a single protein (or biological entity) cannot be the input for a pathway/multi-step biological process (e.g. a BP representing a series of molecular functions such as mitophagy etc). A single protein (entity) can be the input for a biological process where a specific protein (entity) is being metabolized/modified/transported etc, e.g. protein phosphorylation' (GO:0006468).

You may want to capture that another protein (entity) is involved (or even the direct target) in the process. However, the Annotation Extension field extends the annotated GO term itself. Therefore, the GO term extended needs to describe a process happening to a protein or entity.

For example you cannot extend activation of mitophagy using has_input protein B. A way round this is: Either to request a more specific GO term: protein ubiquitination involved in activation of mitophagy. For this GO term you could then use has_input protein B. Because now you are specifying that ubiquitination of the protein is the focus of the process. And you would effectively be extending the annotation to protein ubiquitination (has_input protein B) involved in activation of mitophagy

Or another option is to create the annotation protein ubiquitination (has_input protein B, part_of activation of mitophagy)

Child terms
-----------

-   [has\_input](Annotation_Extension_Relation:has_input "wikilink")

<!-- -->

-   [has\_output](Annotation_Extension_Relation:has_output "wikilink")

<!-- -->

-   [has\_regulation\_target](Annotation_Extension_Relation:has_regulation_target "wikilink")

<!-- -->

-   [stabilizes](Annotation_Extension_Relation:stabilizes "wikilink")

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
