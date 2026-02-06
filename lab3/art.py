import requests

def search_artworks_by_title(title):
    BASE_URL = "https://api.artic.edu/api/v1/artworks/search"
    params = {
        "q": title,
        "limit": 5,
        "fields": "id,title,artist_display,date_display"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        results = response.json().get("data", [])

        print(f"\nFiltered results for title containing '{title}':")
        print("---------------------")

        for art in results:
            artwork_title = art.get("title", "")

            if title.lower() in artwork_title.lower():
                print(f"Title: {artwork_title}")
                print(f"Artist: {art.get('artist_display', 'N/A')}")
                print(f"Date: {art.get('date_display', 'N/A')}")
                print(f"Artwork ID: {art.get('id')}")
                print("---------------------")
    else:
        if response.status_code == 400:
            print(f"Error: 400. Bad request. Check the artwork name")
        elif response.status_code == 404:
            print(f"Error: 404. Artwork not found.")
        else:
            print(f"Error: {response.status_code}. Something went wrong.")


if __name__ == "__main__":
    title = input("Enter artwork title: ").strip()
    search_artworks_by_title(title)