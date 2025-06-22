from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def test_extract():
    df = extract_data("data/social_ads.csv")
    assert not df.empty, "Extracted DataFrame is empty"

def test_transform():
    df = extract_data("data/social_ads.csv")
    df_clean = transform_data(df)
    assert 'AgeGroup' in df_clean.columns, "AgeGroup column missing after transform"

def test_load(tmp_path):
    # Create a temp file path
    test_path = tmp_path / "test_cleaned_data.csv"
    df = extract_data("data/social_ads.csv")
    df_clean = transform_data(df)
    load_data(df_clean, str(test_path))
    assert test_path.exists(), "Cleaned CSV was not saved"
