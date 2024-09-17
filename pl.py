import requests
import json

from pyflarum import FlarumUser
USER = FlarumUser(forum_url="FLARUM URL")

print(USER.get_discussion_by_id("10").get_author("fist_number"))
