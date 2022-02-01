"""
Methods to format html and send api message to sandbox console
HTML wrap module functions have the semantic color encapsulated
"""
from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.helpers.sandbox_reporter import html_wrap


class SandboxConsole:
    def __init__(self, api: CloudShellAPISession, reservation_id: str):
        """ Store api and sandbox id for api call """
        self._api = api
        self._reservation_id = reservation_id

    def sb_print(self, message: str):
        """ Shorthand alias for printing to sandbox console """
        self._api.WriteMessageToReservationOutput(self._reservation_id, message)

    def html_print(self, message, color="white", html_element="span", italicized=False):
        """ Flexible method for custom html color and elements """
        self.sb_print(html_wrap.element_wrap(message, color, html_element, italicized))

    def err_print(self, message: str, html_element="span", italicized=False):
        """ Print red message to highlight errors """
        self.sb_print(html_wrap.error_wrap(message, html_element, italicized))

    def success_print(self, message: str, html_element="span", italicized=False):
        """ Print green message to highlight passing action """
        self.sb_print(html_wrap.success_wrap(message, html_element, italicized))

    def warn_print(self, message: str, html_element="span", italicized=False):
        """ Print yellow message to highlight important messages """
        self.sb_print(html_wrap.warn_wrap(message, html_element, italicized))

    def debug_print(self, message: str, html_element="span", italicized=False):
        """ Print yellow message to highlight important messages """
        self.sb_print(html_wrap.debug_wrap(message, html_element, italicized))

    def anchor_tag_print(self, url: str, text: str):
        """ For wrapping text in html anchor tag; opens link in new tab by default """
        self.sb_print(html_wrap.anchor_wrap(url, text))
