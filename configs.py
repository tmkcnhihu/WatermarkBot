# (c) @VideosWaterMarkRobot

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH")
	STREAMTAPE_API_PASS = os.environ.get("dq6hzjewe27bmwdn", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("y7bhafa3bxfxudzk", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	UPDATES_CHANNEL = os.environ.get("-1002233071560", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("6052303737", 1960040199))
	CAPTION = "By @PBX1_BOTS"
	BOT_USERNAME = os.environ.get("X1WatermarkAdderBot", "VideosWaterMarkRobot")
	DATABASE_URL = os.environ.get("mongodb+srv://david:surya@cluster12.f7tpy44.mongodb.net/")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note:   If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/VideosWaterMarkRobot).__

Desgined by @VideosWaterMarkRobot
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
