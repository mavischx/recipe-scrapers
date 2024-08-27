from ._abstract import AbstractScraper


class App(AbstractScraper):
    @classmethod
    def host(cls):
        return "example.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

# Function to scrape using Template
def scrape_recipe(url):
    scraper = App()  # Create an instance of the Template class
    scraper.load(url)  # Assuming there's a method to load the URL
    return {
        'title': scraper.title(),
        'author': scraper.author(),
        'category': scraper.category(),
        'total_time': scraper.total_time(),
        'yields': scraper.yields(),
        'image': scraper.image(),
        'ingredients': scraper.ingredients(),
        'instructions': scraper.instructions(),
        'ratings': scraper.ratings(),
        'cuisine': scraper.cuisine(),
        'description': scraper.description(),
    }