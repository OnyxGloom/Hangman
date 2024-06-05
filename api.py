import requests
import os
from dotenv import load_dotenv

def formRequest():
    load_dotenv()
    apiKey = os.getenv("APIKEY")
    formID = os.getenv("FORMID")

    url =f"https://eu-api.jotform.com/form/{formID}/submissions?apiKey={apiKey}"

    response = requests.get(url)
    data = response.json()
    wordList=[]
    submissions = data.get('content', [])
    for submission in submissions:
        answers = submission.get('answers', {})
        name_answer = answers.get('6', {}).get('answer', 'No name provided')
        wordList.append(name_answer)
    return wordList

