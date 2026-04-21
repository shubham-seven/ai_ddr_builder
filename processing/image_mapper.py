def map_images_to_observations(structured_data, images, debug=False):

    # Step 1: group images into pairs
    pairs = {}

    for img in images:
        page = img["page"]
        idx = img["index"]

        key = (page, idx // 2)  # pair grouping

        if key not in pairs:
            pairs[key] = []

        pairs[key].append(img)

    # Step 2: assign pairs to observations
    for obs in structured_data:
        obs_page = obs.get("page")
        issue = obs.get("issue", "").lower()

        matched_images = []

        for (page, _), pair_imgs in pairs.items():
            if page != obs_page:
                continue

            # Check if pair contains thermal image
            has_thermal = any("thermal" in img["image_path"] for img in pair_imgs)

            if has_thermal:
                # assign SAME pair to both hotspot & coldspot
                if "hotspot" in issue or "coldspot" in issue:
                    matched_images.extend(pair_imgs)

            else:
                # inspection images → normal issues
                if "hotspot" not in issue and "coldspot" not in issue:
                    matched_images.extend(pair_imgs)

        # fallback
        if not matched_images:
            matched_images = [img for img in images if img["page"] == obs_page]

        # debug vs production
        if debug:
            obs["images"] = matched_images[:10]
        else:
            obs["images"] = matched_images[:4]

    return structured_data