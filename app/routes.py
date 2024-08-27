from flask import request, jsonify
from. import app, db
from .models import Recipe
from .scraper import scrape_recipe
import requests

@app.route('/api/scrape', method=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        recipe_data = scrape_recipe(url)
        return jsonify(recipe_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/api/recipes', method=['POST'])
def save_recipe():
    data = request.json
    recipe = Recipe(title=data['title'],ingredients=data['ingredients'], instructions=data['instructions'], url=data.get('url'))
    db.session.add(recipe)
    db.session.commit()
    return jsonify({'message':'Recipe saved!'})

@app.route('/api/recipes/<int:id>', method=['PUT'])
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    data = request.json
    recipe.title = data.get('title',recipe.title)
    recipe.ingredients = data.get('ingredients',recipe.ingredients)
    recipe.instructions = data.get('instructions',recipe.instructions)
    db.session.commit()
    return jsonify({'message':'Recipe updated!'})

@app.route('/api/recipes/<int:id>', method=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message':'Recipe deleted!'})

@app.route('/api/recipes', method=['GET'])
def get_recipes():
    recipe = Recipe.query.all()
    return jsonify({'id': r.id, 'title': r.title, 'ingredients': r.ingredients, 'instructions': r.instructions, 'url': r.url}for r in recipe)
