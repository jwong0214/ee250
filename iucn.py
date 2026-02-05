import requests
import json

# WeatherAPI key
IUCN_API_KEY = 'ovnJDTtdhoKtVwiBgo3ZGQXzKoNkJAAtM5bd'  # TODO: Replace with your own WeatherAPI key

def get_assessment(scientific_name):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    BASE_URL = f"https://apiv3.iucnredlist.org/api/v4/taxa/scientific_name/{scientific_name}"
    params = {
        "token": IUCN_API_KEY
    }

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(BASE_URL, params=params)

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    if response.status_code == 200:
        data = response.json()

        if not data["result"]:
            print("No assessments found for this scientific name.")
            return

        # Print latest assessment (first result)
        assessment = data["result"][0]

        print(f"Scientific Name: {assessment.get('scientific_name', 'N/A')}")
        print(f"Red List Category: {assessment.get('red_list_category', 'N/A')}")
        print(f"Population Trend: {assessment.get('population_trend', 'N/A')}")
        print(f"Assessment Year: {assessment.get('year', 'N/A')}")

    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if response.status_code == 400:
            print(f"Error: 400. Bad request.")
        elif response.status_code == 401:
            print(f"Error: 401. Unauthorized. Check your API key.")
        elif response.status_code == 404:
            print(f"Error: 404. Scientific name not found.")
        else:
            print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    scientific_name = input("Enter a scientific name: ")

    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_assessment(scientific_name)
