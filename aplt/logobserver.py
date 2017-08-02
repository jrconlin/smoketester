import io
import json
import sys
import time

from twisted.logger import (
    formatEventAsClassicLogText,
    formatEvent,
    LogLevel,
    ILogObserver,
    globalLogBeginner,
    globalLogPublisher

)

from zope.interface import implementer

began_logging = False


def begin_or_register(observer, redirectStandardIO=False, **kwargs):
    global began_logging

    if not began_logging:
        globalLogBeginner.beginLoggingTo(
            [observer],
            redirectStandardIO=redirectStandardIO,
            **kwargs
        )
        began_logging = True
    else:
        globalLogPublisher.addObserver(observer=observer)


@implementer(ILogObserver)
class JSONLogger(object):

    def __init__(self, logger_name, log_level="debug",
                 log_format="json", log_output="stdout"):
        self._start = time.time()
        self.logger_name = logger_name
        self._filename = None
        self._log_level = LogLevel.lookupByName(log_level)
        output = log_output.lower()
        if output == "stdout":
            self._output = sys.stdout
        elif output == "none":
            self._output = None
        else:
            self._filename = log_output
        try:
            self.format_event = getattr(self, "{}_format".format(log_format))
        except AttributeError:
            self.format_event = formatEventAsClassicLogText

    def __call__(self, event):
        import pdb; pdb.set_trace()

    def emit(self, event):
        if event.get("log_level", LogLevel.info) < self._log_level:
            return
        text = self.format_event(event)

        if self._output:
            self._output.write(unicode(text)+"\n")
            self._output.flush()

    def human_format(self, event):
        ev = formatEvent(event)
        return "{:0>7.3f} {:>8} {}".format(
            event['log_time'] - self._start,
            event['log_level'].name.upper(),
            ev)

    def json_format(self, event):
        ev = formatEvent(event)
        for item in ['format', 'log_source', 'log_factory', 'log_legacy',
                     'log_text', 'log_format',
                     'log_namespace', 'factory', 'log_logger', 'message']:
            if item in event:
                del(event[item])
        if 'reason' in event:
            event['reason'] = repr(event['reason'])
        event['message'] = ev
        event['log_level'] = event['log_level'].name
        return json.dumps(event)

    def start(self):
        if self._filename:
            self._output = io.open(self._filename, "a", encoding="utf-8")
        begin_or_register(self)

    def stop(self):
        globalLogPublisher.removeObserver(self)
        if self._filename:
            self._output.close()
            self._output = None