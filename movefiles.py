import os
import json
import shutil

PICTURES_DIR = r"C:\Users\IIcee\Desktop\picture"
JSON_PATH = r"C:\Users\IIcee\car_counter\pictures.json"


def load_state(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"JSON file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Expecting the newer structure with "pictures" list
    if isinstance(data, dict) and "pictures" in data:
        return data["pictures"]

    # Fallback if JSON is a plain list of picture entries
    if isinstance(data, list):
        return data

    raise ValueError("Unexpected JSON format in pictures.json")


def main():
    pictures = load_state(JSON_PATH)

    # Collect all descriptions
    descriptions = sorted(
        {p.get("description") for p in pictures if p.get("description")}
    )

    if not descriptions:
        print("No descriptions found in JSON. Nothing to do.")
        return

    print("Found descriptions:")
    for d in descriptions:
        print(f"  - {d}")

    # Create a folder for each description
    for desc in descriptions:
        folder_path = os.path.join(PICTURES_DIR, desc)
        os.makedirs(folder_path, exist_ok=True)

    moved_count = 0

    # Move files based on description + filename
    for p in pictures:
        desc = p.get("description")
        filename = p.get("filename")

        if not desc or not filename:
            continue

        src_in_root = os.path.join(PICTURES_DIR, filename)
        dest_folder = os.path.join(PICTURES_DIR, desc)
        dest_path = os.path.join(dest_folder, filename)

        # If already in the right folder, skip
        if os.path.exists(dest_path):
            continue

        # If it's still in the root picture folder, move it
        if os.path.exists(src_in_root):
            shutil.move(src_in_root, dest_path)
            moved_count += 1
            print(f"Moved {filename} -> {dest_folder}")
        else:
            # Maybe it was manually moved or deleted; just skip
            pass

    print(f"\nDone. Total files moved: {moved_count}")


if __name__ == "__main__":
    main()
