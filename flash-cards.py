import cgi
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import os
from google.appengine.ext.webapp import template

class Card(db.Model):
    author = db.UserProperty()
    question = db.StringProperty(multiline=True)
    answer = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        cards_query = Card.all().order('-date')
        cards = cards_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            current_user = users.get_current_user()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = ''

        template_values = {
            'cards': cards,
            'url': url,
            'url_linktext': url_linktext,
            'current_user': current_user,
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
        
class Create(webapp.RequestHandler):
	def get(self):
	
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			current_user = users.get_current_user()
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			current_user = ''
            
		template_values = {
			'url': url,
			'url_linktext': url_linktext,
			'current_user': current_user,
			}
		path = os.path.join(os.path.dirname(__file__), 'create.html')
		self.response.out.write(template.render(path, template_values))
		
class Test(webapp.RequestHandler):
	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			current_user = users.get_current_user()
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			current_user = ''
            
		template_values = {
			'url': url,
			'url_linktext': url_linktext,
			'current_user': current_user,
			}
		path = os.path.join(os.path.dirname(__file__), 'test.html')
		self.response.out.write(template.render(path, template_values))

class CardSet(webapp.RequestHandler):
    def post(self):
        card = Card()

        if users.get_current_user():
            card.author = users.get_current_user()

        card.question = self.request.get('question')
        card.answer = self.request.get('answer')
        card.put()
        self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/create', Create),
                                      ('/test', Test),
                                      ('/cardset', CardSet)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()