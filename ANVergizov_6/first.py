from requests import get

link = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = get(link)
text = response.text

res = []

with open('ngnix.txt', 'w', encoding='utf-8') as f:
    f.write(text)

f.close()

with open('ngnix.txt', 'r', encoding='utf-8') as f:
    for line in f:
        string = line.strip().split()
        res.append((string[0], string[5][1:], string[6]))

print(res)


