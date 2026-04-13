import os, re

DIR = r"c:\Users\johnp\OneDrive\Documents\Claude\Web Design"

recipes = {
    "recipe-spring-pasta.html": [
        "4-cheese ravioli",
        "Leeks",
        "Spring peas",
        "Crème fraîche",
        "Tomato sauce base",
    ],
    "recipe-salmon-chicken.html": [
        "Salmon fillets",
        "Butter",
        "Lemon",
        "Green beans",
        "Whole chicken",
        "Potatoes",
        "Compound butter",
        "Rotating seasonal vegetables",
    ],
    "recipe-halloween-meatballs.html": [
        "Ground meat",
        "Breadcrumbs",
        "Egg",
        "Seasonings",
    ],
    "recipe-grilled-chicken.html": [
        "Chicken pieces",
        "Mashed potatoes",
        "Peas",
        "Homemade butter",
        "Pan drippings (for gravy)",
    ],
    "recipe-french-toast.html": [
        "Thick-cut bread",
        "Eggs",
        "Milk",
        "Cinnamon",
        "Vanilla",
        "Homemade honey butter",
    ],
    "recipe-lasagna.html": [
        "Lasagna noodles",
        "Ricotta cheese",
        "Mozzarella",
        "Parmesan",
        "Meat or tomato sauce",
    ],
    "recipe-chicken-noodle-soup.html": [
        "Rotisserie chicken",
        "Egg noodles",
        "Carrots",
        "Celery",
        "Chicken broth",
        "Aromatics (onion, garlic, bay leaf, thyme)",
    ],
    "recipe-yellow-cake.html": [
        "All-purpose flour",
        "Sugar",
        "Eggs",
        "Butter",
        "Buttermilk",
        "Vanilla extract",
        "Pillsbury chocolate frosting",
    ],
    "recipe-salmon-two-ways.html": [
        "Salmon fillets",
        "Teriyaki glaze",
        "Sesame seeds",
        "Green onion",
        "Lemon",
        "Fresh herbs",
        "Roasted potatoes",
        "Garlic green beans",
    ],
    "recipe-lemon-salmon.html": [
        "Salmon fillets",
        "Lemon",
        "Fresh herbs",
        "Orzo",
        "Sun-dried tomatoes",
        "Green beans",
    ],
    "recipe-chili.html": [
        "Ground beef or turkey",
        "Canned beans",
        "Canned tomatoes",
        "Onion",
        "Bell peppers",
        "Chili spices",
        "Cornmeal (for muffins)",
        "Butter, egg, milk (for muffins)",
    ],
    "recipe-lemon-scones.html": [
        "All-purpose flour",
        "Butter",
        "Sugar",
        "Heavy cream",
        "Lemon zest and juice",
        "Eggs (for curd)",
        "Butter (for curd)",
    ],
    "recipe-lettuce-wraps.html": [
        "Ground turkey",
        "Butter lettuce leaves",
        "Water chestnuts",
        "Hoisin sauce",
        "Soy sauce",
        "Fresh ginger",
        "Garlic",
        "Green onion",
        "Sesame oil",
    ],
    "recipe-coq-au-vin.html": [
        "Whole chicken pieces",
        "Red wine",
        "Lardons (bacon lardons)",
        "Mushrooms",
        "Pearl onions",
        "Thyme & bay leaf",
        "Garlic",
        "Mashed potatoes",
        "Roasted green beans",
        "Lyonnaise salad ingredients",
    ],
    "recipe-honeycomb.html": [
        "Sugar",
        "Golden syrup",
        "Baking soda",
        "Dark chocolate (for dipping)",
    ],
    "recipe-wrap-bar.html": [
        "Ground turkey",
        "Butter lettuce leaves",
        "Diced fresh vegetables",
        "Hoisin sauce",
        "Soy sauce",
        "Sesame oil",
        "Toppings bar (green onion, sesame seeds, lime, etc.)",
    ],
    "recipe-turkey-chili.html": [
        "Ground turkey",
        "Canned tomatoes",
        "Kidney beans",
        "Onion",
        "Garlic",
        "Bell peppers",
        "Cumin",
        "Chili powder",
        "Paprika",
    ],
    "recipe-chicken-madeira.html": [
        "Chicken breasts (pounded thin)",
        "Madeira or Marsala wine",
        "Mushrooms",
        "Beef broth",
        "Butter",
        "Fresh herbs",
    ],
    "recipe-homemade-soup.html": [
        "Whole chickens (bones roasted at 350°F for 2 hrs)",
        "Chicken breasts",
        "Carrots",
        "Celery",
        "Egg noodles",
        "Salt, pepper, seasoning",
    ],
    "recipe-pasta-vodka.html": [
        "Handmade pasta",
        "San Marzano tomatoes",
        "Vodka",
        "Heavy cream",
        "Shallots",
        "Garlic",
        "Pecorino Romano",
        "Red pepper flakes",
        "Fresh basil",
    ],
    "recipe-pot-roast.html": [
        "Chuck and bottom round (~6 lbs)",
        "Cabernet Sauvignon",
        "Onion",
        "Carrots",
        "Garlic",
        "Beef broth",
        "Tomato paste",
        "Fresh herbs",
    ],
    "recipe-pot-roast-marrow.html": [
        "Chuck roast",
        "Beef bone marrow",
        "Root vegetables",
        "Red wine",
        "Beef broth",
        "Mashed potatoes",
    ],
    "recipe-julia-coq-au-vin.html": [
        "Whole chicken",
        "Burgundy wine",
        "Lardons",
        "Pearl onions",
        "Mushrooms",
        "Cognac",
        "Butter",
        "Thyme & bay leaves",
    ],
}

UL_PATTERN = re.compile(
    r'(<ul style="font-family:\'Lato\'[^>]+>).*?(</ul>)',
    re.DOTALL
)

for filename, ingredients in recipes.items():
    path = os.path.join(DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    items = "\n".join(f"            <li>{ing}</li>" for ing in ingredients)
    new_ul = f'\g<1>\n{items}\n          \g<2>'
    new_html = UL_PATTERN.sub(new_ul, html, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Updated: {filename} ({len(ingredients)} ingredients)")

print("All done!")
