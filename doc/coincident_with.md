Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
---------------Text extracted from ontology: DO NOT EDIT---------------

## coincident_with
* OWL ID: RO_0002008
* label: coincident with
* synonyms
[]

### Definition
A relation that holds between two linear structures that are approximately parallel to each other for their entire length and where either the two structures are adjacent to each other or one is part of the other.

### Usage
Use this relation to link a region of chromosome or chromatin to the sequence region that it contains.  The sequence region may be a specific gene or some generic region referred to by a SO term.

### Comment
Example: if we define region of chromosome as any subdivision of a chromosome along its long axis, then we can define a region of chromosome that contains only gene x as 'chromosome region' that coincident_with some 'gene x', where the term gene X corresponds to a genomic sequence.

### Subsets
[valid_for_annotation_extension, ro-eco, AE_cellular_component, display_for_curators]

##local domain
{u'GO:0005575': u'cellular_component'}

## local range
{u'CHEBI:24431': u'chemical entity', u'SO:0000001': u'region', u'SO:0000704': u'gene'}

---------------END AUTO GENERATED SECTION---------------

























Annotation Extension Usage Example
----------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)