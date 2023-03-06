# pyGraphvizFsmGenerator

Generate python-based state machine with a .dot graphviz file

```
cd example
xdot MyStateMachine.dot
python3 ../tools/GraphvizToStateMachine.py MyStateMachine.dot MyStateMachine > MyStateMachine.py
ln -s ../src/State.py State.py
python3 TestMyStateMachine.py
```

It should be noted that I've created TestMyStateMachine.py and
MyStateMachineStates.py to demostrate.

Normally you'll need to create your own MyStateMachineStates.py to
implement what the state does. And your own test hardness
TestMyStateMachine.py

The benefit of this tool is so you can keep the state implementation
static, but the transisision logic is dynamically created in the
generated code based on the .dot file.
