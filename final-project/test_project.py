import pytest, requests
from unittest.mock import patch
from project import Medicine, fetch_drug_info, get_drug_names, validate_result

def test_medicine_creation():
    fake_data = {
        "openfda": {"brand_name": ["Advil"], "generic_name": ["Ibuprofen"]},
        "purpose": ["Purpose: Pain Reliever"]
    }

    med = Medicine("Advil", fake_data)

    assert med.name == "Advil"
    assert med.med_info["Brand Name"] == "Advil"
    assert med.med_info["Purpose"] == "Pain Reliever"

def test_medicine_missing_fields():
    med = Medicine("Unknown", {"openfda": {}})
    assert med.med_info["Brand Name"] == "N/A"
    assert med.caution_info["Warnings"] == "N/A"

@patch("builtins.input", side_effect=["Advil", "Tylenol", "q"])
def test_get_drug_names(mock_input):
    assert get_drug_names() == ["Advil", "Tylenol"]

@patch("requests.get")
def test_fetch_drug_info_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"results": "some data"}

    assert fetch_drug_info("Advil") == {"results": "some data"}

@patch("requests.get")
def test_fetch_drug_info_not_found(mock_get):
    mock_get.return_value.status_code = 404

    with pytest.raises(ValueError):
        fetch_drug_info("FakeDrug123")

@patch("requests.get")
def test_fetch_drug_info_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException
    with pytest.raises(ConnectionError):
        fetch_drug_info("Advil")


def test_validate_result_fail():
    bad_data = {
        "results": [
            {"openfda": {"brand_name": ["Different Med"]}}
        ]
    }
    with pytest.raises(ValueError):
        validate_result(bad_data, "MyMed")

def test_validate_result_success():
    good_data = {"results": [{"openfda": {"brand_name": ["Advil"]}}]}
    result = validate_result(good_data, "Advil")
    assert result == {"openfda": {"brand_name": ["Advil"]}}




