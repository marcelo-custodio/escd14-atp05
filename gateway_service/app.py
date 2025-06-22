import os
import requests
from ariadne import QueryType, MutationType, make_executable_schema, gql
from ariadne.asgi import GraphQL

# carrega schema
type_defs = gql(open("schema.graphql").read())

REST_URL = os.getenv("REST_URL", "http://contacts:8000")

query = QueryType()
mutation = MutationType()

@query.field("contact")
def resolve_contact(*_, id):
    resp = requests.get(f"{REST_URL}/contacts/{id}")
    resp.raise_for_status()
    return resp.json()

@query.field("contacts")
def resolve_contacts(*_):
    resp = requests.get(f"{REST_URL}/contacts")
    resp.raise_for_status()
    return resp.json()

@mutation.field("createContact")
def resolve_create_contact(*_, input):
    resp = requests.post(f"{REST_URL}/contacts", json=input)
    resp.raise_for_status()
    return resp.json()

schema = make_executable_schema(type_defs, [query, mutation])
app = GraphQL(schema, debug=True)