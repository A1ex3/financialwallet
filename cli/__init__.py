import argparse
from record import Record

class Cli:
    def __init__(self):
        self.__record = Record()

    def run(self):
        parser = argparse.ArgumentParser(description='Financial Wallet CLI')
        subparsers = parser.add_subparsers(dest='command')

        add_parser = subparsers.add_parser('add', help='Add a new record')
        add_parser.add_argument('amount', type=float, help='Transaction amount')
        add_parser.add_argument('category', type=str, help='Category')
        add_parser.add_argument('date', type=str, help='Transaction date')
        add_parser.add_argument('description', type=str, help='Transaction description')

        update_parser = subparsers.add_parser('update', help='Update an existing record')
        update_parser.add_argument('index', type=int, help='Record index')
        update_parser.add_argument('--amount', type=float, help='Updated amount')
        update_parser.add_argument('--category', type=str, help='Updated category')
        update_parser.add_argument('--date', type=str, help='Updated date')
        update_parser.add_argument('--description', type=str, help='Updated description')

        balance_parser = subparsers.add_parser('get_balance', help='Get balance, income, and expenses')

        get_parser = subparsers.add_parser('get', help='Get all records')

        get_by_key_parser = subparsers.add_parser('get_by_key', help='Get records by key')
        get_by_key_parser.add_argument('by', type=str, choices=['amount', 'category', 'date'], help='Search key')
        get_by_key_parser.add_argument('value', help='Search value')

        args = parser.parse_args()
        command = args.command

        if command == 'add':
            self.add(args.amount, args.category, args.date, args.description)
        elif command == 'update':
            self.update(args.index, args.amount, args.category, args.date, args.description)
        elif command == 'get_balance':
            self.get_balance()
        elif command == 'get':
            self.get_all()
        elif command == 'get_by_key':
            self.get_by_key(args.by, self.convert_value(args.by, args.value))

    def convert_value(self, key, value):
        if key == 'amount':
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Invalid value for 'amount': {value}")
        return value

    def add(self, amount, category, date, description):
        result = self.__record.add(amount, category, date, description)
        print(result)

    def update(self, index, amount=None, category=None, date=None, description=None):
        result = self.__record.update(index, amount, category, date, description)
        print(result)

    def get_balance(self):
        balance = self.__record.get_balance()
        for line in balance:
            print(line)

    def get_all(self):
        records = self.__record.get()
        if records:
            for record in records:
                print(f"{record}\n")
        else:
            print("No records found.")

    def get_by_key(self, by: str, value: float | str):
        records = self.__record.get_by_key(by, value)
        if isinstance(records, str):
            print(records)
        else:
            if records:
                for record in records:
                    print(f"{record}\n")
            else:
                print(f"No records found for {by}: {value}")
