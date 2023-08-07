## Bug description
`hide_input_in_errors` does not work for fast api responses. 
`input` field is present in both responses, however models configured to hide the error
Check `src/user.py` for configuration


## Reproduce steps

### Init env

```bash
poetry shell
poetry install
python -m src
```

### Sample #1

```bash
curl --request POST \
  --url http://localhost:8000/user_1 \
  --header 'Content-Type: application/json' \
  --data '{"name": "1"}'
```

Response

```json
{"detail":[{"type":"missing","loc":["body","firstName"],"msg":"Field required","input":{"name":"1"},"url":"https://errors.pydantic.dev/2.1/v/missing"}]}
```


### Sample #2

```bash
curl --request POST \
  --url http://localhost:8000/user_2 \
  --header 'Content-Type: application/json' \
  --data '{"name": "1"}'
```

Response

```json
{"detail":[{"type":"missing","loc":["body","firstName"],"msg":"Field required","input":{"name":"1"},"url":"https://errors.pydantic.dev/2.1/v/missing"}]}
```
