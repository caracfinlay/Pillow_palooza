import pandas as pd


def load_data():
    # Load "data/airbnb_price.csv" as a DataFrame called prices.

    prices = pd.read_csv("data/prices.csv")

    # Load "data/airbnb_room_type.xlsx" as a DataFrame called xls, and the first
    # sheet from xls as a DataFrame called room_types.

    room_types = pd.read_excel("data/room_types.xlsx")

    # Load "data/airbnb_last_review.tsv" as a DataFrame called reviews.

    reviews = pd.read_csv("data/reviews.tsv", delimiter="\t")

    return prices, room_types, reviews
