from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin, RoomsMixin

from socketio.sdjango import namespace

from CustomUser.models import User

@namespace('/chat')
class EventNameSpace(BaseNamespace, RoomsMixin, BroadcastMixin):
	connected_users = []

	def initialize(self):
		pass

	def on_join(self, room):
		import pdb; pdb.set_trace()
		self.room = room
		self.join(room)
		return True	

	def on_user_entered(self, user):
		self.connected_users.append(user)
		self.emit_to_room(self.room, 'announcement', '%s' %user)
		return user

	def on_user_message(self, user, msg):
		import pdb;pdb.set_trace()
		self.emit_to_room(self.room, 'msg_to_room', user, msg )
		print msg
		return True
