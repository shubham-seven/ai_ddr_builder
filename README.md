# 🏠 AI-Based DDR (Detailed Diagnostic Report) Generator

An end-to-end AI system that processes inspection and thermal PDFs to generate a structured, client-ready **Detailed Diagnostic Report (DDR)** with insights, severity analysis, and visual evidence.

---

## 🚀 Project Overview

This project builds an intelligent pipeline that:

* Extracts **text + images** from inspection & thermal PDFs
* Uses **LLMs (Gemini)** to structure and interpret data
* Maps **images to observations** intelligently
* Performs **root cause & severity analysis**
* Generates a **clean HTML + JSON report**

---

## 🧠 Key Features

✅ Multi-modal processing (Text + Images)
✅ LLM-powered structuring & reasoning
✅ Intelligent image mapping (thermal + normal pairing)
✅ Conflict handling across multiple sources
✅ Root cause analysis
✅ Severity assessment
✅ Clean HTML report generation

---

## 🏗️ Project Architecture

```
ai_ddr_builder/
│
├── main.py
├── .env
├── requirements.txt
│
├── ingestion/
│   ├── pdf_loader.py
│   ├── text_extractor.py
│   ├── image_extractor.py
│
├── processing/
│   ├── text_structurer.py
│   ├── image_filter.py
│   ├── image_mapper.py
│
├── fusion/
│   ├── data_merger.py
│   ├── conflict_handler.py
│
├── reasoning/
│   ├── root_cause_analyzer.py
│   ├── severity_analyzer.py
│
├── report/
│   ├── ddr_generator.py
│   ├── template_builder.py
│
├── utils/
│   ├── llm_client.py
│
├── prompts/
│   ├── extraction_prompt.txt
│   ├── root_cause_prompt.txt
│   ├── severity_prompt.txt
│
├── data/
│   ├── input/
│   ├── images/
│   ├── output/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shubham-seven/ai_ddr_builder.git
cd ai_ddr_builder
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 5️⃣ Add Input PDFs

Place files inside:

```
data/input/
```

Example:

```
inspection.pdf
thermal.pdf
```

---

## ▶️ Run the Project

### Debug Mode (Recommended First)

```bash
python main.py
```

Runs with:

* limited pages
* limited LLM calls
* faster execution

---

## 📊 Output

### 📁 Generated Files

```
data/output/
├── ddr_report.json
├── ddr_report.html
```

---

### 🖥️ HTML Report Includes:

* Property Issue Summary
* Area-wise Observations
* Images (thermal + normal paired)
* Root Cause Analysis
* Severity Assessment
* Recommendations

---

## 🧠 Design Decisions

### 🔹 Controlled LLM Usage

* **Flash model** → text structuring (fast)
* **Pro model** → reasoning (accurate)

---

### 🔹 Image Mapping Strategy

* Images grouped into **pairs (thermal + normal)**
* Pair assigned to both hotspot & coldspot observations
* Based on **index-based pairing**

---

### 🔹 Handling PDF Limitations

* PDFs do not provide direct mapping between text and images
* Solution: **page-level grouping + heuristic alignment**

---

### 🔹 Debug Mode

* Limits:

  * pages processed
  * LLM calls
* Helps reduce cost and speed up testing

---

## ⚠️ Limitations

* No exact mapping between specific text and specific image (PDF limitation)
* Heuristic-based image association
* Root cause inference depends on LLM reasoning

---

## 🚀 Future Improvements

* Layout-aware parsing (bounding boxes)
* Vision-based image classification
* Better semantic matching (embeddings)
* Structured database storage
* Web UI for uploading PDFs

---


## 📌 Conclusion

This project demonstrates how to build a **real-world AI pipeline** combining:

* Document processing
* LLM reasoning
* Image analysis
* Structured reporting

---
## 📸 Sample Output

You can view the generated DDR report here:

👉 data/output/ddr_report.html

## 👨‍💻 Author

Shubham Trivedi
