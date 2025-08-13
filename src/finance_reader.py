import csv
import openpyxl
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    headers = [cell.value for cell in next(sheet.iter_rows(min_row=1, max_row=1))]
    transactions = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        transaction = dict(zip(headers, row))
        transactions.append(transaction)

    return transactions
