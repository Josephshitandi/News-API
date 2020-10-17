import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_newss(source):
    '''
    Function that gets the json response to our url request
    '''
    get_newss_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_newss_url) as url:
        get_newss_data = url.read()
        get_newss_response = json.loads(get_newss_data)

        news_results = None

        if get_newss_response['articles']:
            news_results_list = get_newss_response['articles']
            news_results = process_results(news_results_list)


    return news_results
