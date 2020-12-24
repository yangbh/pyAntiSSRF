# pyAntiSSRF

anti ssrf by hijack requests

supports py2 & py3

## install

`pip install pyAntiSSRF`


## usage

```python
import pyAntiSSRF

pyAntiSSRF.patchRequests()

import requests

# custom requests usage
requests.get("http://10.10.10.10/")

# patch requests by hijack requests.sessions.Session.request, default disable
requests.get("http://10.10.10.10/", anti_ssrf=False)

# raise Exception
requests.get("http://10.10.10.10/", anti_ssrf=True)
```

