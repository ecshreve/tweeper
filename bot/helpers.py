import json
import os.path
import pickle
import random


def clean_quote(quote_object):
    s = "".join(quote_object["lines"])
    return s


def persist_data(all_quotes):
    # Pickle our nice clean dict so we can use it later without having to parse
    # the JSON file again.
    with open('data.pickle', 'wb') as f:
        pickle.dump(all_quotes, f, pickle.HIGHEST_PROTOCOL)


def parse_json():
    try:
        ret = {}

        # Load the JSON file into a dictionary.
        with open("../data/quotes.json") as infile:
            data = json.load(infile)

        # Clean each quote and massage the data structure a bit so we have a
        # Map<show, []quote>.
        for quote in data:
            show_name = quote["show"]
            cq = clean_quote(quote)
            if show_name not in ret:
                ret[show_name] = []
            ret[show_name].append(cq)
        persist_data(ret)

    except Exception as e:
        print(e)


def setup_data():
    try:
        # Check if a pickle file already exists, if not then parse the JSON file
        # and pickle it.
        if not os.path.isfile('data.pickle'):
            parse_json()

        with open('data.pickle', 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            data = pickle.load(f)
            return data

    except Exception as e:
        print(e)


def get_random_quote():
    all_quotes = setup_data()

    # Pick a random key and a random element from that key's associated list
    # of quotes.
    k = random.choice(list(all_quotes.keys()))
    q = random.choice(all_quotes[k])

    # Remove the quote we randomly picked and persist.
    all_quotes[k].remove(q)
    persist_data(all_quotes)

    return [k, q]
