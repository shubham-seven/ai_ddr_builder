# ingestion/text_extractor.py

def extract_text_by_page(doc, max_pages=None):
    text_data = []

    total_pages = len(doc)
    limit = min(max_pages, total_pages) if max_pages else total_pages

    for page_num in range(limit):
        page = doc[page_num]
        text = page.get_text()

        text_data.append({
            "page": page_num + 1,
            "text": text
        })

    return text_data