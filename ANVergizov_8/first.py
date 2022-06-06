import re

def email_parse(email):
    email_dict = {}
    if_valid = re.match(r'\w+@\w+\.\w+', email)
    if if_valid:
        email_dict['username'] = re.split(r'@', email)[0]
        email_dict['domain'] = re.findall(r'@\w+.\w+', email)[0]
        print(email_dict)
    else:
        raise ValueError(f'ValueError: wrong email {email}')


email_parse('domdom@dom.ru')
email_parse('gonevegan@gb.ru')
email_parse('wrongmail.ru')
