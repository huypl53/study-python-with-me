# Python logging

- `logging.getLogger()` receives optinal argument as name of logger, if nothing is provided, root logger is returned. Use `logger.propagate = False` to stop foward log record to parent logger

- logger should be initiated in a separated module then imported before need-to-log module's import within main

- if module's logger doesn't have a `handler`, the log record is propagated to **higher-level logger** toward root logger

- if logger's log level is higher than handler's log level. No log is passed to that handler