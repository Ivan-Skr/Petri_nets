from requests import get

print(get('http://127.0.0.1:8081/api/results').json())