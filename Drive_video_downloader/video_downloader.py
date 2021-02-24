#! /usr/bin/python3
import urllib
import os 
import argparse
from urllib.parse import parse_qsl, unquote
parser = argparse.ArgumentParser()

parser.add_argument("--file_id", type=str,help="FILE_ID") 
parser.add_argument("--drive_id",type=str,help="for __Secure-3PSID cookie")
parser.add_argument("--drive_stream",type=str,help="for DRIVE_STREAM cookie")

args = parser.parse_args()

FILE_ID = args.file_id 
SECURE_3PSID=args.drive_id
DRIVE_STREAM=args.drive_stream

GET_INFO_URL =  'https://drive.google.com/u/1/get_video_info?docid='+FILE_ID
os.system('rm get_video_info*')

ARIA2C_PREFIX=f"aria2c --header='Cookie: __Secure-3PSID={SECURE_3PSID}'  --header='Cookie: DRIVE_STREAM={DRIVE_STREAM} '"
get_video_cmd=f'{ARIA2C_PREFIX} {GET_INFO_URL}'
os.system(get_video_cmd)

with open('get_video_info', 'r') as f:
    raw = f.read()
    parsed = parse_qsl(unquote(raw))
    for pair in parsed:
        if pair[0] == "url":
            best_quality_pair = pair

VIDEO_LINK=best_quality_pair[1]

download_cmd=f'{ARIA2C_PREFIX} "{str(VIDEO_LINK)}"'
os.system(download_cmd)
