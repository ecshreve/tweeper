import json
import os.path
import pickle


def CleanQuote(quote_object):
    s = "".join(quote_object["lines"])[:-1]
    return s


def ParseJson():
    try:
        ret = {}

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

        # Pickle our nice clean dict so we can use it later without having to parse
        # the JSON file again.
        with open('data.pickle', 'wb') as f:
            pickle.dump(ret, f, pickle.HIGHEST_PROTOCOL)

    except Exception as e:
        print(e)


def SetupData():
    try:
        # Check if a pickle file already exists, if not then parse the JSON file
        # and pickle it.
        if not os.path.isfile('data.pickle'):
            ParseJson()

        with open('data.pickle', 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            data = pickle.load(f)
            return data

    except Exception as e:
        print(e)
