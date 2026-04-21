# fusion/conflict_handler.py

def handle_conflicts(merged_data):
    for item in merged_data:
        details = item["details"].lower()

        # Simple conflict detection
        if "no issue" in details and "damage" in details:
            item["conflict"] = "Conflicting information detected"
        else:
            item["conflict"] = None

        # Missing info check
        if item["area"] == "Not Available":
            item["missing_info"] = "Area not specified"
        else:
            item["missing_info"] = None

    return merged_data