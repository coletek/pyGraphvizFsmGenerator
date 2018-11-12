import sys
import re
import pprint

filename = sys.argv[1]
state_machine_name = sys.argv[2]

lines = (open(filename).read())
#print (data)

state_machine = {}
first_state = ""

def snake_to_camel(word):
    import re
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

def process_transition(matchobj):
    global state_machine
    global first_state
    
    line = matchobj.group(0)
    splits = line.split(' -> ')
    start_state = splits[0]
    end_state = splits[1]

    searchObj = re.search(r'(\w+)\[label="(.*)"\]', line, re.M|re.I)
    end_state = searchObj.group(1)
    label = searchObj.group(2)

    start_state = snake_to_camel(start_state) + "State"
    end_state = snake_to_camel(end_state) + "State"

    if not first_state:
        first_state = start_state
    
    item = (end_state, label)
    if start_state in state_machine:
        state_machine[start_state].append(item)
    else:
        state_machine[start_state] = [item]

    #print ("")
    #print ("process_transition")
    #print (line)
    #print ("start_state=%s" % (start_state))
    #print ("end_state=%s" % (end_state))
    #print ("label=%s" % (label))

for l in lines.splitlines():
    lines = re.sub(r'\w+ -> .+', process_transition, l)

#pp = pprint.PrettyPrinter(indent=1)
#pp.pprint(state_machine)

print ('from %sStates import *\n'
       'from State import *' % state_machine_name)

for start_state in state_machine:
    print ('\nclass %s(%sMasterState):\n'
           '    def __init__(self):\n'
           '        %sMasterState.__init__(self)\n'
           '        print("%sInit")\n'
           '    def on_event(self, event):' \
           % (start_state, start_state, start_state, start_state))
    c = 0
    for t in (state_machine[start_state]):
        if c == 0:
            start = "if"
        else:
            start = "elif"
        print ("        %s event == '%s':\n"
               "            return %s()" % (start, t[1], t[0]))
        c += 1
    print "        return self"

print ("")
print ('class %s(object):\n'
       '    def __init__(self):\n'
       '        self.state = %s()\n'
       '    def on_event(self, event):\n'
       '        self.state = self.state.on_event(event)' \
       % (state_machine_name, first_state))
