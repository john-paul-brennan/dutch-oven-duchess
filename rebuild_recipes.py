path = r"c:\Users\johnp\OneDrive\Documents\Claude\Web Design\recipes.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Cards data: (title, image, category, slug, stars, mb_class)
top_rated = [
    ("Cabernet-Braised Pot Roast", "recipe-pot-roast.jpg", "Dutch Oven", "recipe-pot-roast.html", "mb-1"),
    ("Pasta alla Vodka", "recipe-pasta-vodka.jpg", "Pasta", "recipe-pasta-vodka.html", "mb-1"),
    ("Dutch Oven Rotisserie Chicken Noodle Soup", "recipe-chicken-noodle-soup.jpg", "Dutch Oven", "recipe-chicken-noodle-soup.html", "mb-1"),
    ("Classic Yellow Cake with Chocolate Frosting", "recipe-yellow-cake.jpg", "Dessert", "recipe-yellow-cake.html", "mb-1"),
]

all_recipes = [
    ("Spring Pasta \u2014 Ravioli in Tomato Cr\u00e8me Fra\u00eeche", "recipe-spring-pasta.jpg", "Pasta", "recipe-spring-pasta.html"),
    ("Weeknight Salmon &amp; Meal-Prep Roast Chicken", "recipe-salmon-chicken.jpg", "Meal Prep", "recipe-salmon-chicken.html"),
    ("Halloween Meatballs", "recipe-halloween-meatballs.jpg", "Dinner", "recipe-halloween-meatballs.html"),
    ("Sunday Grilled Chicken &amp; Mashed Potatoes", "recipe-grilled-chicken.jpg", "Dinner", "recipe-grilled-chicken.html"),
    ("French Toast with Homemade Honey Butter", "recipe-french-toast.jpg", "Breakfast", "recipe-french-toast.html"),
    ("The Cheesiest Lasagna", "recipe-lasagna.jpg", "Pasta", "recipe-lasagna.html"),
    ("Salmon Two Ways", "recipe-salmon-two-ways.jpg", "Dinner", "recipe-salmon-two-ways.html"),
    ("Lemon Herb Salmon with Sun-Dried Tomato Orzo", "https://placehold.co/300x220/9b7c5e/fff?text=Lemon+Salmon", "Dinner", "recipe-lemon-salmon.html"),
    ("Crock Pot Chili &amp; Cornbread Muffins", "https://placehold.co/300x220/c8856b/fff?text=Chili", "Slow Cooker", "recipe-chili.html"),
    ("Lemon Scones with Lemon Curd", "https://placehold.co/300x220/f5c8d8/fff?text=Lemon+Scones", "Baking", "recipe-lemon-scones.html"),
    ("Turkey Lettuce Wraps", "https://placehold.co/300x220/8faa7c/fff?text=Lettuce+Wraps", "Lunch", "recipe-lettuce-wraps.html"),
    ("Coq au Vin with Mashed Potatoes &amp; Lyonnaise Salad", "https://placehold.co/300x220/c8a882/fff?text=Coq+au+Vin", "Dinner", "recipe-coq-au-vin.html"),
    ("Homemade Honeycomb Candy (Crunchie Dupe)", "https://placehold.co/300x220/9b7c5e/fff?text=Honeycomb", "Dessert", "recipe-honeycomb.html"),
    ("Ground Turkey Lettuce Wrap Bar", "https://placehold.co/300x220/c8856b/fff?text=Wrap+Bar", "Lunch", "recipe-wrap-bar.html"),
    ("Turkey Chili", "https://placehold.co/300x220/8faa7c/fff?text=Turkey+Chili", "Dinner", "recipe-turkey-chili.html"),
    ("Chicken Madeira / Marsala", "https://placehold.co/300x220/c8a882/fff?text=Chicken+Madeira", "Dinner", "recipe-chicken-madeira.html"),
    ("Homemade Chicken Noodle Soup", "https://placehold.co/300x220/9b7c5e/fff?text=Chicken+Noodle", "Soup", "recipe-homemade-soup.html"),
    ("Classic Pot Roast with Beef Bone Marrow", "https://placehold.co/300x220/c8856b/fff?text=Pot+Roast+Marrow", "Dutch Oven", "recipe-pot-roast-marrow.html"),
    ("Julia Child\u2019s Coq au Vin", "https://placehold.co/300x220/c8a882/fff?text=Julia+Coq+au+Vin", "Dinner", "recipe-julia-coq-au-vin.html"),
]

def top_card(title, image, category, slug):
    return f"""        <a href="{slug}" style="display:block;">
          <div class="recipe-card cursor-pointer">
            <div class="relative mb-3">
              <img src="{image}" class="w-full h-44 object-cover" alt="{title}">
              <div class="absolute top-2 left-2"><span class="post-category">{category}</span></div>
            </div>
            <h3 class="recipe-title font-serif font-semibold text-base leading-snug mb-1" style="color:#333;">{title}</h3>
            <div class="flex items-center gap-1 mb-1"><span class="star text-xs">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span style="font-family:'Lato',sans-serif;font-size:10px;color:#aaa;">1m reviews</span></div>
          </div>
        </a>"""

def all_card(title, image, category, slug):
    return f"""        <a href="{slug}" style="display:block;">
          <div class="recipe-card cursor-pointer">
            <div class="relative mb-3">
              <img src="{image}" class="w-full h-44 object-cover" alt="{title}">
              <div class="absolute top-2 left-2"><span class="post-category">{category}</span></div>
            </div>
            <h3 class="recipe-title font-serif font-semibold text-base leading-snug mb-1" style="color:#333;">{title}</h3>
            <div class="flex items-center gap-1"><span class="star text-xs">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span style="font-family:'Lato',sans-serif;font-size:10px;color:#aaa;">1m reviews</span></div>
          </div>
        </a>"""

top_cards_html = "\n\n".join(top_card(t, i, c, s) for t, i, c, s, _ in top_rated)
all_cards_html = "\n\n".join(all_card(t, i, c, s) for t, i, c, s in all_recipes)

new_top_section = f"""      <div class="grid grid-cols-4 gap-5 mb-10">

{top_cards_html}

      </div>"""

new_all_section = f"""      <div class="grid grid-cols-4 gap-5">

{all_cards_html}

      </div>"""

# Find and replace the top rated grid
start_top = html.find('      <div class="grid grid-cols-4 gap-5 mb-10">')
end_top = html.find('      </div>', start_top) + len('      </div>')
html = html[:start_top] + new_top_section + html[end_top:]

# Find and replace the all recipes grid
start_all = html.find('      <div class="grid grid-cols-4 gap-5">')
end_all = html.find('\n      </div>', start_all) + len('\n      </div>')
html = html[:start_all] + new_all_section + html[end_all:]

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done! recipes.html rebuilt cleanly.")
