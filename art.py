import requests

BASE_URL = "https://api.artic.edu/api/v1/artworks/search"

def search_artworks_by_title(title):
    params = {
        "q": title,
        "limit": 5,
        "fields": "id,title,artist_display,date_display"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}")
        return

    results = response.json().get("data", [])

    print(f"\nFiltered results for title containing '{title}':")
    print("-" * 50)

    for art in results:
        artwork_title = art.get("title", "")

        print(f"Title: {artwork_title}")
        print(f"Artist: {art.get('artist_display', 'N/A')}")
        print(f"Date: {art.get('date_display', 'N/A')}")
        print(f"Artwork ID: {art.get('id')}")
        print("-" * 50)
        # STRICT title-only filter
        # if title.lower() in artwork_title.lower():
        #     print(f"Title: {artwork_title}")
        #     print(f"Artist: {art.get('artist_display', 'N/A')}")
        #     print(f"Date: {art.get('date_display', 'N/A')}")
        #     print(f"Artwork ID: {art.get('id')}")
        #     print("-" * 50)


if __name__ == "__main__":
    title = input("Enter artwork title: ").strip()
    search_artworks_by_title(title)
