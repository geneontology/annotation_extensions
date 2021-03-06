Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)

---------------Text extracted from ontology: DO NOT EDIT---------------

## results_in_movement_of
* OWL ID: RO_0002565
* label: results in movement of
* synonyms
[]

### Definition
Holds between p and c when p is locomotion process and the outcome of this process is the change of location of c

### Usage
Use this relation to link a locomotion process to the type of cell or anatomical structure or organism that the process results in locomotion of.

### Comment
For movement of chemicals or cell parts, please use transports_or_maintains_localization_of

### Subsets
[valid_for_annotation_extension, AE_cell_or_anatomical, display_for_curators]

##local domain
{u'GO:0008150': u'biological_process'}

## local range
{u'CL:0000000': u'cell', u'WBbt:0004017': u'Cell'}

---------------END AUTO GENERATED SECTION---------------

























Comment
-------

Consider instead using [transports\_or\_maintains\_localization\_of](https://github.com/geneontology/annotation_extensions/blob/master/doc/transports_or_maintains_localization_of.md)

* Use results_in_movement_of for transport/movement of a cell or component
* Use the transports term for transport/movement of proteins and small molecules 

Annotation Extension Usage Examples
-----------------------------------

### Enhancing Molecular Function and Biological Process Annotations

#### Specifying the cell or cellular component which move in response to the gene product

**Cell adhesion molecule stimulates cell mobility**

Statement from paper:

*blood vessel epicardial substance (Bves) is critical for regulation of epicardial cell directional movement, as disruption of this interaction randomizes migratory patterns.*

| Gene Name (col 2)                            | GO ID (col 5)                                                                              | Reference (col 6) | Evidence (col 7) | Annotation Extension (col 16)                                                      |
|----------------------------------------------|--------------------------------------------------------------------------------------------|-------------------|------------------|------------------------------------------------------------------------------------|
| Q9ES83 <span style="color:green">Bves</span> | <GO:0060973> <span style="color:green">cell migration involved in heart development</span> | <PMID:24048452>   | IMP              | results\_in\_movement\_of (CL:0002494 <span style="color:green">cardiocyte</span>) |

Using examples to demonstrate [Folding\_and\_Unfolding](http://wiki.geneontology.org/index.php/Folding_and_Unfolding) using the relationship results\_in\_movement\_of
------------------------------------------------------------------------------------------------------------------------------------------

**Specifying that a gene product regulates the location of cardiocytes as part of heart development .** <PMID:24048452>

Statement from paper: blood vessel epicardial substance (Bves) is critical for regulation of epicardial cell directional movement, as disruption of this interaction randomizes migratory patterns.

| Folded/unfolded | DB (Col 2) | Object (Col 3)                        | GO ID (Col 5)                                                                                   | Reference (Col 6) | Extension (Col 16)                                                                 | Parent terms for new folded GO term                                                                                                                                                                                                                |
|-----------------|------------|---------------------------------------|-------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unfolded        | Q9ES83     | <span style="color:green">Bves</span> | <GO:0060973> <span style="color:green">cell migration involved in heart development</span>      | <PMID:24048452>   | results\_in\_movement\_of (CL:0002494 <span style="color:green">cardiocyte</span>) |                                                                                                                                                                                                                                                    |
| Folded          | Q9ES83     | <span style="color:green">Bves</span> | New GO term <span style="color:green">cardiocyte migration involved in heart development</span> | <PMID:24048452>   |                                                                                    | is\_a <GO:0060973> <span style="color:green">cell migration involved in heart development</span> AND is\_a New GO term <span style="color:green">cardiocyte migration</span> (parent <GO:0016477> <span style="color:green">cell migration</span>) |
||

**OWL class expression:** <GO:0060973> <font color = "red">cell migration involved in heart development</font> results\_in\_movement\_of SOME CL:0002494 <font color = "red">cardiocyte</font>

------------------------------------------------------------------------

Back to [index of relations docs](https://github.com/geneontology/annotation_extensions/tree/master/doc)

[QuickGO graph](http://www.ebi.ac.uk/QuickGO/AnnotationExtensionRelations.html)
