import pandas as pd
import urllib.request
import shutil
import os

import json

import lyricsgenius
import argparse


def save_lyrics(artist_id, max_songs):
    artist = genius.search_artist(artist_id, max_songs=int(max_songs))
    artist.save_lyrics()


genius = lyricsgenius.Genius(
    "5y-Ynf87UKhSvEAB90B3eAT3P6Y-aiVft2qPYMVtyRVi85u4JhgOQQrXaJiTyJN0"
)
genius.remove_section_headers = True


def get_lyrics(artist_id, artist_name, max_songs):

    save_lyrics(artist_id, max_songs)

    FILENAME_LYRICS = "Lyrics_{}".format(artist_name.replace(" ", ""))
    with open(FILENAME_LYRICS + ".json") as json_data:
        data = json.load(json_data)

    all_lyrics = []

    for num_song in range(len(data["songs"])):
        song = data["songs"][num_song]

        lyrics = {}
        # lyrics attributes
        lyrics["lyrics"] = song["lyrics"]
        lyrics["release_date"] = song["release_date"]
        lyrics["release_date_for_display"] = song["release_date_for_display"]

        lyrics["full_title"] = song["full_title"]
        lyrics["featured_video"] = song["featured_video"]
        lyrics["header_image_thumbnail_url"] = song["header_image_thumbnail_url"]
        lyrics["header_image_url"] = song["header_image_url"]
        lyrics["lyrics_state"] = song["lyrics_state"]
        lyrics["song_art_image_thumbnail_url"] = song["song_art_image_thumbnail_url"]
        lyrics["song_art_image_url"] = song["song_art_image_url"]
        lyrics["title"] = song["title"]
        # lyrics["pageviews"] = song["stats"]["pageviews"]
        lyrics["title_with_featured"] = song["title_with_featured"]
        lyrics["featured_artists"] = song["featured_artists"]

        # artist attributes
        lyrics["artist_name"] = data["name"]
        lyrics["artist_id"] = data["id"]

        all_lyrics.append(lyrics)

    lyrics_df = pd.DataFrame.from_dict(all_lyrics)
    lyrics_df.to_csv("../data/lyrics_/" + FILENAME_LYRICS + "_clean.csv", index=False)


import argparse

parser = argparse.ArgumentParser(
    description="Get lyrics of an artist from Genius and save it into a csv file."
)

parser.add_argument("--artist_name", help="an integer for the accumulator")

parser.add_argument("--max_songs", help="Maximum number of songs.", default=None)

args = parser.parse_args()


if __name__ == "__main__":

    artist_id = args.artist_name.lower()
    artist_name = args.artist_name.lower().capitalize()
    max_songs = args.max_songs

    get_lyrics(artist_id, artist_name, max_songs)
