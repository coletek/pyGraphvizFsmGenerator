# pyGraphvizFsmGenerator

Generate python-based state machine with a .dot graphviz file

```
cd example
xdot MyStateMachine.dot
python ../tools/GraphvizToStateMachine.py MyStateMachine.dot MyStateMachine > MyStateMachine.py
ln -s ../src/State.py State.py
python TestMyStateMachine.py
```
