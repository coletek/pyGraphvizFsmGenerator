# EDIT this to suit states found in MyStateMachine.dot

from State import *

class OnStateMasterState(State):
    def __init__(self):
        State.__init__(self)
        print ("On doing cool stuff")

class OffStateMasterState(State):
    def __init__(self):
        State.__init__(self)
        print ("Off doing cool stuff")

class ErrorStateMasterState(State):
    def __init__(self):
        State.__init__(self)
        print ("Error doing cool stuff")
