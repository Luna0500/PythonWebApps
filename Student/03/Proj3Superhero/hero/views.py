from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'heroes.html'

class SpidermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'id': 'Peter Parker',
            'strength1': 'Web Powers',
            'strength2': 'Spidey Senses',
            'strength3': 'Strength',
            'weakness1': 'His Naivete',
            'weakness2': 'Too Much Self Confidence',
            'weakness3': 'Ethyl Chloride Pesticide',
            'image': '/static/images/spiderman.webp'
        }
    
class ThingView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Thing',
            'id': 'Ben Grimm',
            'strength1': 'Great Teamwork',
            'strength2': 'Strength',
            'strength3': 'Durability',
            'weakness1': 'Emotional Vulnerability',
            'weakness2': 'Stubborn',
            'weakness3': 'Too Large To Interact With Small Objects',
            'image': '/static/images/thing.jpg'
        }
    
class CyborgView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Cyborg',
            'id': 'Victor Stone',
            'strength1': 'Technopath',
            'strength2': 'Strength',
            'strength3': 'Intellect',
            'weakness1': 'Maintaining His Humanity',
            'weakness2': 'Vulnerable To Magic',
            'weakness3': 'Vulnerable To Mind Control',
            'image': '/static/images/cyborg.webp'
        }
