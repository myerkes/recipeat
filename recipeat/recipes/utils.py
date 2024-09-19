from recipe_scrapers import scrape_html
from recipe_scrapers._exceptions import WebsiteNotImplementedError
from ingredient_parser import parse_ingredient
import requests

class RecipeScraper:
    def __init__(self, url):
        html = requests.get(url, headers={"User-Agent": f"Recipe Scraper"}).content
        try:
            self.scraper = scrape_html(html, org_url=url)
        except WebsiteNotImplementedError as e:
            self.scraper = scrape_html(html, org_url=url, wild_mode=True)

    def title(self):
        return self.scraper.title()

    def ingredients(self):
        return self.scraper.ingredients()
    
    def parsed_ingredients(self):
        ingredients = self.scraper.ingredients()
        return [self.parse_ingredient(ingredient) for ingredient in ingredients]

    def parse_ingredient(self, ingredient_str):
        return parse_ingredient(ingredient_str)

    def ingredient_groups(self):
        return self.scraper.ingredient_groups()
    
    def instructions(self):
        return self.scraper.instructions()
    
    def instructions_list(self):
        return self.scraper.instructions_list()
    
    def to_json(self):
        return self.scraper.to_json()
    
    def yields(self):
        return self.scraper.yields()

    def total_time(self):
        return self.scraper.total_time()
    
    def image(self):
        return self.scraper.image()
    
    def links(self):
        return self.scraper.links()