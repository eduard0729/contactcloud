import falcon
from .model import Contact
class ContactCRUD(object):

	def on_get(self, req, resp):
        # You can access self.session here
        # self.session.add(foo)
        # self.session.commit()