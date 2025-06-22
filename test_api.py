import requests

GQL = "http://localhost:8001"  # GraphQL gateway

# 1) criar um contato
create_q = """
mutation($c: ContactInput!) {
  createContact(input: $c) { id name category phones { number type } }
}
"""
variables = {
  "c": {
    "name": "João Silva",
    "category": "family",
    "phones": [
      {"number": "+5511999998888", "type": "mobile"},
      {"number": "32321234",     "type": "landline"}
    ]
  }
}
resp = requests.post(GQL, json={"query": create_q, "variables": variables})
print("CREATE:", resp.json())

# 2) listar todos
list_q = "{ contacts { id name category } }"
resp = requests.post(GQL, json={"query": list_q})
print("LIST:", resp.json())

# 3) buscar por id
id0 = resp.json()["data"]["contacts"][0]["id"]
get_q = f'{{ contact(id: {id0}) {{ id name phones {{ number type }} }} }}'
resp = requests.post(GQL, json={"query": get_q})
print("GET:", resp.json())