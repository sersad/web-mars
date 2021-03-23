from pprint import pprint
from requests import get, post, delete

# pprint(get('http://localhost:8080/api/jobs').json())
# pprint(get('http://localhost:8080/api/jobs/1').json())

# Запрос юзеров
# pprint(get('http://localhost:8080/api/v2/users').json())

# Добавление пользоватля
# pprint(post('http://localhost:8080/api/v2/users',
#            json={'surname': 'API',
#                  'name': 'User',
#                  'age': 99,
#                  'position': 'ROOT',
#                  'speciality': 'worker',
#                  'address': 'module_1',
#                  'email': 'a@a.a',
#                  'hashed_password': '1',
#                  }).json())


# # Запрос Пользователя:
# print(get('http://localhost:8080/api/v2/users/7').json())
#
# # Удаления Пользователя:
# print(delete('http://localhost:8080/api/v2/users/7').json())


# Запрос JOBS
# pprint(get('http://localhost:8080/api/v2/jobs').json())

# Добавление JOBS
# pprint(post('http://localhost:8080/api/v2/jobs',
#             json={'team_leader': 1,
#                   'job': 'Jobs from API',
#                   'work_size': 10,
#                   'collaborators': '1, 2, 3',
#                   }).json())

# # Запрос JOBS:
# pprint(get('http://localhost:8080/api/v2/jobs/7').json())

# # Запрос JOBS  не существ
# pprint(get('http://localhost:8080/api/v2/jobs/99').json())
#
# # Удаления JOBS:
pprint(delete('http://localhost:8080/api/v2/jobs/7').json())
