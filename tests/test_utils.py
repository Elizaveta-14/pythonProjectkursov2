from unittest.mock import patch


from src.utils import HH


@patch("json.loads")
def test_get_work(mock_get):
    """Проверяет на возвращение списка"""
    mock_get.return_value = ""
    hh_instance = HH(mock_get)
    assert hh_instance.add_to_file() == ""


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_no_found(mock_file):
    """Проверяет на возвращение пустого списка при ошибке"""
    transactions =HH("data/json")
    assert transactions == []