# Test suite for main.py pipeline
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
import os
import main

def test_extract_returns_list():
    sample_data = [{
        "ID Nation": "01000US",
        "Nation": "United States",
        "ID Year": 2023,
        "Year": "2023",
        "Population": 332387540,
        "Slug Nation": "united-states"
    }]
    with patch('main.requests.get') as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {'data': sample_data}
        mock_get.return_value = mock_resp
        data = main.extract()
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["Nation"] == "United States"

def test_transform_returns_dataframe():
    sample_data = [{
        "ID Nation": "01000US",
        "Nation": "United States",
        "ID Year": 2023,
        "Year": "2023",
        "Population": 332387540,
        "Slug Nation": "united-states"
    }]
    df = main.transform(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert 'Year' in df.columns
    assert 'Population' in df.columns
    assert df.iloc[0]['Nation'] == "United States"

def test_load_creates_csv(tmp_path):
    df = pd.DataFrame([{
        "ID Nation": "01000US",
        "Nation": "United States",
        "ID Year": 2023,
        "Year": "2023",
        "Population": 332387540,
        "Slug Nation": "united-states"
    }])
    with patch('main.print'):
        main.load(df)
    assert os.path.exists('population_data_test.csv')
    # Optionally, check contents
    loaded = pd.read_csv('population_data_test.csv')
    assert loaded.iloc[0]['Nation'] == "United States"
    # Clean up
    os.remove('population_data_test.csv')

def test_main_pipeline(monkeypatch):
    sample_data = [{
        "ID Nation": "01000US",
        "Nation": "United States",
        "ID Year": 2023,
        "Year": "2023",
        "Population": 332387540,
        "Slug Nation": "united-states"
    }]
    monkeypatch.setattr(main, 'extract', lambda: sample_data)
    monkeypatch.setattr(main, 'transform', lambda data: pd.DataFrame(data))
    with patch('main.load') as mock_load:
        main.main()
        mock_load.assert_called()
