"""
todo: 예산 저장해두기
todo: csv -> Oracle
todo: pandas 사용하기
todo: 상대경로 -> 절대경로
todo: 시각화 구현하기
"""

from src.manager import ExpenseManger
from src.utils import *

MENU: list = [0, 1, 2, 3, 4, 5]


def main():
    print("------------------가계부 프로그램 부팅 중------------------")

    app: ExpenseManger = ExpenseManger()

    print("------------------가계부 프로그램 가동------------------")

    while True:
        raw_chosen_menu: str = input("지출 입력: 1, 총 지출 확인: 2, 예산 확인: 3, 입금 입력: 4, 총 입금 확인: 5, 프로그램 종료: 0 ")

        # 사용자 입력 검사
        check_validation: int | None = to_int(raw_chosen_menu)
        if check_validation is not None and check_validation in MENU:  # 제대로 입력했다면
            processed_chosen_menu: int = int(raw_chosen_menu)

            # case 지출 입력
            if processed_chosen_menu == 1:
                print("------------------------------------------------------")
                print("------------------지출 입력 프로그램 가동------------------")

                user_item_name_1: str = input("어디에 지출했는 지 입력하세요: ")
                user_amount_1: int | None
                while True:  # 숫자를 입력할 때까지 반복
                    user_amount_1 = to_int(input("얼마를 지출하였습니까? "))
                    if isinstance(user_amount_1, int):
                        break
                    else:
                        print("숫자를 입력해라;;")

                while True:  # 제대로 된 형식의 날짜를 입력할 때까지 반복
                    user_spend_at_1 = input("지출한 날짜를 입력하세요(오늘이면 그냥 엔터): ")
                    if user_spend_at_1 == "" or check_date_format(user_spend_at_1):
                        break

                    print("YYYY-MM-DD형식으로 입력해주세요.")

                if user_spend_at_1:
                    app.insert_expense(item_name=user_item_name_1, amount=user_amount_1, spend_at=user_spend_at_1)
                else:
                    app.insert_expense(item_name=user_item_name_1, amount=user_amount_1)

            # case 총 지출
            elif processed_chosen_menu == 2:
                print("------------------------------------------------------")
                print("------------------총 지출 확인 프로그램 가동 ------------------")

                user_date_2: str
                while True:  # 제대로 입력할 때까지 반복
                    user_date_2 = input("총 지출액을 확인할 날짜를 입력해주세요(오늘이면 그냥 엔터): ")
                    if user_date_2 == "" or check_date_format(user_date_2):
                        break

                    print("YYYY-MM-DD형식으로 입력해주세요.")

                if user_date_2:
                    total: int = app.select_expense(target_date=user_date_2)
                    print(f"{user_date_2} 총 지출액: {total}")
                else:
                    total: int = app.select_expense()
                    print(f"오늘 총 지출액: {total}")

            # case 예산 확인
            elif processed_chosen_menu == 3:
                print("------------------------------------------------------")
                print("------------------총 예산 확인 프로그램 가동------------------")

                budget: int = app.get_budget()
                print(f"남은 예산 {budget}\n")

            # case 입금 입력
            elif processed_chosen_menu == 4:
                print("------------------------------------------------------")
                print("------------------입금 입력 프로그램 가동------------------")

                user_sender_4 = input("누가 입금하는 지 적어주세요: ")
                user_amount_4: int | None
                while True:  # 숫자를 입력받을 때까지 반복
                    user_amount_4 = to_int(input("얼마를 입금하는 지 적어주세요: "))
                    if isinstance(user_amount_4, int):
                        break

                    print("숫자를 입력해라;;")

                user_deposit_at_4: str
                while True:  # 제대로 된 날짜 형식 입력할 때까지 반복
                    user_deposit_at_4 = input("언제 입금하는 지 적어주세요(오늘이면 그냥 엔터): ")
                    if user_deposit_at_4 == "" or check_date_format(user_deposit_at_4):
                        break

                    print("YYYY-MM-DD형식으로 입력해주세요.")

                if user_deposit_at_4:
                    app.insert_deposit(sender=user_sender_4, amount=user_amount_4, deposit_at=user_deposit_at_4)
                else:
                    app.insert_deposit(sender=user_sender_4, amount=user_amount_4)

            # case 총 입금
            elif processed_chosen_menu == 5:
                user_date_5: str
                while True:
                    user_date_5 = input("총 입금액을 확인할 날짜를 입력해주세요(오늘이면 그냥 엔터): ")
                    if user_date_5 == "" or check_date_format(user_date_5):
                        break

                    print("YYYY-MM-DD형식으로 입력해주세요.")

                if user_date_5:
                    total: int = app.select_deposit(target_date=user_date_5)
                    print(f"{user_date_5} 총 입금액: {total}")
                else:
                    total: int = app.select_deposit()
                    print(f"오늘 총 입금액: {total}")

            # case 프로그램 종료
            elif processed_chosen_menu == 0:
                print("------------------프로그램 종료------------------")
                break

        else:  # raw_chosen_menu가 제대로 입력되지 않은 경우
            print("똑바로 입력해라;;")


if __name__ == "__main__":
    main()
