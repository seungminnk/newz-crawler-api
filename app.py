from flask import Flask, request

from news_crawler import getNaverNewsLink, summarizeNews

app = Flask(__name__)

@app.route('/news/list')
def getNewsList():
    query = request.args.get('query')
    page = request.args.get('page')
    limit = request.args.get('limit')

    if(query is None or query == ''):
        return 'Query param is required'
    
    if(page is None or page == '' or int(page) < 1):
        page = 1
    
    if(limit is None or limit == '' or int(limit) < 1):
        limit = 3

    news_links = getNaverNewsLink(query, page, limit)

    news_obj = []
    for i in news_links:
        print(i)
        news_obj.append(summarizeNews(i))
    return news_obj
 
if __name__ == '__main__':
    app.run(port=7000, debug=True)