Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## results_in_morphogenesis_of
* OWL ID: RO_0002298
* label: results in morphogenesis of
* synonyms
[]

### Definition
The relationship that links an entity with the process that results in the formation and shaping of that entity over time from an immature to a mature state.

### Usage
The relationship that links an entity with the process that results in the formation and shaping of that entity over time from an immature to a mature state.

### Comment
Example of use: an annotation of gene X to cell morphogenesis with results_in_morphogenesis_of CL:0000540 (neuron) means that at the end of the process an input neuron has attained its shape.

### Subsets
[display_for_curators, AE_cellular_component, AE_cell_or_anatomical]

##local domain
{u'BFO:0000015': u'process'}

## local range
{u'GO:0005575': u'cellular_component', u'WBbt:0004017': u'Cell', u'WBbt:0005766': u'Anatomy', u'UBERON:0001062': u'anatomical entity', u'PO:0025131': u'plant anatomical entity', u'CL:0000000': u'cell'}

---------------END AUTO GENERATED SECTION---------------

Annotation Extension Usage Examples
--

=== Enhancing Molecular Function and Biological Process Annotations ===

==== Specifying the cell or tissue type which are under going the morphogenic process ====

'''1. A protein's involvement in changing a particular cell's shape:'''

Statement from paper:

''Eotaxin, eotaxin-2, and MCP-4 were the most potent inducers of eosinophil shape change, followed by MCP-3, while MCP-1 and IL-8 were inactive. MCP-4 alone showed a bell-shaped eosinophil dose-response curve over the dose range tested. Eotaxin and eotaxin-2 were inactive on monocytes (Fig. 2⇓B), whereas MCP-1, -3, and -4 all induced monocyte shape change, with MCP-3 exhibiting the highest potency.''

{| class="wikitable" border="1"
|-
! Gene Name (col 2)
! GO ID (col 5)
! Reference (col 6)
! Evidence (col 7)
! Annotation Extension (col 16)
|-
| Q99616  <span style="color:green">MCP4</span>
| GO:0008360 <span style="color:green">regulation of cell shape</span>
| PMID:10072545
| IDA
| results_in_morphogenesis_of(CL:0000771 <span style="color:green">eosinophil</span>) 'pipe' results_in_morphogenesis_of(CL:0000576 <span style="color:green">monocyte</span>)
|}

Note the use of the pipe to create a multiple annotation extensions. The interpretation of this annotation is MCP4 is involved in the regulation of eosinophil cell shape and monocyte cell shape. 

More examples of this usage of occurs_in can be found on the documentation page for [[Column_16:_Cell_Type]]











Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)
