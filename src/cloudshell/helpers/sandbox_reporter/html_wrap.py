"""
Helper methods to wrap text in html with semantic coloring
"""

SUCCESS_GREEN = "#00FF00"
ERROR_RED = "#EF5350"
WARN_YELLOW = "#FFFF00"
DEBUG_PURPLE = "#BA68C8"


def element_wrap(text: str, color="white", element="span", italicized=False):
    """ Wrap in target element, color, and font style """
    font_style = "italic" if italicized else "normal"
    return f"<{element} style='color: {color}; font-style: {font_style};'>{text}</{element}>"


def anchor_wrap(url: str, text: str):
    return (
        f"<a href={url} "
        f'style="text-decoration: underline" '
        f'target="_blank" '
        f'rel="noopener noreferrer">'
        f"{text}</a>"
    )


def success_wrap(text: str, element="span", italicized=False):
    return element_wrap(text, SUCCESS_GREEN, element, italicized)


def error_wrap(text: str, element="span", italicized=False):
    return element_wrap(text, ERROR_RED, element, italicized)


def warn_wrap(text: str, element="span", italicized=False):
    return element_wrap(text, WARN_YELLOW, element, italicized)


def debug_wrap(text: str, element="span", italicized=False):
    return element_wrap(text, DEBUG_PURPLE, element, italicized)
