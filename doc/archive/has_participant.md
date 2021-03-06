Comment
-------

**Do not use this relation directly in annotation. Instead use one of the child terms.**

**Limited use of has\_participant child relationships with biological process annotations**

Basically, a single protein (or biological entity) cannot be the input for a pathway/multi-step biological process (e.g. a BP representing a series of molecular functions such as âmitophagyâ etc). A single protein (entity) can be the input for a biological process where a specific protein (entity) is being metabolized/modified/transported etc, e.g. âprotein phosphorylation' (GO:0006468).

You may want to capture that another protein (entity) is involved (or even the direct target) in the process. However, the Annotation Extension field extends the âannotated GO termâ itself. Therefore, the GO term extended needs to describe a process happening to a protein or entity.

For example you cannot extend âactivation of mitophagyâ using âhas\_input protein Bâ. A way round this is: Either to request a more specific GO term: protein ubiquitination involved in activation of mitophagy. For this GO term you could then use âhas\_inputâ protein B. Because now you are specifying that ubiquitination of the protein is the focus of the process. And you would effectively be extending the annotation to âprotein ubiquitination (has\_input protein B) involved in activation of mitophagyâ.

Or another option is to create the annotation âprotein ubiquitination (has\_input protein B, part\_of activation of mitophagy)â.

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

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
