import cgi
from google.appengine.api import users
import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><input type="submit" name="content" value="On"></div>
      <div><input type="submit" name ="content" value="Off"></div>
    </form>
  </body>
</html>
"""
BACK_PAGE ="""\
<html>
  <body>
    <form action="/" method="get">
      <div><input type="submit" name ="content" value="Back"></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')
        self.response.write(BACK_PAGE)
       

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
