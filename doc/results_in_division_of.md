Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

---------------Text extracted from ontology: DO NOT EDIT---------------

## results_in_division_of
* OWL ID: GOREL_0001019
* label: results_in_division_of
* synonyms
[]

### Definition
The relationship linking a entity and its participation in a process that results in the division of the entity into two entities of the same type.

### Usage
The relationship linking a entity and its participation in a process that results in the division of the entity into two entities of the same type.

### Subsets
[display_for_curators, AE_cell_or_anatomical]

##local domain
{u'BFO:0000007': u'BFO:0000007'}

## local range
{u'WBbt:0004017': u'Cell', u'CL:0000000': u'cell'}

---------------END AUTO GENERATED SECTION---------------




Comment
-------

Example of use: an annotation of gene X to cell division with results\_in\_division\_of CL:0000057 (fibroblast) means that at the end of the process a single fibroblast has divided into two fibroblasts.

Annotation Extension Usage Examples
-----------------------------------

**1. Gata3 is required for reactive proliferation of radial glial cells in telencephalon of adult zebrafish**

Paper: "Regenerative Neurogenesis from Neural Progenitor Cells Requires Injury-Induced Expression of Gata3" (PMID: 23168169)

Statement from paper: *"... knocking down gata3 reduces the number of injury-stimulated proliferation [of radial glial cells] at 3pdl significantly, to the level characteristic for unlesioned telencephalon."*

|          | Gene Name (col 2) | GO ID (col 5)                                                              | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                      | Parent terms of new folded GO term                                                                                                          |
|----------|-------------------|----------------------------------------------------------------------------|-------------------|------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded | Q91428 Gata3      | <GO:0008284> positive regulation of cell proliferation                     | PMID: 23168169    | IMP              | results\_in\_division\_of (CL:0013000 forebrain radial glial cell) |
| Folded   | Q91428 Gata3      | New GO ID positive regulation of forebrain radial glial cell proliferation | PMID: 23168169    | IMP              |                                                                    | is\_a new GO: positive regulation of radial glial cell proliferation, is\_a child of <GO:0008284> positive regulation of cell proliferation |

**OWL class expression:** <GO:0008284> <span style="color:red">positive regulation of cell proliferation</span> results\_in\_division\_of SOME CL:0013000 <span style="color:red">forebrain radial glial cell</span>

**2. Pax6a and Pax6b are required during neuronal progenitor proliferation in retina of adult zebrafish**

Paper: "Pa6a and Paxb are required at different points in neuronal progenitor cell proliferation during zebrafish photoreceptor regeneration" (PMID: 20152834)

Statement from paper: *"...knockdown of Pax6b expression inhibited the subsequent division of the MÃÂÃÂÃÂÃÂ¼ller glia-derived INL neuronal progenitor. In contrast, reduction of Pax6a expression allowed this initial neuronal progenitor cell division, but it prevented later cell divisions."*

|          | Gene Name (col 2) | GO ID (col 5)                                                          | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                  | Parent terms of new folded GO term                           |
|----------|-------------------|------------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------|--------------------------------------------------------------|
| Unfolded | P26630 Pax6a      | <GO:0008284> positive regulation of cell proliferation                 | PMID: 20152834    | IMP              | results\_in\_division\_of (CL:0002672 retinal progenitor cell) |
| Folded   | P26630 Pax6a      | New GO ID positive regulation of retinal progenitor cell proliferation | PMID: 20152834    | IMP              |                                                                | is\_a <GO:0008284> positive regulation of cell proliferation |

**OWL class expression:** <GO:0008284> <span style="color:red">positive regulation of cell proliferation</span> results\_in\_division\_of SOME CL:0002672 <span style="color:red">retinal progenitor cell</span>

|          | Gene Name (col 2) | GO ID (col 5)                                                          | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                  | Parent terms of new folded GO term                           |
|----------|-------------------|------------------------------------------------------------------------|-------------------|------------------|----------------------------------------------------------------|--------------------------------------------------------------|
| Unfolded | Q6DHA8 Pax6b      | <GO:0008284> positive regulation of cell proliferation                 | PMID: 20152834    | IMP              | results\_in\_division\_of (CL:0002672 retinal progenitor cell) |
| Folded   | Q6DHA8 Pax6b      | New GO ID positive regulation of retinal progenitor cell proliferation | PMID: 20152834    | IMP              |                                                                | is\_a <GO:0008284> positive regulation of cell proliferation |

**OWL class expression:** <GO:0008284> <span style="color:red">positive regulation of cell proliferation</span> results\_in\_division\_of SOME CL:0002672 <span style="color:red">retinal progenitor cell</span>

------------------------------------------------------------------------

Back to [Annotation usage examples for each annotation extension relation](http://wiki.geneontology.org/index.php/Annotation_usage_examples_for_each_annotation_extension_relation)

<Category:relations> [Category:annotation extension](Category:annotation extension "wikilink")
