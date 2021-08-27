import json

import pprint


def CleanQuote(quote_object):
    s = "".join(quote_object["lines"])[:-1]
    return s


def ParseJson():
    ret = {}
    try:
        # Load the JSON file into a dictionary.
        with open("../data/quotes.json") as infile:
            data = json.load(infile)

        # Clean each quote and massage the data structure a bit so we have a
        # Map<show, []quote>.
        for quote in data:
            show_name = quote["show"]
            cq = CleanQuote(quote)
            if show_name not in ret:
                ret[show_name] = []
            ret[show_name].append(cq)

    except Exception as e:
        print(e)

    return ret
