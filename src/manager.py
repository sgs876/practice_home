import csv, json
from src.utils import get_today, get_today_ym


class ExpenseManger:
    def __init__(self):
        self.budget_path: str = "database/budget.json"
        self.expense_data_path: str = "database/expenses.csv"
        self.deposit_data_path: str = "database/deposits.csv"
        self.expenses_field_names: list[str] = ["item_name", "amount", "spend_at"]
        self.deposits_field_names: list[str] = ["sender", "amount", "deposit_at"]

        self.check_and_reset_budget()

    # 예산 초기화
    def check_and_reset_budget(self):
        today_ym: str = get_today_ym()

        with open(self.budget_path, 'r', encoding="utf-8-sig") as f1:
            data = json.load(f1)
            if data["last_reset_ym"] != today_ym:
                data["budget"] = 200000
                data["last_reset_ym"] = today_ym

            with open(self.budget_path, 'w', encoding="utf-8-sig") as f2:
                json.dump(data, f2, indent=4, ensure_ascii=False)

    # 지출 입력
    def insert_expense(self, item_name: str, amount: int, spend_at: str = get_today()):
        new_row: dict = {
            "item_name": item_name,
            "amount": amount,
            "spend_at": spend_at
        }

        with open(self.expense_data_path, 'a', encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.expenses_field_names)
            writer.writerow(new_row)

        # --------------------------------------------------------------------
        # 예산에서 빼기
        with open(self.budget_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            data["budget"] -= amount

        with open(self.budget_path, 'w', encoding="utf-8-sig") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("완료")

    # 지출 확인
    def select_expense(self, target_date: str = get_today()) -> int:
        total = 0

        with open(self.expense_data_path, 'r', encoding="utf-8-sig") as f:
            reader: csv.DictReader = csv.DictReader(f)
            for row in reader:
                if row["spend_at"] == target_date:
                    total += int(row["amount"])

        return total

    # 예산 확인
    def get_budget(self) -> int:
        with open(self.budget_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

        return data["budget"]

    # 입금 입력
    def insert_deposit(self, sender: str, amount: int, deposit_at: str = get_today()):
        new_row: dict = {
            "sender": sender,
            "amount": amount,
            "deposit_at": deposit_at
        }

        with open(self.deposit_data_path, 'a', encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=self.deposits_field_names)
            writer.writerow(new_row)

    def select_deposit(self, target_date: str = get_today()) -> int:
        total = 0

        with open(self.deposit_data_path, 'r', encoding="utf-8-sig") as f:
            reader: csv.DictReader = csv.DictReader(f)
            for row in reader:
                if row["deposit_at"] == target_date:
                    total += int(row["amount"])

        return total
