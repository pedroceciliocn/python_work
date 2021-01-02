messages = ['a', 'b', 'c', 'd', 'vsf']
sent_messages = []

#import module_name
import sending_messages

sending_messages.send_messages(messages, sent_messages)
sending_messages.show_messages(sent_messages)

#from module_name import function_name
from sending_messages import send_messages, show_messages

send_messages(messages, sent_messages)
show_messages(sent_messages)

#from module_name import function_name as fn
from sending_messages import send_messages as sdm

sdm(messages, sent_messages)

from sending_messages import show_messages as shm

shm(sent_messages)

#import module_name as mn
import sending_messages as smsg

smsg.send_messages(messages, sent_messages)
smsg.show_messages(sent_messages)

#from module_name import *
from sending_messages import *

send_messages(messages, sent_messages)
show_messages(sent_messages)

