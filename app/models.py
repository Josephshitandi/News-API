class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,image,description,date):
        self.title = title
        self.image = image
        self.description = description
        self.date = date
        
class Article:

    all_articles = []

    def __init__(self,title,image,article):
        self.title = title
        self.imageurl = imageurl
        self.article = article


    def save_article(self):
        article.all_articles.append(self)


    @classmethod
    def clear_articles(cls):
        article.all_articles.clear()

    @classmethod
    def get_articles(cls,title):

        response = []

        for article in cls.all_articles:
            if article.title == title:
                response.append(article)

        return response