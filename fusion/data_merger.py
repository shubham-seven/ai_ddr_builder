# fusion/data_merger.py

def merge_data(inspection_data, thermal_data):
    merged = []

    all_data = inspection_data + thermal_data

    for item in all_data:
        found = False

        for existing in merged:
            # Simple match: same area + similar issue
            if (
                item["area"].lower() == existing["area"].lower()
                and item["issue"].lower() in existing["issue"].lower()
            ):
                # Merge details
                existing["details"] += " | " + item["details"]

                # Add source
                existing["sources"].add(item["source"])

                # Merge images
                if "images" in item:
                    existing["images"].extend(item["images"])

                found = True
                break

        if not found:
            merged.append({
                "area": item["area"],
                "issue": item["issue"],
                "details": item["details"],
                "sources": {item["source"]},
                "images": item.get("images", [])
            })

    # Convert set → list
    for m in merged:
        m["sources"] = list(m["sources"])

    return merged