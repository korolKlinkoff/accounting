from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def get_date():
    return datetime.date(datetime.today())


if __name__ == '__main__':
    print(get_date())
    print(calculate_salary())
    print(get_employees())
