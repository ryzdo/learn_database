import csv
import time

from db import db_session
from models import Salary


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city', 'address', 'company',
                  'job', 'phone_number', 'email', 'date_of_birth', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        salary_data = []
        for row in reader:
            salary_data.append(row)
        save_salary_data(salary_data)


def save_salary_data(salary_data):
    db_session.bulk_insert_mappings(Salary, salary_data)
    db_session.commit()


if __name__ == '__main__':
    start = time.time()
    read_csv('salary.csv')
    print('Данные загружены за ', time.time() - start)
    # Данные загружены за  0.802269697189331
