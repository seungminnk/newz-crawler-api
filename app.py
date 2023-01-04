from flask import Flask, request, jsonify, make_response

from news_crawler import getNewsLink, summarizeNews

app = Flask(__name__)

@app.route('/news/list')
def getNewsList():
    query = request.args.get('query')
    page = request.args.get('page')
    limit = request.args.get('limit')

    if(query is None or query == ''):
        return make_response("'query' parameter is required!"), 400
    
    if(page is None or page == '' or int(page) < 1):
        page = 1
    
    if(limit is None or limit == '' or int(limit) < 1):
        limit = 3

    news_links = getNewsLink(query, page, limit)

    news_obj = []
    for i in news_links:
        news_obj.append(summarizeNews(i))

    return jsonify(news_obj)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')