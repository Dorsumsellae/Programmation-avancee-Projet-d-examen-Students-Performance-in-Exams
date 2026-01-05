"""
CLI helper to fetch the Students Performance dataset from Kaggle.
Requires a Kaggle API token (kaggle.json) in %USERPROFILE%/.kaggle or KAGGLE_USERNAME/KAGGLE_KEY env vars.
"""
from pathlib import Path
import argparse
import zipfile
import sys

from kaggle.api.kaggle_api_extended import KaggleApi

DEFAULT_DATASET = "spscientist/students-performance-in-exams"
DEFAULT_FILENAME = "StudentsPerformance.csv"
DEFAULT_RAW_DIR = "data/raw"


def download_dataset(dataset: str = DEFAULT_DATASET, filename: str = DEFAULT_FILENAME, raw_dir: str = DEFAULT_RAW_DIR) -> Path:
    """Download the dataset file if missing and return the local path."""
    raw_path = Path(raw_dir)
    raw_path.mkdir(parents=True, exist_ok=True)

    target = raw_path / filename
    zipped = raw_path / f"{filename}.zip"

    if target.exists():
        print(f"Dataset already present at {target}")
        return target

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as exc:  # Kaggle raises generic Exceptions for auth issues
        print("Kaggle authentication failed. Ensure kaggle.json is in %USERPROFILE%/.kaggle or set KAGGLE_USERNAME/KAGGLE_KEY.")
        raise

    print(f"Downloading {dataset}:{filename} to {raw_path}")
    api.dataset_download_file(dataset, file_name=filename, path=raw_path, quiet=False)

    if target.exists():
        print(f"Downloaded to {target}")
        return target

    if zipped.exists():
        with zipfile.ZipFile(zipped, "r") as zf:
            zf.extractall(raw_path)
        zipped.unlink()
        if target.exists():
            print(f"Downloaded and extracted to {target}")
            return target

    raise FileNotFoundError(f"Expected {target} after download; check dataset and filename.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Download the Students Performance dataset from Kaggle.")
    parser.add_argument("--dataset", default=DEFAULT_DATASET, help="Kaggle dataset slug, e.g. owner/dataset")
    parser.add_argument("--filename", default=DEFAULT_FILENAME, help="Dataset file to fetch")
    parser.add_argument("--raw-dir", default=DEFAULT_RAW_DIR, help="Destination directory for the raw file")
    args = parser.parse_args()

    try:
        download_dataset(dataset=args.dataset, filename=args.filename, raw_dir=args.raw_dir)
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
