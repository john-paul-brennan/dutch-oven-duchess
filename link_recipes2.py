path = r"c:\Users\johnp\OneDrive\Documents\Claude\Web Design\recipes.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    ("Cabernet-Braised Pot Roast", "recipe-pot-roast.html"),
    ("Dutch Oven Rotisserie Chicken Noodle Soup", "recipe-chicken-noodle-soup.html"),
    ("Classic Yellow Cake with Chocolate Frosting", "recipe-yellow-cake.html"),
    ("Weeknight Salmon &amp; Meal-Prep Roast Chicken", "recipe-salmon-chicken.html"),
    ("Weeknight Salmon & Meal-Prep Roast Chicken", "recipe-salmon-chicken.html"),
    ("Sunday Grilled Chicken &amp; Mashed Potatoes", "recipe-grilled-chicken.html"),
    ("Sunday Grilled Chicken & Mashed Potatoes", "recipe-grilled-chicken.html"),
    ("French Toast with Homemade Honey Butter", "recipe-french-toast.html"),
    ("The Cheesiest Lasagna", "recipe-lasagna.html"),
    ("Crock Pot Chili &amp; Cornbread Muffins", "recipe-chili.html"),
    ("Crock Pot Chili & Cornbread Muffins", "recipe-chili.html"),
    ("Lemon Scones with Lemon Curd", "recipe-lemon-scones.html"),
    ("Coq au Vin with Mashed Potatoes &amp; Lyonnaise Salad", "recipe-coq-au-vin.html"),
    ("Coq au Vin with Mashed Potatoes & Lyonnaise Salad", "recipe-coq-au-vin.html"),
    ("Homemade Honeycomb Candy (Crunchie Dupe)", "recipe-honeycomb.html"),
    ("Ground Turkey Lettuce Wrap Bar", "recipe-wrap-bar.html"),
    ("Homemade Chicken Noodle Soup", "recipe-homemade-soup.html"),
    ("Classic Pot Roast with Beef Bone Marrow", "recipe-pot-roast-marrow.html"),
]

# Strategy: for each title, find the recipe-card div containing it
# and wrap it. We'll split by lines and rebuild.

for title, slug in replacements:
    if title not in html:
        print(f"SKIP (not found): {title}")
        continue
    if f'href="{slug}"' in html:
        print(f"ALREADY linked: {title}")
        continue

    # Find the <div class="recipe-card cursor-pointer"> that appears before this title
    idx = html.find(title)
    if idx == -1:
        continue

    # Walk back to find the opening div
    open_tag = '<div class="recipe-card cursor-pointer">'
    start = html.rfind(open_tag, 0, idx)
    if start == -1:
        print(f"No opening div for: {title}")
        continue

    # Find the matching closing </div></div> after the title
    # Count divs from the open tag
    pos = start + len(open_tag)
    depth = 1
    while depth > 0 and pos < len(html):
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                end = next_close + len('</div>')
            else:
                pos = next_close + len('</div>')

    card_html = html[start:end]
    wrapped = f'<a href="{slug}" style="display:block;">{card_html}</a>'
    html = html[:start] + wrapped + html[end:]
    print(f"Linked: {title} -> {slug}")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")
