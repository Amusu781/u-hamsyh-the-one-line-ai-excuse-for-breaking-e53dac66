"""The One-Line AI Excuse for Breaking Production: writes one funny line to /output/entry.txt."""

import os
import shutil


LINE = "I did back up the database before deploying — I stored the backup in the same folder, then deleted the folder, because a backup nobody can find is just a secret."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Create the output directory first.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One line only: the whole entry is a single sentence.
        f.write(LINE)


if __name__ == "__main__":
    main()
