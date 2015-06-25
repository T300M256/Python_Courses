import re

def phone_hide(text):
    # ...use a raw string constant!
    return re.subn(r"\d{3}-\d{4}", "XXX-XXXX", text)