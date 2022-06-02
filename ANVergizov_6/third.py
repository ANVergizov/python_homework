from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as user:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        users = user.read().splitlines()
        hobbys = hobby.read().splitlines()

if len(users) < len(hobbys):
    print(1)
else:
    users_hobbys = dict(zip_longest(users, hobbys, fillvalue=None))
    print(users_hobbys)
    with open('users_hobbys.txt', 'w', encoding='utf-8') as f:
        json.dumps(users_hobbys, f, ensure_ascii=False)



