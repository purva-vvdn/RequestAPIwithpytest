

import requests

url = "https://qa-unicloud.vvdncloud.com/auth/realms/unicloud/login-actions/authenticate?session_code=UtbL63q9DqMDVqYRES7rLPqAo-l0Wv8DruE7juDfT-0&execution=451e6d48-a6bf-4f21-b03a-1dcb26b266a5&client_id=react-base-app&tab_id=u0yNd4qXsYk"

payload = 'username=unicloud_admin&password=PassWord%401&rememberMe=on&credentialId='
headers = {
  'cookie': 'KEYCLOAK_LOCALE=en; AUTH_SESSION_ID=9a9966b8-0fdb-4099-86e9-a0c90d82c41a.keycloak-0-48795; AUTH_SESSION_ID_LEGACY=9a9966b8-0fdb-4099-86e9-a0c90d82c41a.keycloak-0-48795; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjNzY5NTliMC0zN2IwLTRkNGYtYTQyYy0yZDg0MTEwYjkxYTEifQ.eyJjaWQiOiJyZWFjdC1iYXNlLWFwcCIsInB0eSI6Im9wZW5pZC1jb25uZWN0IiwicnVyaSI6Imh0dHBzOi8vcWEtdW5pY2xvdWQudnZkbmNsb3VkLmNvbS8iLCJhY3QiOiJBVVRIRU5USUNBVEUiLCJub3RlcyI6eyJzY29wZSI6Im9wZW5pZCIsImlzcyI6Imh0dHBzOi8vcWEtdW5pY2xvdWQudnZkbmNsb3VkLmNvbS9hdXRoL3JlYWxtcy91bmljbG91ZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9xYS11bmljbG91ZC52dmRuY2xvdWQuY29tLyIsInN0YXRlIjoiN2EzYWQ4ZGUtM2FhOC00ZGFhLWExNTctYzA0NDZhYzc4Yzg4Iiwibm9uY2UiOiJlZjBmN2NlMC0zNWEzLTQ5NjUtODg5OC1hMTc2YTFjYzA4ZjIiLCJyZXNwb25zZV9tb2RlIjoiZnJhZ21lbnQifX0.mWhs86Pl4mtHSI5I4tNo-eiK2a7UQ6GE0prOMyPUO70; AUTH_SESSION_ID=4c05435e-5b57-44a9-8609-e9dd29d82480.keycloak-0-48795; AUTH_SESSION_ID_LEGACY=4c05435e-5b57-44a9-8609-e9dd29d82480.keycloak-0-48795'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)
print("HI...............................")
print(response.cookies.get('KC_STATE_CHECKER'))

