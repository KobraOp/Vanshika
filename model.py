import json
import re
from google import genai

class Model:
    def __init__(self, json_file):
        self.client = genai.Client(api_key="AIzaSyDvOQxLXW-eQg0uk-1_8iWqAXqLjsWzPy8")
        self.qa_data = self.load_json(json_file)

    def load_json(self, json_file):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for item in data["questions_answers"]:
            item["question"] = self.clean_text(item["question"])
        
        return data["questions_answers"]

    def clean_text(self, text):
        return re.sub(r"[^a-zA-Z0-9\s]", "", text)

    def search_local_data(self, query):
        cleaned_query = self.clean_text(query).lower()
        for item in self.qa_data:
            if cleaned_query in item["question"].lower():
                return item["answer"]
        return None

    def generate_response(self, query):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=query
        )
        return response.text

    def get_answer(self, query):
        answer = self.search_local_data(query)
        if answer:
            return answer
        else:
            return self.generate_response(query)
