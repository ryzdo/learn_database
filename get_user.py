from models import User

my_user = User.query.first()
print(f"""Имя: {my_user.name}
Зарплата: {my_user.salary}
Email: {my_user.email}""")