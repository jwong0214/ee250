import requests
import json

BASE_URL = "https://api.artic.edu/api/v1/artworks/search"

def search_artworks(title):
    """
    Searches for artworks by title using the Art Institute of Chicago API.
    """

    params = {
        "q": title,
        "limit": 5   # number of results to return
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get("data", [])

        if not results:
            print("No artworks found.")
            return

        print(f"\nSearch results for '{title}':")
        print("-" * 40)

        for art in results:
            print(f"Title: {art.get('title', 'N/A')}")
            print(f"Artist: {art.get('artist_display', 'N/A')}")
            print(f"Date: {art.get('date_display', 'N/A')}")
            print(f"Artwork ID: {art.get('id', 'N/A')}")
            print("-" * 40)

    else:
        print(f"Error {response.status_code}: Unable to fetch artworks.")


if __name__ == "__main__":
    title = input("Enter artwork title or keyword: ").strip()
    search_artworks(title)
