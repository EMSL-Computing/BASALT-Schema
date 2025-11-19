import os
import yaml
import pytest
from pathlib import Path

METAGENOMICS_YAML = Path("src/analysis_api_schema/schema/metagenomics.yaml")
ANALYSIS_SCHEMA_YAML = Path("src/analysis_api_schema/schema/analysis_api_schema.yaml")

def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_metagenomics_classes_exist():
    data = load_yaml(METAGENOMICS_YAML)
    classes = data.get("classes", {})
    assert "Metagenomics_BinningProduct" in classes, "Missing Metagenomics_BinningProduct"
    assert "Metagenomics_AnnotationProduct" in classes, "Missing Metagenomics_AnnotationProduct"
    assert "Metagenomics_GenePhylogenyProduct" in classes, "Missing Metagenomics_GenePhylogenyProduct"

def test_id_ranges_to_processedData():
    data = load_yaml(METAGENOMICS_YAML)
    classes = data.get("classes", {})
    for cname in ("Metagenomics_BinningProduct", "Metagenomics_AnnotationProduct", "Metagenomics_GenePhylogenyProduct"):
        attrs = classes[cname].get("attributes", {})
        id_attr = attrs.get("id")
        assert id_attr is not None, f"{cname} missing id attribute"
        # check the id range references the processedData class name
        assert id_attr.get("range") == "processedData", f"{cname}.id.range != 'processedData'"

def test_processedData_has_required_s3_key():
    data = load_yaml(ANALYSIS_SCHEMA_YAML)
    classes = data.get("classes", {})
    pd = classes.get("processedData")
    assert pd is not None, "processedData class missing in analysis_api_schema.yaml"
    s3_key_attr = pd.get("attributes", {}).get("s3_key")
    assert s3_key_attr is not None, "processedData.s3_key attribute missing"
    # YAML has required: true for s3_key in your excerpt
    assert s3_key_attr.get("required", False) is True, "processedData.s3_key should be required"

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