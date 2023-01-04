from gensim.summarization import summarize
from newspaper import Article
import requests


def getNewsLink(search_word, page, limit):
    url = 'https://openapi.naver.com/v1/search/news.json'

    headers = {
        'X-Naver-Client-Id': '',
        'X-Naver-Client-Secret': ''
    }

    params = {
        'query': search_word,
        'sort': 'sim',
        'start': page,
        'display': limit
    }

    response = requests.get(url, params=params, headers=headers)
    
    result = response.json()

    news_list = result['items']

    result = []
    for news in news_list:
        links = {}

        links['link'] = news['link']
        links['original_link'] = news['originallink']

        result.append(links)
        
    return result


def summarizeNews(links):
    link = links['link']
    original_link = links['original_link']

    url = link

    news = Article(link, language='ko')
    news.download()
    news.parse()

    title = news.title
    original_content = news.text

    remove_keyword = '모두에게 보여주고 싶은 기사라면?beta'

    if remove_keyword in news.text:
        news = Article(original_link, language='ko')
        news.download()
        news.parse()

        original_content = news.text

    original_content = ". ".join(original_content.split("."))
    original_content = ". ".join(original_content.split(".  "))
    original_content = " ".join(original_content.split("\n"))

    summary_content = summarize(original_content, word_count=40)

    json_obj = {}
    json_obj['title'] = title
    json_obj['link'] = url
    json_obj['content'] = summary_content

    return json_obj