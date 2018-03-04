from fbchat import log, Client
from fbchat.models import *
from cleverwrap import CleverWrap
import argparse


class EchoBot(Client):

	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(author_id, thread_id)
		self.markAsRead(author_id)

		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

		if message_object.text == 'stop':
			self.send(Message(text='Turning off ):'),thread_id=thread_id, thread_type=thread_type)
			self.listening = False

		cb_message = cw.say(message_object.text)
	
		if author_id != self.uid:
			self.send(Message(text=cb_message),thread_id=thread_id, thread_type=thread_type)



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help="enter facebook email")
	parser.add_argument("password", help="facebook password")
	parser.add_argument("api", help="cleverbot api")
	args = parser.parse_args()
	
	email = args.email
	password = args.password
	clever_key = args.api

	cw = CleverWrap(clever_key)
	client = EchoBot(email, password)
	client.listen()
	client.logout()