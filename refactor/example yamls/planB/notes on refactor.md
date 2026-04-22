03/10/26 

These notes follow a recent chat with Yuri as well as the stale comments from Montana on [!MR11](https://gitlab.pnnl.gov/MoNET/analysis-api-schema/-/merge_requests/11).

**These have been reflected in [core-planB.yaml](https://gitlab.pnnl.gov/MoNET/analysis-api-schema/-/blob/schema_v2/refactor/example%20yamls/planB/core-planB.yaml)**

General design princples for Data Model upgrades:

- Use slots in lieu of attributes for nearly all cases, except for UUIDs
- implement inheritance via is_a relationships, not via class inheritance
- abstract DataProduct class
- rename workflowExecutionActivity to dataProcessingActivity
- rename analysisActivity to dataGenerationActivity
- analysisAct & processedData should also be abstract=TRUE: "the guiding principle will be to maintain high-level classes as abstract classes, including sampling activity, sample processing, data generation, and data processing activities, along with their respective entities."
- everything should be minimal e.g. enumerated timepoints on sub-activities, not master
- campaign table is too specific. instead have a nullable field with some sort of name on sampling activity ('EMSL_activity'?)


# DISCUSSION POINTS
- ingestion validation scripts - should we revisit given new product classes?
- should sample/processedSample have a master Entity class?

# HIGH LEVEL SUMMARY OF CHANGES/ADDITIONS 
- workflowExecutionActivity with self-ref FK called parent_workflow_id to facilitate chaining
- analysisActivity gets sequence_order to track order of events. timepoint label on subclassed activities as appropriate.
- linkage_cache is a new table that acts as a "ledger" of events. can link any of 'sample' | 'processedSample' |  'workflowExecutionActivity' | 'processedData', except sample-to-sample.
    - this is complementary to processingSampleLink, which records direct processing relationships (single hop parent to child). Both are required but serve different purposes
    - linkage_cache can be refreshed upon ingest to traverse segmental processingSamplelInk chains
- as a reminder, sample = Original physical material that comes in the door (e.g., soil core, mixed culture); processedSample - Any derivative physical material created through processing
