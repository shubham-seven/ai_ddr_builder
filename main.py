# main.py

from ingestion.pdf_loader import load_pdf
from ingestion.text_extractor import extract_text_by_page
from ingestion.image_extractor import extract_images

from processing.text_structurer import structure_text
from processing.image_filter import filter_images
from processing.image_mapper import map_images_to_observations

from fusion.data_merger import merge_data
from fusion.conflict_handler import handle_conflicts

from reasoning.root_cause_analyzer import analyze_root_cause
from reasoning.severity_analyzer import analyze_severity

from report.ddr_generator import generate_ddr
import json
import os

from report.template_builder import generate_html_report

def run_pipeline(inspection_path, thermal_path, debug=False):
    print("🚀 Starting DDR AI Pipeline...\n")

    max_pages = 2 if debug else None
    max_chunks = 1 if debug else 5

    # -----------------------------
    # 1. Load PDFs
    # -----------------------------
    inspection_doc = load_pdf(inspection_path)
    thermal_doc = load_pdf(thermal_path)

    # -----------------------------
    # 2. Extract Text
    # -----------------------------
    print("📄 Extracting text...")
    inspection_text = extract_text_by_page(inspection_doc, max_pages=max_pages)
    thermal_text = extract_text_by_page(thermal_doc, max_pages=max_pages)

    # -----------------------------
    # 3. Extract Images
    # -----------------------------
    print("🖼️ Extracting images...")
    inspection_images = extract_images(inspection_doc, prefix="inspection", max_pages=max_pages)
    thermal_images = extract_images(thermal_doc, prefix="thermal", max_pages=max_pages)

    # -----------------------------
    # 4. Filter Images
    # -----------------------------
    print("🧹 Filtering images...")
    inspection_images = filter_images(inspection_images)
    thermal_images = filter_images(thermal_images)

    # -----------------------------
    # 5. Structure Text (LLM)
    # -----------------------------
    print("🧠 Structuring text with LLM...")
    inspection_structured = structure_text(inspection_text, source="inspection", max_chunks=max_chunks)
    thermal_structured = structure_text(thermal_text, source="thermal", max_chunks=max_chunks)

    # -----------------------------
    # 6. Map Images
    # -----------------------------
    print("🔗 Mapping images to observations...")
    inspection_structured = map_images_to_observations(inspection_structured, inspection_images, debug=debug)
    thermal_structured = map_images_to_observations(thermal_structured, thermal_images, debug=debug)

    # -----------------------------
    # 7. Merge Data (NEW)
    # -----------------------------
    print("🔀 Merging inspection + thermal data...")
    merged_data = merge_data(inspection_structured, thermal_structured)

    # -----------------------------
    # 8. Handle Conflicts (NEW)
    # -----------------------------
    print("⚠️ Handling conflicts...")
    final_data = handle_conflicts(merged_data)
    # -----------------------------

    # 9. Root Cause Analysis
    # -----------------------------
    print("🧠 Analyzing root causes...")
    final_data = analyze_root_cause(final_data)
    # -----------------------------

    # 10. Severity Analysis
    # -----------------------------
    print("⚖️ Assessing severity...")
    final_data = analyze_severity(final_data)
    # -----------------------------

    # -----------------------------
    # 11. Generate DDR Report
    # -----------------------------
    print("🧾 Generating DDR report...")
    ddr_report = generate_ddr(final_data)

    # -----------------------------
    # 12. Save Report
    # -----------------------------
    os.makedirs("data/output", exist_ok=True)

    with open("data/output/ddr_report.json", "w") as f:
         json.dump(ddr_report, f, indent=4)

    print("✅ DDR report saved at data/output/ddr_report.json")

    # -----------------------------
    # 13. Generate HTML Report
    # -----------------------------
    print("🌐 Generating HTML report...")
    generate_html_report(ddr_report)

    # 14. Debug Output
    # -----------------------------
    print("\n--- FINAL SAMPLE ---")
    print(final_data[0] if final_data else "No data")

    # -----------------------------
    # 15. Return Everything
    # -----------------------------
    return final_data


if __name__ == "__main__":
    results = run_pipeline(
        "inspection.pdf",
        "thermal.pdf",
        debug=True  
    )