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

-   [has\_input](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_input.md)
-   - [has\_direct\_input](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_direct_input.md)
-   - [stabilizes](https://github.com/geneontology/annotation_extensions/blob/master/doc/stabilizes.md)

<!-- -->

-   [has\_output](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_ouput.md)
-   -   [results\_in\_formation\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_formation_of.md)

<!-- -->

-   [has\_regulation\_target](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_regulation_target.md)

<!-- -->

-   [acts\_on\_population\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/acts_on_population_of.md)
-   [has\_agent](https://github.com/geneontology/annotation_extensions/blob/master/doc/has_agent.md)

<!-- -->
-   [results\_in_acquisition\_of\_features\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_acquisition_of_features_of.md)

<!-- -->
-   [results\_in\_development\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_development_of.md)

<!-- -->
-   [results\_in\_division\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_division_of.md)

<!-- -->
-   [results\_in\_maturation\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_maturation_of.md)

<!-- -->
-   [results\_in\_morphogenesis\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_morphogenesis_of.md)

<!-- -->
-   [results\_in\_movement\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/results_in_movement_of.md)

<!-- -->
-   [transports\_or\_maintains\_localization\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/transports_or_maintains_localization_of.md)

<!-- -->

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
