"""
In addition to logging, "SandboxReporter" methods will also handle sending formatted html messages to sandbox console
This class is a "logger adapter" that uses duck typing of standard logger signature
"""
import inspect
import logging

from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.helpers.sandbox_reporter.sandbox_console import SandboxConsole

DEFAULT_STACK_CORRECTION = 3


class SandboxReporter:
    def __init__(self, api: CloudShellAPISession, reservation_id: str, logger: logging.Logger, stack_correction=0):
        """
        Stack correction is when you put sandbox reporter into a wrapper and want the parent function logged
        stack corrections will take effect only for python 3.8 and higher
        """
        self._api = api
        self._reservation_id = reservation_id
        self._logger = logger
        self._console = SandboxConsole(api, reservation_id)
        self._stack_correction = stack_correction

    @property
    def logger(self):
        """
        The underlying logger is always here to use directly
        Can be passed along to lower level functions to avoid unexpected console prints
        (Unless you are debugging and want everything dumped directly to console)
        """
        return self._logger

    @property
    def console(self):
        """
        The console printer can be used directly to print something without logging it
        If you don't care about logging, better to instantiate console independently
        """
        return self._console

    def _is_enabled_for(self, level):
        """
        Is this logger enabled for level 'level'?
        """
        return self.logger.isEnabledFor(level)

    def _log(self, level, msg, *args, **kwargs):
        """
        Delegate a log call to the underlying logger
        Adjust stack level for newer python versions, 3.8 and higher
        """
        sig = inspect.getfullargspec(self.logger._log)  # pylint: disable=protected-access
        if "stacklevel" in sig.args:  # Python 3.8 and above
            total_stacks = DEFAULT_STACK_CORRECTION + self._stack_correction
            self.logger.log(level, msg, *args, stacklevel=total_stacks, **kwargs)
        else:
            self.logger.log(level, msg, *args, **kwargs)

    def debug(self, msg, *args, console_print=True, console_prefix=True, **kwargs):
        """
        Delegate a debug call to the underlying logger
        Prints purple text with contextual prefix to console
        """
        if self._is_enabled_for(logging.DEBUG):
            self._log(logging.DEBUG, msg, *args, **kwargs)
            if console_print:
                if console_prefix:
                    msg = "[DEBUG] - " + msg
                self.console.debug_print(msg)

    def info(self, msg, *args, console_print=True, **kwargs):
        """
        Delegate an info call to the underlying logger
        Neutral color print, optional to set different html element such as H2, H3, etc
        The html signature is slightly different here to avoid un-necessary html wrapping on neutral color prints
        """
        if self._is_enabled_for(logging.INFO):
            self._log(logging.INFO, msg, *args, **kwargs)
            if console_print:
                self.console.sb_print(msg)

    def warning(self, msg, *args, console_print=True, **kwargs):
        """
        Delegate a warning call to the underlying logger
        Print Yellow text to console
        """
        if self._is_enabled_for(logging.WARNING):
            self._log(logging.WARNING, msg, *args, **kwargs)
            if console_print:
                self.console.warn_print(msg)

    def warning_header(self, msg, *args, console_print=True, **kwargs):
        """
        Delegate a warning call to the underlying logger
        Print Yellow text to console
        """
        if self._is_enabled_for(logging.WARNING):
            self._log(logging.WARNING, msg, *args, **kwargs)
            if console_print:
                self.console.warn_print(msg, html_element="h4", italicized=True)

    def error(self, msg, *args, console_print=True, **kwargs):
        """
        Delegate an error call to the underlying logger
        Print Red text to console
        """
        if self._is_enabled_for(logging.ERROR):
            self._log(logging.ERROR, msg, *args, **kwargs)
            if console_print:
                self.console.err_print(msg)

    def exception(self, msg, *args, console_print=True, **kwargs):
        """
        Delegate an exception call to the underlying logger
        Print Red text to console
        """
        if self._is_enabled_for(logging.ERROR):
            self._log(logging.ERROR, msg, *args, exc_info=True, **kwargs)
            if console_print:
                self.console.err_print(msg)

    def critical(self, msg, *args, console_print=True, console_prefix=True, **kwargs):
        """
        Delegate a critical call to the underlying logger.
        Print red text to console with additional contextual prefix
        """
        if self._is_enabled_for(logging.CRITICAL):
            self._log(logging.CRITICAL, msg, *args, **kwargs)
            if console_print:
                if console_prefix:
                    msg = "[CRITICAL] - " + msg
                self.console.err_print(msg)

    def success(self, msg, *args, console_print=True, **kwargs):
        """
        Delegate an info call to the underlying logger
        Neutral color print, optional to set different html element such as H2, H3, etc
        The html signature is slightly different here to avoid un-necessary html wrapping on neutral color prints
        """
        if self._is_enabled_for(logging.INFO):
            self._log(logging.INFO, msg, *args, **kwargs)
            if console_print:
                self.console.success_print(msg)
