Collecting workspace information# Schema Transition Gameplan: MONet Analysis-API to LinkML

## Executive Summary

This document outlines a 6-month incremental transition plan for FY26 from the current Flask/SQLAlchemy-based schema in [`analysis-api`](c:\Users\kapu336\Documents\MONet\analysis-api) to a LinkML-based schema architecture. The primary goals are to create extensible, interoperable metadata models that can synchronize user-submission metadata with backend systems while maintaining backward compatibility and enabling future integration with projects like AMP2.

Ideally this work would include consultation with CDO, LIMS and AMP2 teams with relevant campaigns.

## Current State Assessment

### Existing Architecture
- PostgreSQL database with complex enum types  
- Flask-based API with SQLAlchemy models
- Enrichment providers (e.g., `nasa_climate_provider.py`)
- Manual batch processing scripts (`batch_enrich.ps1`) and ingest

### LinkML Foundation
- Template repository: [`analysis-api-schema`](c:\Users\kapu336\Documents\MONet\analysis-api-schema)
- Poetry-based dependency management (`pyproject.toml`)
- Automated generation tools (Makefile, `justfile`)

---

## Month 1-2: Foundation & Discovery Phase

### Week 1-2: Schema Audit & Mapping
**Deliverables:**
- Complete audit of existing PostgreSQL schema from `backup-9-5-2025-modified.sql`
- Document all enum types (39 identified: `aerosoltype`, `sampletype`, `methodname`, etc.)
- Map existing table relationships and constraints
- Identify user-submission vs. backend-generated metadata boundaries

**Actions:**
```bash
# Extract schema structure
just _gen-project
make gen-project
```

### Week 3-4: LinkML Schema Bootstrap
**Deliverables:**
- Initial LinkML schema covering core entities: `Sample`, `SampleBase`, `ProcessedSample`
- Enum definitions for critical types (`sampletype`, `processedsampletype`, `samplebasetype`)
- Basic validation rules and constraints
- JSON scripts? User Metadata?

**Files to Create:**
- `src/analysis_api_schema/schema/core_samples.yaml`
- `src/analysis_api_schema/schema/enums.yaml` 
- `src/data/examples/valid/sample_basic.yaml`

### Week 5-6: Metadata Provider Integration Planning
**Deliverables:**
- USER SUBMISSION DELIVERABLES HERE
- POTENTIALLY: Design patterns for provider integration in LinkML context
- POTENTIALLY: Refactor `nasa_climate_provider.py` to work with LinkML models
- POTENTIALLY: Define metadata enrichment workflow in schema terms

### Week 7-8: Development Environment Setup
**Deliverables:**
- Docker integration for LinkML generation pipeline
- CI/CD setup for schema validation
- Documentation generation pipeline using mkdocs.yml

---

## Month 3-4: Core Schema Implementation

### Week 9-10: Sample Management Schema
**Deliverables:**
- Complete `Sample` class hierarchy with inheritance patterns
- Container and storage condition modeling
 

**Schema Structure:**
```yaml
classes:
  SampleBase:
    is_a: NamedThing
    slots:
      - id
      - sample_type
      - collection_date
      
  Sample:
    is_a: SampleBase
    slots:
      - latitude
      - longitude
      - depth
      
  ProcessedSample:
    is_a: SampleBase
    slots:
      - processing_method
      - parent_sample
```

### Week 11-12: Analysis Methods Schema
**Deliverables:**
- Method classes: `BulkDensityMethod`, `ElementalAnalysisMethod`, `EnzymeActivityMethod`
- Product classes: `BulkDensityProduct`, `ElementalAnalysisProduct`, `FTICRProduct`
- Method-to-product relationships

### Week 13-14: Enrichment Metadata Schema
**Deliverables:**
- TBD

### Week 15-16: Validation & Testing Framework
**Deliverables:**
- tbd

**Testing Commands:**
```bash
just test
make test-examples
poetry run linkml-validate
```

---

## Month 5: Integration & Migration Tools

### Week 17-18: Database Migration Tools
**Deliverables:**
- SQL-to-LinkML migration scripts
- Data transformation utilities
- Backward compatibility layers

**Migration Strategy:**
```python
# Example migration script
from analysis_api_schema.datamodel import Sample
from sqlalchemy import create_engine

def migrate_samples():
    # Read from existing PostgreSQL
    # Transform to LinkML models
    # Validate against schema
    # Write to new structure
```

### Week 19-20: API Integration Layer
**Deliverables:**
- FastAPI/Flask integration with LinkML models
- Request/response validation using schema
- Automatic OpenAPI generation

### Week 21-22: Metadata Synchronization System
**Deliverables:**
- User submission validation pipeline
- Backend metadata enrichment workflow 

**Sync Architecture:**
```yaml
# User submits sample metadata
user_metadata:
  sample_id: "SAMPLE_001"
  latitude: 45.1234
  longitude: -122.5678
  
# Backend enriches with providers
enriched_metadata:
  sample_id: "SAMPLE_001"  
  latitude: 45.1234
  longitude: -122.5678
  nasa_mean_annual_temp_c: 12.5
  nasa_mean_annual_precip_mm: 1200.0
```

### Week 23-24: Batch Processing Integration
**Deliverables:**
- tbd

---

## Month 6: Production Readiness & Future Planning

### Week 25-26: Performance Optimization
**Deliverables:**
- Schema compilation optimization
- Caching strategies for validation
- Database query optimization

### Week 27-28: Documentation & Training
**Deliverables:**
- Complete API documentation
- Schema evolution guidelines
- Developer onboarding materials

**Documentation Structure:**
```
docs/
├── index.md
├── schema/
│   ├── samples.md
│   ├── methods.md
│   └── enrichment.md
├── migration/
│   ├── database.md
│   └── api.md
└── examples/
    ├── submission.md
    └── enrichment.md
```

### Week 29-30: AMP2 Integration Planning
**Deliverables:**
- Cross-project schema alignment
- Shared vocabulary definitions
- Extension points for external projects

### Week 31-32: Production Deployment
**Deliverables:**
- TBD

---

## Key Considerations & Risk Mitigation

### Data Consistency
- **Challenge**: Ensuring user submissions match backend expectations
- **Solution**: Layered validation with clear error messages
- **Implementation**: Use LinkML's built-in validation with custom rules
 
### Backward Compatibility
- **Challenge**: Existing API consumers during transition
- **Solution**: Versioned APIs with gradual deprecation
- **Implementation**: Maintain v1 API while rolling out v2 

## Success Metrics

### Month 1-2: Foundation
- [ ] 100% of existing enums mapped to LinkML
- [ ] Basic sample schema validates existing data
- [ ] Development pipeline functional

### Month 3-4: Implementation  
- [ ] Core schema covers 80% of use cases
- [ ] Examples validate successfully
- [ ] Provider integration working

### Month 5: Integration
- [ ] Migration tools handle existing data
- [ ] API integration complete
- [ ] Batch processing updated

### Month 6: Production
- [ ] Performance benchmarks met
- [ ] Documentation complete
- [ ] AMP2 integration pathway defined

## Technology Stack

### Core Tools
- **LinkML**: Schema definition and validation
- **Poetry**: Dependency management (`pyproject.toml`)
- **Just/Make**: Build automation (justfile, `Makefile`)
- **MkDocs**: Documentation generation (`mkdocs.yml`)

### Integration Points
- **PostgreSQL**: Existing data store
- **Flask/FastAPI**: Web framework integration
- **MinIO**: Object storage for enrichment cache
- **Docker**: Containerized deployment 