Usage
----------

The relationship that links an entity with a process in which the process has more than one participant that is of the same entity type.

{"gitdown": "include", "file": "USAGE_acts_on_population_of.md"}


Child terms
-----------

-   None.

Scope of use
------------

### Domain

<GO:0003674> (molecular\_function) or <GO:0008150> (biological\_process)

### Range

CL:0000000 (cell) or <GO:0005575> (cellular component) or WBbt:0004017 (cell)

Annotation Extension Usage Examples
-----------------------------------

**1. SEMA3A signals through NRP1 and PLXNA4 to guide the axons of facial visceromotor neurons:**

Statement from paper:

*Whilst axons formed normal projections in 5/5 Nrp2-null and 3/3 Sema3F-null mutants, we observed striking axon guidance errors in 5/5 Nrp1-null and 5/5 Sema3a-null mutants. Specifically, there was defasciculation and midline crossing of ectopic axons near Rathke's pouch, consistent with the idea that Sema3a normally provides repulsive cues for GSPN axons. Moreover, there was no arborisation in the area where the sphenopalatine ganglion forms; rather, some axons appeared to extend beyond the target area.*

| Gene Name (col 2)                              | GO ID (col 5)                                                            | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                            |
|------------------------------------------------|--------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------------|
| O08665 <span style="color:green">Sema3a</span> | <GO:0008045> <span style="color:green">motor neuron axon guidance</span> | <PMID:18804103>   | IMP              | acts\_on\_population of(CL:0005025 <span style="color:green">visceromotor neuron</span>) |

Using example (from above) to demonstrate [Folding\_and\_Unfolding][] using the relationship acts\_on\_population\_of
---------------------------------------------------------------------------------------------------------------------

**1. SEMA3A signals through NRP1 and PLXNA4 to guide the axons of facial visceromotor neurons:**

| Folded/unfolded | Gene Name (col 2)                              | GO ID (col 5)                                                                             | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                            | Parent terms of new folded GO term                                            |
|-----------------|------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Unfolded        | O08665 <span style="color:green">Sema3a</span> | <GO:0008045> <span style="color:green">motor neuron axon guidance</span>                  | <PMID:18804103>   | IMP              | acts\_on\_population of(CL:0005025 <span style="color:green">visceromotor neuron</span>) |                                                                               |
| Folded          | O08665 <span style="color:green">Sema3a</span> | New GO ID <span style="color:green">visceromotor neuron motor neuron axon guidance</span> | <PMID:18804103>   | IMP              |                                                                                          | is\_a <GO:0008045> <span style="color:red"> motor neuron axon guidance</span> |

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation][]

<Category:relations> [Category:annotation extension][]

  [Annotation usage examples for each annotation extension relation]: http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation
  [Folding\_and\_Unfolding]: Folding_and_Unfolding "wikilink"
  [Category:annotation extension]: Category:annotation extension "wikilink"
