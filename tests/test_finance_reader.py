from unittest.mock import MagicMock, mock_open, patch

from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel


def test_read_transactions_from_csv():
    mock_csv_content = "date,amount,category\n2025-08-01,100,Food\n2025-08-02,200,Transport\n"
    with (
        patch("builtins.open", mock_open(read_data=mock_csv_content)),
        patch(
            "csv.DictReader",
            return_value=[
                {"date": "2025-08-01", "amount": "100", "category": "Food"},
                {"date": "2025-08-02", "amount": "200", "category": "Transport"},
            ],
        ) as mock_reader,
    ):

        result = read_transactions_from_csv("fake_path.csv")

        assert len(result) == 2
        assert result[0]["amount"] == "100"
        mock_reader.assert_called_once()


def test_read_transactions_from_excel():
    mock_workbook = MagicMock()
    mock_sheet = MagicMock()

    headers_row = [MagicMock(value="date"), MagicMock(value="amount"), MagicMock(value="category")]

    data_rows = [
        ("2025-08-01", 100, "Food"),
        ("2025-08-02", 200, "Transport"),
    ]

    mock_sheet.iter_rows.side_effect = [iter([headers_row]), iter(data_rows)]

    mock_workbook.active = mock_sheet

    with patch("openpyxl.load_workbook", return_value=mock_workbook):
        result = read_transactions_from_excel("fake_path.xlsx")

        assert len(result) == 2
        assert result[0]["date"] == "2025-08-01"
        assert result[1]["amount"] == 200
