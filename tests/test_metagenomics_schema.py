import os
import yaml
import pytest
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

METAGENOMICS_YAML = Path("src/analysis_api_schema/schema/metagenomics.yaml")
ANALYSIS_SCHEMA_YAML = Path("src/analysis_api_schema/schema/analysis_api_schema.yaml")

METAGENOMICS_PRODUCTS = (
    "Metagenomics_BinningProduct",
    "Metagenomics_AnnotationProduct",
    "Metagenomics_GenePhylogenyProduct",
)

def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def sv():
    """
    Inheritance- and import-aware view of the schema. Needed because most slots
    on these classes are inherited rather than declared in the class's own
    "attributes" block, so raw yaml.safe_load cannot see them.
    """
    return SchemaView(str(ANALYSIS_SCHEMA_YAML))

def test_metagenomics_classes_exist():
    data = load_yaml(METAGENOMICS_YAML)
    classes = data.get("classes", {})
    assert "Metagenomics_BinningProduct" in classes, "Missing Metagenomics_BinningProduct"
    assert "Metagenomics_AnnotationProduct" in classes, "Missing Metagenomics_AnnotationProduct"
    assert "Metagenomics_GenePhylogenyProduct" in classes, "Missing Metagenomics_GenePhylogenyProduct"

def test_metagenomics_products_derive_from_ProcessedData(sv):
    """
    These classes are tied to ProcessedData through the is_a chain
    (-> MetagenomicsProduct -> ProcessedData), not through an id range.
    """
    for cname in METAGENOMICS_PRODUCTS:
        ancestors = sv.class_ancestors(cname)
        assert "ProcessedData" in ancestors, f"{cname} does not inherit from ProcessedData (got {ancestors})"

def test_metagenomics_products_have_required_uuid_id(sv):
    for cname in METAGENOMICS_PRODUCTS:
        id_slot = sv.induced_slot("id", cname)
        assert id_slot is not None, f"{cname} has no id slot"
        assert id_slot.range == "uuid", f"{cname}.id.range == {id_slot.range!r}, expected 'uuid'"
        assert id_slot.required is True, f"{cname}.id should be required"

def test_ProcessedData_has_required_s3_key(sv):
    assert "ProcessedData" in sv.all_classes(imports=True), "ProcessedData class missing from schema"
    s3_key = sv.induced_slot("s3_key", "ProcessedData")
    assert s3_key is not None, "ProcessedData.s3_key slot missing"
    assert s3_key.required is True, "ProcessedData.s3_key should be required"

def assemble_s3_url(processed):
    # processed is dict with s3_base_url, s3_bucket, s3_key
    base = processed.get("s3_base_url", "").rstrip("/")
    bucket = processed.get("s3_bucket", "").strip("/")
    key = processed.get("s3_key", "").lstrip("/")
    if not base or not key:
        return None
    # Basic S3-style URL assembly (adjust to your deployment)
    return f"{base}/{bucket}/{key}" if bucket else f"{base}/{key}"

@pytest.mark.skipif(not os.getenv("MINIO_TEST_URL"), reason="MINIO_TEST_URL not set")
def test_minio_pointer_accessibility():
    """
    Optional integration check: set MINIO_TEST_URL to a reachable URL, e.g.
    http://localhost:9000 and provide MINIO_TEST_KEY and MINIO_TEST_SECRET in env
    and MINIO_TEST_OBJECT as the key to test.
    """
    import requests
    url = os.getenv("MINIO_TEST_URL").rstrip("/")
    bucket = os.getenv("MINIO_TEST_BUCKET", "")
    key = os.getenv("MINIO_TEST_OBJECT")
    assert key, "Set MINIO_TEST_OBJECT env var to a test object key"
    obj_url = f"{url}/{bucket}/{key}" if bucket else f"{url}/{key}"
    r = requests.head(obj_url, timeout=10)
    assert r.status_code == 200, f"MinIO object not reachable: {r.status_code}"