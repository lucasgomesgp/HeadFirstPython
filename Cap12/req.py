import requests

urls = ('http://headfirstlabs.com','http://orelly.com','http://twitter.com')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)