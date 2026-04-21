# processing/image_filter.py

from PIL import Image
import os
import hashlib


def get_image_hash(image_path):
    """Generate hash for duplicate detection"""
    with open(image_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def filter_images(image_data, min_width=200, min_height=200):
    filtered_images = []
    seen_hashes = set()

    for img in image_data:
        path = img["image_path"]

        if not os.path.exists(path):
            continue

        try:
            with Image.open(path) as im:
                width, height = im.size

                # ❌ Filter small images
                if width < min_width or height < min_height:
                    continue

                # ❌ Remove duplicates
                img_hash = get_image_hash(path)
                if img_hash in seen_hashes:
                    continue

                seen_hashes.add(img_hash)

                # ✅ Keep valid image
                img["width"] = width
                img["height"] = height

                filtered_images.append(img)

        except Exception as e:
            print(f"⚠️ Skipping image {path}: {e}")

    print(f"✅ Filtered images: {len(filtered_images)} / {len(image_data)}")
    return filtered_images