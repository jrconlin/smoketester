# plan

* **simplify run** - 
currently scenarios are in same file. Can we either store all there or import the run code easily?
* **cleaner logs** - 
make logs more human/machine friendly, not just
```
    INFO:twisted:Starting factory <autobahn.twisted.websocket.WebSocketClientFactory object at 0x7f78a1e049d0>
```
* **scenario only runs** - disable/remove `aplt.runner:run_testplan`? Call `RunnerHarness` directly?
* 