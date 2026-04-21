# report/ddr_generator.py

def generate_ddr(data):
    report = {
        "Property Issue Summary": [],
        "Area-wise Observations": [],
        "Probable Root Cause": [],
        "Severity Assessment": [],
        "Recommended Actions": [],
        "Additional Notes": [],
        "Missing or Unclear Information": []
    }

    for item in data:
        area = item.get("area", "Not Available")
        issue = item.get("issue", "Not Available")
        details = item.get("details", "Not Available")
        root_cause = item.get("root_cause", "Not Available")
        severity = item.get("severity", "Not Available")
        images = item.get("images", ["Image Not Available"])
        conflict = item.get("conflict")
        missing = item.get("missing_info")

        # -----------------------------
        # Summary
        # -----------------------------
        report["Property Issue Summary"].append(f"{area}: {issue}")

        # -----------------------------
        # Area-wise Observations
        # -----------------------------
        report["Area-wise Observations"].append({
            "area": area,
            "issue": issue,
            "details": details,
            "images": images
        })

        # -----------------------------
        # Root Cause
        # -----------------------------
        report["Probable Root Cause"].append({
            "area": area,
            "cause": root_cause
        })

        # -----------------------------
        # Severity
        # -----------------------------
        report["Severity Assessment"].append({
            "area": area,
            "severity": severity
        })

        # -----------------------------
        # Recommendations (basic rule-based)
        # -----------------------------
        recommendation = generate_recommendation(issue, severity)
        report["Recommended Actions"].append({
            "area": area,
            "action": recommendation
        })

        # -----------------------------
        # Additional Notes
        # -----------------------------
        if conflict:
            report["Additional Notes"].append({
                "area": area,
                "note": conflict
            })

        # -----------------------------
        # Missing Info
        # -----------------------------
        if missing:
            report["Missing or Unclear Information"].append({
                "area": area,
                "info": missing
            })

    return report


def generate_recommendation(issue, severity):
    issue = issue.lower()
    severity = severity.lower()

    if "damp" in issue or "leak" in issue:
        return "Inspect waterproofing and repair affected areas"

    if "crack" in issue:
        return "Consult structural engineer for crack assessment"

    if "electrical" in issue:
        return "Check wiring and ensure safety compliance"

    if "high" in severity:
        return "Immediate attention required by professional"

    return "Further inspection recommended"