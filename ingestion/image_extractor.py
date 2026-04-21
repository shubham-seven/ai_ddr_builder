# ingestion/image_extractor.py

import os
import fitz


def extract_images(doc, output_dir="data/images", prefix="img", max_pages=None):
    import os
    os.makedirs(output_dir, exist_ok=True)

    image_data = []

    total_pages = len(doc)
    limit = min(max_pages, total_pages) if max_pages else total_pages

    for page_index in range(limit):
        page = doc[page_index]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]

            img_filename = f"{prefix}_p{page_index+1}_{img_index}.png"
            img_path = os.path.join(output_dir, img_filename)

            if os.path.exists(img_path):
                image_data.append({
                    "image_path": img_path,
                    "page": page_index + 1,
                    "index": img_index
                })
                continue

            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            with open(img_path, "wb") as f:
                f.write(image_bytes)

            image_data.append({
                "image_path": img_path,
                "page": page_index + 1,
                "index": img_index
            })

    return image_data