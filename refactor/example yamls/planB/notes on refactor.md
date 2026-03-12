03/10/26 Notes from chat with Yuri
**These have been reflected in core-planB.yaml**
General design princples for Data Model upgrades:

- Use slots in lieu of attributes for nearly all cases, except for UUIDs
- implement inheritance via is_a relationships, not via class inheritance
- abstract DataProduct class
- rename workflowExecutionActivity to dataProcessingActivity
- rename analysisActivity to dataGenerationActivity
- analysisAct & processedData should also be abstract
- everything should be minimal e.g. enumerated timepoints on sub-activities, not master
- campaign table is too specific. instead have a nullable field with some sort of name on sampling activity ('EMSL_activity'?)