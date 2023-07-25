# pylint: disable-all
import requests

def search_news(query):
    """
    Searches the News API for articles based on the given query.

    Args:
        query (str): The search query.

    Returns:
        None

    Raises:
        Any specific exceptions raised by the code, if applicable.
    """
    api_key = "9ad15860ec644be8a8fefd37f413bb50"
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={'9ad15860ec644be8a8fefd37f413bb50'}"
   
    # pylint: disable=E1101
    response = requests.get(url)
    data = response.json()

    # Handle the response data here
    # You can access the news articles or perform any other actions
    articles = data['articles']
    return articles

def gen_content(query):
    api_key = "9ad15860ec644be8a8fefd37f413bb50"
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={'9ad15860ec644be8a8fefd37f413bb50'}"

    response = requests.get(url)
    data = response.json()

    articles = data['articles']
    return articles





# from pprint import pprint
# pprint(search_news('tate'))



    # for article in articles:
    #     title = article['title']
    #     author = article['author']
    #     description = article['description']
    #     # Process and display the article information as desired
    #     print(f"Title: {title}")
    #     print(f"Author: {author}")
    #     print(f"Description: {description}")
    #     print()