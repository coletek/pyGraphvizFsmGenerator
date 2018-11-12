# EDIT this to suit states found in MyStateMachine.dot

from MyStateMachine import MyStateMachine

fsm = MyStateMachine()

print ("state=%s\n" % fsm.state)

print ("event=press_switch")
fsm.on_event('press_switch')
print ("state=%s\n" % fsm.state)

print ("event=press_switch")
fsm.on_event('press_switch')
print ("state=%s\n" % fsm.state)

print ("event=press_switch")
fsm.on_event('press_switch')
print ("state=%s\n" % fsm.state)

print ("event=got_error")
fsm.on_event('got_error')
print ("state=%s\n" % fsm.state)

print ("event=press_switch")
fsm.on_event('press_switch')
print ("state=%s\n" % fsm.state)




