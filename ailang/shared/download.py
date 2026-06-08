# pylint: disable=invalid-name
"""Download/get functionality for AiLang: generic URL downloads and Kaggle dataset retrieval."""

import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

import kagglehub

from ailang.shared.utils import _AILANG_DATA_DIR, _ensureDataDir, downloadToPath


def parseKaggleHandle(url: str) -> str:
    """Extract `owner/dataset` handle from a Kaggle URL, or pass through if already a handle."""
    parsed = urlparse(url)
    if parsed.netloc and "kaggle.com" in parsed.netloc:
        path = parsed.path.strip("/")
        m = re.match(r"datasets/([^/]+/[^/]+)", path)
        if not m:
            print(f"Could not parse Kaggle dataset URL: {url}")
            sys.exit(1)
        return m.group(1)
    if "/" in url and not url.startswith("http"):
        return url
    print(f"Unrecognised Kaggle URL format: {url}")
    sys.exit(1)


def downloadUrlFile(url: str) -> Path:
    """Download any file from a URL to the data directory. Returns the destination path."""
    _ensureDataDir()
    parsed = urlparse(url)
    filename = Path(parsed.path).name
    if not filename:
        print(f"Could not determine filename from URL: {url}")
        sys.exit(1)
    dest = _AILANG_DATA_DIR / filename
    downloadToPath(url, dest)
    print(f"Downloaded {url} -> {dest}")
    return dest


def downloadKaggleDataset(handle: str, specific_file: str | None = None) -> None:
    """Download a Kaggle dataset by handle, with optional single-file selection."""
    _ensureDataDir()
    download_path = kagglehub.dataset_download(handle, path=specific_file)

    src = Path(download_path)
    if specific_file:
        dst = _AILANG_DATA_DIR / specific_file
        shutil.copy2(src, dst)
        print(f"Downloaded {specific_file} -> {dst}")
    else:
        for item in src.iterdir():
            if item.is_file():
                shutil.copy2(item, _AILANG_DATA_DIR / item.name)
        print(f"Downloaded dataset -> {_AILANG_DATA_DIR}")


def getFile(raw: str, specific_file: str | None = None) -> None:
    """Dispatch a `get` operation to generic URL download or Kaggle dataset download."""
    if raw.startswith("http") and "kaggle.com" not in raw:
        downloadUrlFile(raw)
    else:
        handle = parseKaggleHandle(raw)
        downloadKaggleDataset(handle, specific_file)
