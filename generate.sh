#!/bin/bash

curl -X GET "https://integrations-service.tractian.com/tractian/openapi.json" -H "accept: application/json" >openapi.json

uv run python3 -m json.tool openapi.json >openapi.json

# Generate the client
uv run openapi-python-client generate --url https://integrations-service.tractian.com/tractian/openapi.json --output-path tractian_api --config config.yaml --overwrite

# Format generated code for readability
uv run black tractian_api
