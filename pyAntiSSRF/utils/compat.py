import sys

PY2 = sys.version_info[0] == 2

if not PY2:
    text_type = str
    string_types = (str,)
    from urllib.request import unquote, quote
    from urllib.parse import urlparse, urlencode
    import urllib.request as urllib2
    import urllib.parse as urllib
    long = int
    import queue as Queue
else:
    text_type = unicode
    string_types = (str, unicode)
    from urllib import unquote, quote, urlencode
    from urlparse import urlparse
    import urllib2
    import urllib
    import Queue


def to_bytes(text):
    """Transform string to bytes."""
    if isinstance(text, text_type):
        text = text.encode('utf-8')
    return text


def to_unicode(input_bytes, encoding='utf-8'):
    """Decodes input_bytes to text if needed."""
    if not isinstance(input_bytes, string_types):
        input_bytes = input_bytes.decode(encoding)
    return input_bytes

