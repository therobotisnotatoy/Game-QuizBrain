import requests
import html


parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "easy"
}


def api_connection_response() -> list:

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    return response.json()["results"]


def quiz_data() -> list:

    json_data = api_connection_response()
    question_data = []

    for i in range(0, len(json_data)):
        question_data.append({"text": html.unescape(json_data[i]["question"]),
                              "answer": json_data[i]["correct_answer"]}
                             )

    return question_data
