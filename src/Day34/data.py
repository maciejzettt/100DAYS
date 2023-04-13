import requests

_parameters = {
    "amount": 10,
    "type": "boolean"
}
_response = requests.get(url='https://opentdb.com/api.php', params=_parameters)

_question_data_raw = _response.json()
question_data = _question_data_raw.get("results")
