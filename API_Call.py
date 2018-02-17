from API_INFO import API_KEY, APP_ID
from typing import List
import requests

API_POST = "https://trackapi.nutritionix.com/v2/natural/nutrients"


class APICall:
    """
    PUT SOMETHING HERE LATER
    """
    def send_post(self, foods: str) -> List[dict]:
        """Returns a list of dictionaries of each food passed
        as a request."""
        query = self.make_query(foods)
        headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
        # Send POST to Nutritionix API for nutrition.
        r = requests.post(API_POST, data=query, headers=headers)
        all_foods = r.json()['foods']

        return all_foods

    def make_query(self, ingredients: str) -> dict:
        """
        Create the query we send to the API.
        """
        json_post = {"query": ingredients}
        return json_post
