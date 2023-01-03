from gensim.summarization import summarize
from newspaper import Article
import requests


def getNaverNewsLink(search_word, page, limit):
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
    print("REQUEST URL: ", response.request.url)
    
    result = response.json()

    news_list = result['items']

    news_links = []
    for news in news_list:
        # if(news['originallink'] == ''):
        #     news_links.append(news['link'])
        # else:
        #     news_links.append(news['originallink'])
        news_links.append(news['link'])
        
            
    return news_links

def summarizeNews(url):
    news = Article(url, language='ko')
    news.download()
    news.parse()

    original_content = ". ".join(news.text.split("."))
    original_content = ". ".join(news.text.split(".  "))
    summary_content = summarize(original_content, word_count=40)

    # try:
    #     summary_content = summarize(original_content, word_count=40)
    # except:
    #     original_content = ". ".join(news.text.split("."))
    #     summary_content = summarize(original_content, word_count=40)

    print("------------------------------------------------------------------------------------------------------------------------")
    print("url: ", url)
    print("original content: ", original_content);
    print("------------------------------------------------------------------------------------------------------------------------")
    print()

    json_obj = {}
    json_obj['title'] = news.title
    json_obj['link'] = url

    # if(summary_content == ''):
    #     original_content = ". ".join(original_content.split("."))
    #     summary_content = summarize(original_content, word_count=40)
    
    json_obj['content'] = summary_content

    return json_obj