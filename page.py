import requests
import json

class Page:
    def __init__(self, page_id):
        self.page_id = page_id
        self.process();

    def process(self):
        res = requests.get(f"https://www.finn.no/bap/forsale/ad.html?finnkode={self.page_id}")

        html = res.text

        with open("test.html", "w") as txt:txt.write(html)

        startIndex = html.find(f"\"adId\":{self.page_id},\"brand\":")-1
        endIndex   = html.find("shouldLoadHotjar")+24

        full_data = json.loads(html[startIndex:endIndex])

        self.full_data = full_data

        self.ad_id = full_data["adId"]
        self.brand = full_data["brand"]

        self.user_owner = full_data["userOwner"]
        self.object_user_id = full_data["objectUserId"]
        self.object_data = full_data["objectData"]

        self.price = self.object_data["ad"]["price"]
        self.title = self.object_data["ad"]["title"]
        self.description = self.object_data["ad"]["description"]

        self.extras = self.object_data["ad"]["extras"]
        self.images = self.object_data["ad"]["images"]
        self.categories = self.object_data["ad"]["category"]
        self.location = self.object_data["ad"]["location"]

        self.sold = "disposed" in self.object_data["ad"]
        