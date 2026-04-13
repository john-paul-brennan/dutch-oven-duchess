import os

DIR = r"c:\Users\johnp\OneDrive\Documents\Claude\Web Design"

recipes = [
    ("pot-roast", "Cabernet-Braised Pot Roast", "recipe-pot-roast.jpg", "Dutch Oven"),
    ("pasta-vodka", "Pasta alla Vodka", "recipe-pasta-vodka.jpg", "Pasta"),
    ("chicken-noodle-soup", "Dutch Oven Rotisserie Chicken Noodle Soup", "recipe-chicken-noodle-soup.jpg", "Dutch Oven"),
    ("yellow-cake", "Classic Yellow Cake with Chocolate Frosting", "recipe-yellow-cake.jpg", "Dessert"),
    ("spring-pasta", "Spring Pasta &#8212; Ravioli in Tomato Cr&egrave;me Fra&icirc;che", "recipe-spring-pasta.jpg", "Pasta"),
    ("salmon-chicken", "Weeknight Salmon &amp; Meal-Prep Roast Chicken", "recipe-salmon-chicken.jpg", "Meal Prep"),
    ("halloween-meatballs", "Halloween Meatballs", "recipe-halloween-meatballs.jpg", "Dinner"),
    ("grilled-chicken", "Sunday Grilled Chicken &amp; Mashed Potatoes", "recipe-grilled-chicken.jpg", "Dinner"),
    ("french-toast", "French Toast with Homemade Honey Butter", "recipe-french-toast.jpg", "Breakfast"),
    ("lasagna", "The Cheesiest Lasagna", "recipe-lasagna.jpg", "Pasta"),
    ("salmon-two-ways", "Salmon Two Ways", "recipe-salmon-two-ways.jpg", "Dinner"),
    ("lemon-salmon", "Lemon Herb Salmon with Sun-Dried Tomato Orzo", "recipe-lemon-salmon.jpg", "Dinner"),
    ("chili", "Crock Pot Chili &amp; Cornbread Muffins", "recipe-chili.jpg", "Slow Cooker"),
    ("lemon-scones", "Lemon Scones with Lemon Curd", "recipe-lemon-scones.jpg", "Baking"),
    ("lettuce-wraps", "Turkey Lettuce Wraps", "recipe-lettuce-wraps.jpg", "Lunch"),
    ("coq-au-vin", "Coq au Vin with Mashed Potatoes &amp; Lyonnaise Salad", "recipe-coq-au-vin.jpg", "Dinner"),
    ("honeycomb", "Homemade Honeycomb Candy (Crunchie Dupe)", "recipe-honeycomb.jpg", "Dessert"),
    ("wrap-bar", "Ground Turkey Lettuce Wrap Bar", "recipe-wrap-bar.jpg", "Lunch"),
    ("turkey-chili", "Turkey Chili", "recipe-turkey-chili.jpg", "Dinner"),
    ("chicken-madeira", "Chicken Madeira / Marsala", "recipe-chicken-madeira.jpg", "Dinner"),
    ("homemade-soup", "Homemade Chicken Noodle Soup", "recipe-homemade-soup.jpg", "Soup"),
    ("pot-roast-marrow", "Classic Pot Roast with Beef Bone Marrow", "recipe-pot-roast-marrow.jpg", "Dutch Oven"),
    ("julia-coq-au-vin", "Julia Child&#39;s Coq au Vin", "recipe-julia-coq-au-vin.jpg", "Dinner"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_plain} &#8211; Dutch Oven Duchess</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{ site: 'rgb(254,186,209)', body: 'rgb(77,77,77)' }},
          fontFamily: {{
            serif: ['Bitter','Georgia','serif'],
            sans: ['Lato','Helvetica Neue','sans-serif'],
          }},
        }}
      }}
    }}
  </script>
  <style>
    body {{ color: rgb(77,77,77); font-family: 'Bitter', Georgia, serif; }}
    a {{ color: inherit; text-decoration: none; }}
    .nav-link {{ font-family:'Lato',sans-serif; font-size:11px; letter-spacing:2px; text-transform:uppercase; font-weight:700; }}
    .section-label {{ font-family:'Lato',sans-serif; font-size:10px; letter-spacing:3px; text-transform:uppercase; font-weight:700; color:rgb(77,77,77); }}
    .post-category {{ font-family:'Lato',sans-serif; font-size:9px; letter-spacing:2px; text-transform:uppercase; font-weight:700; background:rgb(254,186,209); color:rgb(100,40,70); padding:3px 8px; display:inline-block; margin-bottom:12px; }}
    .footer-heading {{ font-family:'Lato',sans-serif; font-size:10px; letter-spacing:2px; text-transform:uppercase; font-weight:700; margin-bottom:10px; color:rgb(100,40,70); }}
    .footer-link {{ font-family:'Lato',sans-serif; font-size:12px; color:rgb(120,50,80); line-height:2; }}
  </style>
</head>
<body class="bg-white">

  <!-- Top Bar -->
  <div style="background:rgb(254,186,209);font-family:'Lato',sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:rgb(100,40,70);" class="text-center py-2">
    <span>OUR RECIPES.</span><span class="mx-3">YOUR INBOX.</span><a href="#" class="underline">SIGN UP</a>
  </div>

  <!-- Navigation -->
  <nav class="bg-white border-b border-gray-100 sticky top-0 z-50">
    <div class="max-w-5xl mx-auto px-4 flex items-center justify-between h-16">
      <div class="flex items-center gap-8">
        <a href="index.html" class="nav-link">Home</a>
        <a href="about.html" class="nav-link">About</a>
        <a href="recipes.html" class="nav-link" style="color:rgb(200,100,140);border-bottom:2px solid rgb(200,100,140);padding-bottom:2px;">Recipes</a>
      </div>
      <a href="index.html">
        <div style="font-family:'Bitter',serif;font-size:22px;font-weight:600;letter-spacing:1px;color:#222;">Dutch Oven Duchess</div>
      </a>
      <div class="flex items-center gap-8">
        <a href="#" class="nav-link">Start Here</a>
        <svg class="w-4 h-4 text-gray-600 cursor-pointer" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
        </svg>
      </div>
    </div>
  </nav>

  <!-- Recipe Header -->
  <section class="py-10 bg-white">
    <div class="max-w-3xl mx-auto px-4 text-center">
      <span class="post-category">{category}</span>
      <h1 style="font-family:'Bitter',serif;font-size:2.2rem;font-weight:600;color:#222;line-height:1.2;margin-bottom:16px;">{title}</h1>
      <div class="flex items-center justify-center gap-3 mb-4" style="font-family:'Lato',sans-serif;font-size:11px;color:#aaa;letter-spacing:1px;">
        <span style="color:#F2B955;">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        <span>1m reviews</span>
        <span>&#183;</span>
        <a href="recipes.html" style="color:rgb(200,100,140);">&#8592; Back to Recipes</a>
      </div>
    </div>
  </section>

  <!-- Hero Image -->
  <section class="bg-white mb-10">
    <div class="max-w-3xl mx-auto px-4">
      <img src="{image}" class="w-full object-cover" style="max-height:480px;" alt="{title_plain}">
    </div>
  </section>

  <!-- Recipe Content -->
  <section class="pb-16 bg-white">
    <div class="max-w-3xl mx-auto px-4">
      <div class="grid grid-cols-3 gap-10">

        <!-- Ingredients -->
        <div class="col-span-1">
          <p class="section-label mb-4">Ingredients</p>
          <ul style="font-family:'Lato',sans-serif;font-size:14px;line-height:2;color:#555;list-style:disc;padding-left:18px;">
            <li>Ingredient one</li>
            <li>Ingredient two</li>
            <li>Ingredient three</li>
            <li>Ingredient four</li>
            <li>Ingredient five</li>
            <li>Ingredient six</li>
            <li>Ingredient seven</li>
            <li>Ingredient eight</li>
          </ul>
        </div>

        <!-- Instructions -->
        <div class="col-span-2">
          <p class="section-label mb-4">Instructions</p>
          <ol style="font-family:'Lato',sans-serif;font-size:14px;line-height:1.9;color:#555;list-style:decimal;padding-left:18px;">
            <li style="margin-bottom:16px;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Preheat your oven or prepare your cooking vessel as needed.</li>
            <li style="margin-bottom:16px;">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Combine the main ingredients and season generously.</li>
            <li style="margin-bottom:16px;">Ut enim ad minim veniam, quis nostrud exercitation ullamco. Cook over medium heat, stirring occasionally, until done.</li>
            <li style="margin-bottom:16px;">Duis aute irure dolor in reprehenderit in voluptate. Rest before serving and garnish as desired.</li>
          </ol>
        </div>

      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer style="background:rgb(210,120,155);" class="pt-10 pb-6">
    <div class="max-w-5xl mx-auto px-4">
      <div class="grid grid-cols-4 gap-8 mb-8">
        <div>
          <p class="footer-heading">Dutch Oven Duchess</p>
          <a href="index.html" class="footer-link block">Blog</a>
          <a href="about.html" class="footer-link block">About / Contact</a>
          <a href="#" class="footer-link block">Work With Us</a>
          <a href="#" class="footer-link block">Privacy Policy</a>
        </div>
        <div>
          <p class="footer-heading">Food &amp; Recipes</p>
          <a href="recipes.html" class="footer-link block">All Recipes</a>
          <a href="#" class="footer-link block">Dinner</a>
          <a href="#" class="footer-link block">Quick + Easy</a>
          <a href="#" class="footer-link block">Meal Prep Recipes</a>
        </div>
        <div class="col-span-2">
          <p class="footer-heading">Sign Up for Email Updates</p>
          <div class="flex mb-4">
            <input type="email" placeholder="Email Address" class="px-3 py-2 flex-1 text-sm" style="font-family:'Lato',sans-serif;font-size:12px;border:none;outline:none;">
            <button style="background:#F2B955;color:#fff;font-family:'Lato',sans-serif;font-size:11px;font-weight:700;padding:10px 18px;border:none;cursor:pointer;">GO</button>
          </div>
        </div>
      </div>
      <div class="border-t border-opacity-20 pt-6 flex items-center justify-between">
        <div style="font-family:'Bitter',serif;font-size:20px;font-weight:600;color:#fff;">Dutch Oven Duchess</div>
        <p style="font-family:'Lato',sans-serif;font-size:11px;color:rgba(100,40,70,0.7);">&#169; 2026 Dutch Oven Duchess &#183; All Rights Reserved</p>
        <div class="flex gap-4">
          <a href="#" style="font-family:'Lato',sans-serif;font-size:11px;color:rgba(100,40,70,0.8);">Privacy Policy</a>
          <a href="#" style="font-family:'Lato',sans-serif;font-size:11px;color:rgba(100,40,70,0.8);">Terms</a>
        </div>
      </div>
    </div>
  </footer>

</body>
</html>"""

for slug, title, image, category in recipes:
    title_plain = title.replace("&amp;", "&").replace("&#8212;", "—").replace("&egrave;", "è").replace("&icirc;", "î").replace("&#39;", "'").replace("&#8211;", "–")
    html = TEMPLATE.format(title=title, title_plain=title_plain, image=image, category=category)
    path = os.path.join(DIR, f"recipe-{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: recipe-{slug}.html")

print("All done!")
