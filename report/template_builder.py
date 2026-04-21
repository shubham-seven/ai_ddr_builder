# report/template_builder.py

import os


def generate_html_report(ddr_data, output_path="data/output/ddr_report.html"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    html = f"""
    <html>
    <head>
        <title>DDR Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f8f9fa;
            }}
            h1, h2 {{
                color: #2c3e50;
            }}
            .section {{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .issue {{
                margin-bottom: 15px;
            }}
            .images img {{
                width: 250px;
                margin: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }}
        </style>
    </head>
    <body>

    <h1>🏠 Detailed Diagnostic Report (DDR)</h1>

    <div class="section">
        <h2>Property Issue Summary</h2>
        <ul>
    """

    # -----------------------------
    # Summary
    # -----------------------------
    for item in ddr_data["Property Issue Summary"]:
        html += f"<li>{item}</li>"

    html += "</ul></div>"

    # -----------------------------
    # Area-wise Observations
    # -----------------------------
    html += '<div class="section"><h2>Area-wise Observations</h2>'

    for obs in ddr_data["Area-wise Observations"]:
        html += f"""
        <div class="issue">
            <h3>{obs['area']} - {obs['issue']}</h3>
            <p>{obs['details']}</p>

            <div class="images">
        """

        images = obs.get("images", [])

        if not images or images == ["Image Not Available"]:
            html += "<p><i>Image Not Available</i></p>"
        else:
            for img in images:
                path = img["image_path"] if isinstance(img, dict) else img

        # ✅ Safe relative path
                relative_path = os.path.relpath(path, start="data/output")
                relative_path = relative_path.replace("\\", "/")

        # ✅ Check file exists
                if os.path.exists(path):
                    html += f'<img src="{relative_path}" />'
                else:
                    html += "<p><i>Image Not Available</i></p>"

        html += "</div></div>"

    html += "</div>"

    # -----------------------------
    # Root Cause
    # -----------------------------
    html += '<div class="section"><h2>Probable Root Cause</h2><ul>'

    for item in ddr_data["Probable Root Cause"]:
        html += f"<li><b>{item['area']}:</b> {item['cause']}</li>"

    html += "</ul></div>"

    # -----------------------------
    # Severity
    # -----------------------------
    html += '<div class="section"><h2>Severity Assessment</h2><ul>'

    for item in ddr_data["Severity Assessment"]:
        html += f"<li><b>{item['area']}:</b> {item['severity']}</li>"

    html += "</ul></div>"

    # -----------------------------
    # Recommendations
    # -----------------------------
    html += '<div class="section"><h2>Recommended Actions</h2><ul>'

    for item in ddr_data["Recommended Actions"]:
        html += f"<li><b>{item['area']}:</b> {item['action']}</li>"

    html += "</ul></div>"

    # -----------------------------
    # Additional Notes
    # -----------------------------
    html += '<div class="section"><h2>Additional Notes</h2><ul>'

    for item in ddr_data["Additional Notes"]:
        html += f"<li><b>{item['area']}:</b> {item['note']}</li>"

    html += "</ul></div>"

    # -----------------------------
    # Missing Info
    # -----------------------------
    html += '<div class="section"><h2>Missing or Unclear Information</h2><ul>'

    for item in ddr_data["Missing or Unclear Information"]:
        html += f"<li><b>{item['area']}:</b> {item['info']}</li>"

    html += "</ul></div>"

    html += "</body></html>"

    # Save file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ HTML report saved at {output_path}")
    print("IMG PATH:", path, "→", relative_path)