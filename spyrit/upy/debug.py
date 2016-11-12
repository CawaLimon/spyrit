import pyb
import sys
import scheduler

messages = []

##
#
# Print a debug message and add it to the list.
def log(message):
    global messages
    print(message)
    messages.append(message)
    
##
#
# Display up to the last DEBUG_MESSAGES_SHOW in the messages list.
def print_latest_messages():
    count = DEBUG_MESSAGES_TO_SHOW
    global messages
    if count > len(messages):
        count = len(messages)
    for message in messages[-count:]:
        print(message)
        
##
#
# Display all debug messages.
def print_all():
    global messages
    for message in messages:
        print(message)
        
##
#
# Clear the list of debug messages.
def clear():
    global messages
    messages = ['Cleared debug messages']