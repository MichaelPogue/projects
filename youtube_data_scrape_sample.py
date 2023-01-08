# Import modules.
import os
import csv
import schedule
import pandas as pd
from os import path
from csv import writer
from googleapiclient.discovery import build
from dotenv import load_dotenv
from datetime import datetime

# Set API parameters. 
load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")
youtube = build('youtube', 'v3', developerKey = API_KEY)

# Primary function to get statistics.
class ytStatsBase:
    def __init__(self, API_KEY, CHANNEL_ID, youtube, channel_name):
        self.API_KEY = API_KEY
        self.CHANNEL_ID = CHANNEL_ID
        self.youtube = youtube

    # Get basic channel statistics.
    def get_channel_statistics(self):
        pass

    # Get individual video IDs through playlist. 
    def get_video_ids(self):
        pass

    # Get individual video details. 
    def get_video_details(self):
        pass

    # Transfer data into dataframes.
    def create_data_frame(channel_stats, video_details):
        pass

    # Generate personalized files.
    def create_files(dfc, dfv):
        pass

    # Gather new videos and append csv files.
    def append_new_videos_data(dfv):
        pass

    # Gather new videos and append csv files.
    def append_latest_statistics(dfv):
        pass

# Call functions.
yt = ytStatsBase
channel_stats, video_details = yt.get_channel_statistics(youtube), yt.get_video_details(youtube)
channel_name = channel_stats[0]['result_channel_name']
dfc, dfv = yt.create_data_frame(channel_stats, video_details)
yt.create_files(dfc, dfv)
yt.append_new_videos_data(dfv)
#yt.append_latest_statistics(dfv)