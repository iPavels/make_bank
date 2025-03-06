def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и значение для ключа state"""
    filtered_transactions = []
    for transaction in transactions:
        if transaction.get("state") == state:
            filtered_transactions.append(transaction)
    return filtered_transactions
