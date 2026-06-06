"""
Functionality tests for data loading: URL CSV downloads and Kaggle dataset retrieval.
"""

import os
import shutil
from pathlib import Path

import pytest

_HAS_KAGGLE_AUTH = (Path.home() / ".kaggle" / "kaggle.json").exists() or bool(
    os.environ.get("KAGGLE_USERNAME") and os.environ.get("KAGGLE_KEY")
)

DATA_DIR = Path(os.environ.get("AILANG_DATA_DIR", ".ailang/data"))

RAW_CSV_URL = "https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv"

KAGGLE_URL = (
    "https://www.kaggle.com/datasets/defcodeking/spaceship-titanic-prepared-datasets"
)

# Files inside the downloaded dataset
KAGGLE_TRAIN = "train_prepared.csv"
KAGGLE_TEST = "test_prepared.csv"


from main import runAilang

# ── Fixtures ─────────────────────────────────────────────


@pytest.fixture(autouse=True)
def clean_data_dir():
    data_dir = Path(os.environ.get("AILANG_DATA_DIR", ".ailang/data"))
    if data_dir.exists():
        shutil.rmtree(data_dir)
    yield
    if data_dir.exists():
        shutil.rmtree(data_dir)


# ── URL CSV download (from) ──────────────────────────────


class TestUrlCsvDownload:
    def test_from_url_loads_and_caches(self):
        runAilang(f'-> {{ from "{RAW_CSV_URL}" -> data }}')
        cache = DATA_DIR / "industry.csv"
        assert cache.exists()
        import pandas as pd

        df = pd.read_csv(cache)
        assert not df.empty
        assert "Industry" in df.columns

    def test_from_url_reuses_cache(self):
        runAilang(f'-> {{ from "{RAW_CSV_URL}" -> data }}')
        cache = DATA_DIR / "industry.csv"
        mtime_first = cache.stat().st_mtime
        runAilang(f'-> {{ from "{RAW_CSV_URL}" -> data }}')
        mtime_second = cache.stat().st_mtime
        assert mtime_first == mtime_second, "File was re-downloaded"


# ── Generic URL download (get) ──────────────────────────────


class TestGetUrlFile:
    def test_get_url_downloads_file(self):
        runAilang(f'-> {{ get "{RAW_CSV_URL}" }}')
        cache = DATA_DIR / "industry.csv"
        assert cache.exists()
        assert cache.stat().st_size > 0

    def test_get_url_imported_corner(self):
        runAilang(f'-> {{ get "{RAW_CSV_URL}" }}')
        runAilang(f'-> {{ from "industry.csv" -> data }}')
        import pandas as pd

        df = pd.read_csv(DATA_DIR / "industry.csv")
        assert not df.empty
        assert "Industry" in df.columns


# ── Kaggle dataset download (get) ────────────────────────


@pytest.mark.skipif(not _HAS_KAGGLE_AUTH, reason="Kaggle API credentials not found")
class TestKaggleDownload:
    def test_get_whole_dataset(self):
        runAilang(f'-> {{ get "{KAGGLE_URL}" }}')
        assert (DATA_DIR / KAGGLE_TRAIN).exists()
        assert (DATA_DIR / KAGGLE_TEST).exists()

    def test_get_specific_file(self):
        runAilang(f'-> {{ get "{KAGGLE_URL}" "{KAGGLE_TRAIN}" }}')
        assert (DATA_DIR / KAGGLE_TRAIN).exists()

    def test_get_multiple_specific_files(self):
        runAilang(f'-> {{ get "{KAGGLE_URL}" "{KAGGLE_TRAIN}" }}')
        runAilang(f'-> {{ get "{KAGGLE_URL}" "{KAGGLE_TEST}" }}')
        assert (DATA_DIR / KAGGLE_TRAIN).exists()
        assert (DATA_DIR / KAGGLE_TEST).exists()

    def test_get_then_from_loads_dataframe(self):
        runAilang(f'-> {{ get "{KAGGLE_URL}" "{KAGGLE_TRAIN}" }}')
        runAilang(f'-> {{ from "{KAGGLE_TRAIN}" -> data }}')
        import pandas as pd

        df = pd.read_csv(DATA_DIR / KAGGLE_TRAIN)
        assert not df.empty
