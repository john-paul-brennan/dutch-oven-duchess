import re

path = r"c:\Users\johnp\OneDrive\Documents\Claude\Web Design\recipes.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Map of identifying title text -> slug
links = [
    ("Cabernet-Braised Pot Roast", "recipe-pot-roast.html"),
    ("Pasta alla Vodka", "recipe-pasta-vodka.html"),
    ("Dutch Oven Rotisserie Chicken Noodle Soup", "recipe-chicken-noodle-soup.html"),
    ("Classic Yellow Cake with Chocolate Frosting", "recipe-yellow-cake.html"),
    ("Spring Pasta", "recipe-spring-pasta.html"),
    ("Weeknight Salmon", "recipe-salmon-chicken.html"),
    ("Halloween Meatballs", "recipe-halloween-meatballs.html"),
    ("Sunday Grilled Chicken", "recipe-grilled-chicken.html"),
    ("French Toast with Homemade Honey Butter", "recipe-french-toast.html"),
    ("The Cheesiest Lasagna", "recipe-lasagna.html"),
    ("Salmon Two Ways", "recipe-salmon-two-ways.html"),
    ("Lemon Herb Salmon", "recipe-lemon-salmon.html"),
    ("Crock Pot Chili", "recipe-chili.html"),
    ("Lemon Scones with Lemon Curd", "recipe-lemon-scones.html"),
    ("Turkey Lettuce Wraps", "recipe-lettuce-wraps.html"),
    ("Coq au Vin with Mashed Potatoes", "recipe-coq-au-vin.html"),
    ("Homemade Honeycomb Candy", "recipe-honeycomb.html"),
    ("Ground Turkey Lettuce Wrap Bar", "recipe-wrap-bar.html"),
    ("Turkey Chili", "recipe-turkey-chili.html"),
    ("Chicken Madeira", "recipe-chicken-madeira.html"),
    ("Homemade Chicken Noodle Soup", "recipe-homemade-soup.html"),
    ("Classic Pot Roast with Beef Bone Marrow", "recipe-pot-roast-marrow.html"),
    ("Julia Child", "recipe-julia-coq-au-vin.html"),
]

# Replace <div class="recipe-card cursor-pointer"> with <a href="..."><div class="recipe-card cursor-pointer">
# and the closing </div>\n\n        </div> pattern with </div></a>
# Strategy: find each card block and wrap it

old_open = '<div class="recipe-card cursor-pointer">'
new_open_template = '<a href="{slug}" style="display:block;"><div class="recipe-card cursor-pointer">'
old_close = '        </div>\n\n        <div class="recipe-card cursor-pointer">'

# Split on card dividers and process
# Actually, let's find each card and replace based on title

for title_hint, slug in links:
    # Find the card containing this title hint
    pattern = r'(<div class="recipe-card cursor-pointer">(?:(?!</div>\n\n\s+(?:<div|</div>)).)*?' + re.escape(title_hint) + r'.*?</div>\s*</div>)'

# Simpler approach: replace each <div class="recipe-card cursor-pointer"> with an anchor,
# based on which title follows. Let's just do string replacement card by card.

# Find all card blocks
card_pattern = re.compile(
    r'<div class="recipe-card cursor-pointer">.*?</div>\s*</div>',
    re.DOTALL
)

cards = card_pattern.findall(html)
print(f"Found {len(cards)} cards")

new_html = html
for title_hint, slug in links:
    # Find the card that contains this title
    for card in cards:
        if title_hint in card:
            wrapped = f'<a href="{slug}" style="display:block;">{card}</a>'
            new_html = new_html.replace(card, wrapped, 1)
            print(f"Linked: {title_hint} -> {slug}")
            break

with open(path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Done!")
