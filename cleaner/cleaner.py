inp = {
    "show": "The O.C.",
    "lines": [
        "Alex",
        ": Marissa's not... happy.",
        "\n",
        "Julie",
        ": Marissa and happy parted ways about her 16th birthday but have you met her new friends sullen and vindictive?",
        "\n",
        "Alex",
        ": No, the only ones she's brought over to the house are scared and overwhelmed.\""]}


def CleanQuote(quote_object):
    s = "".join(quote_object["lines"])[:-1]
    print(s)


CleanQuote(inp)
