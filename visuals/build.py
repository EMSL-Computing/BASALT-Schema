#!/usr/bin/env python
"""Rebuild the embedded data model in visuals/schema-explorer.html from the LinkML schema.

One command, in place:

    uv run python visuals/build.py          # or: .venv/bin/python visuals/build.py

It re-reads the schema with LinkML SchemaView (resolving inheritance, mixins, slot
usage, source module, etc. — none of which the built-in gen-json-schema preserves),
then rewrites the <script id="model"> block in schema-explorer.html. It also prints a
diff of classes added/removed since the last build, which is handy for change tracking.

Why not the generated project/jsonschema/*.json? That output flattens inheritance and
drops from_schema/module info, so it cannot drive the hierarchy/highlight features here.
"""
import json, sys
from pathlib import Path
from linkml_runtime import SchemaView

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src/analysis_api_schema/schema/analysis_api_schema.yaml"
HTML = ROOT / "visuals/schema-explorer.html"
MARKER = '<script id="model" type="application/json">'


def build_model():
    sv = SchemaView(str(SCHEMA))
    classes, enums = sv.all_classes(), sv.all_enums()

    def module_of(elt):
        fs = getattr(elt, "from_schema", None) or ""
        return fs.rsplit("/", 1)[-1] if fs else ""

    def root_of(name):                       # topmost is_a ancestor (mixins ignored)
        cur = name
        while classes[cur].is_a:
            cur = classes[cur].is_a
        return cur

    def anc_set(name):
        return set(sv.class_ancestors(name, mixins=True)) | {name}

    def stage_of(name):                      # process-flow lane
        a = anc_set(name)
        if name == "biological_entity": return "bioentity"
        if "DataProduct" in a or "PlateProduct" in a or name in ("MAOMProduct", "WEOMProduct"): return "products"
        if "DataProcessingActivity" in a: return "dataproc"
        if "DataGenerationActivity" in a: return "datagen"
        if "SampleProcessing" in a or "LabProcessingActivity" in a or "PurchasedMaterial" in a: return "processing"
        if "SamplingActivity" in a: return "sampling"
        if "Sample" in a or name == "Site": return "samples"
        if "Method" in a: return "methods"
        if name.endswith("Value") or name in ("QuantityValue", "DOI"): return "values"
        return "reference"

    out_classes = {}
    for name, c in classes.items():
        direct = set(sv.class_slots(name, direct=True))
        slots = [{
            "name": s.name, "range": s.range,
            "required": bool(s.required), "multivalued": bool(s.multivalued),
            "identifier": bool(s.identifier), "pattern": s.pattern or "",
            "desc": (s.description or "").strip(),
            "inherited": s.name not in direct,
            "is_enum": s.range in enums, "is_class": s.range in classes,
        } for s in sv.class_induced_slots(name)]
        out_classes[name] = {
            "name": name, "is_a": c.is_a, "mixins": list(c.mixins or []),
            "abstract": bool(c.abstract), "mixin": bool(c.mixin),
            "desc": (c.description or "").strip(), "module": module_of(c),
            "ancestors": list(sv.class_ancestors(name, reflexive=False)),
            "root": root_of(name), "stage": stage_of(name),
            "children": [k for k, v in classes.items() if v.is_a == name],
            "slots": slots, "title": c.title or "",
        }

    out_enums = {}
    for name, e in enums.items():
        pvs = list((e.permissible_values or {}).keys())
        out_enums[name] = {"name": name, "desc": (e.description or "").strip(),
                           "module": module_of(e), "values": pvs[:40], "n": len(pvs)}

    return {"classes": out_classes, "enums": out_enums}


def main():
    html = HTML.read_text()
    start = html.index(MARKER) + len(MARKER)
    end = html.index("</script>", start)
    prev = set()
    try:
        prev = set(json.loads(html[start:end]).get("classes", {}))
    except Exception:
        pass

    model = build_model()
    now = set(model["classes"])
    # embed-safe: `<\/` can never prematurely close the <script> block
    payload = json.dumps(model, separators=(",", ":")).replace("</", "<\\/")
    HTML.write_text(html[:start] + payload + html[end:])

    added, removed = sorted(now - prev), sorted(prev - now)
    print(f"✓ {HTML.relative_to(ROOT)} updated — {len(now)} classes, {len(model['enums'])} enums")
    if added:   print(f"  + added ({len(added)}): " + ", ".join(added))
    if removed: print(f"  - removed ({len(removed)}): " + ", ".join(removed))
    if not (added or removed): print("  (no classes added or removed)")


if __name__ == "__main__":
    sys.exit(main())
