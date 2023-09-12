from pathlib import Path
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
import json

class HeroDetailView(TemplateView):
    template_name = "hero.html"
    def get_context_data(self, **kwargs):
        numID = kwargs["numID"]

        data = open('./static/data/heroes.json').read()
        jsonData = json.loads(data)
        heroData = jsonData[numID]
        title = heroData["title"]
        id = heroData["id"]
        strength1 = heroData["strength1"]
        strength2 = heroData["strength2"]
        strength3 = heroData["strength3"]
        weakness1 = heroData["weakness1"]
        weakness2 = heroData["weakness2"]
        weakness3 = heroData["weakness3"]
        imagePath = heroData["imagePath"]

        return {
            "title": title,
            "id": id,
            "strength1": strength1,
            "strength2": strength2,
            "strength3": strength3,
            "weakness1": weakness1,
            "weakness2": weakness2,
            "weakness3": weakness3,
            "imagePath": imagePath,
            "photo": imagePath
        }

def photo_list():
    def photo_details(i, f):
        return dict(id=i, file=f)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos

class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())