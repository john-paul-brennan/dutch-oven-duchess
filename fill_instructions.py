import os, re

DIR = r"c:\Users\johnp\OneDrive\Documents\Claude\Web Design"

recipes = {
    "recipe-spring-pasta.html": [
        "Bring a large pot of salted water to a boil. Cook the ravioli according to package directions, then drain and set aside.",
        "In a large skillet over medium heat, sauté sliced leeks in butter until softened, about 5 minutes. Add the tomato sauce base and simmer for 5 minutes.",
        "Stir in the crème fraîche until the sauce is smooth and creamy. Add the spring peas and cook for 2 minutes until just tender.",
        "Gently fold in the cooked ravioli and toss to coat. Season with salt and pepper. Serve immediately with freshly grated parmesan.",
    ],
    "recipe-salmon-chicken.html": [
        "For the salmon: Season fillets with salt and pepper. Melt butter in a skillet over medium-high heat. Sear salmon skin-side up for 3–4 minutes, flip, and cook 3 more minutes. Finish with a squeeze of lemon. Steam green beans alongside.",
        "For the roast chicken: Rub a whole chicken generously with compound butter under and over the skin. Season with salt and pepper. Place in a roasting pan with potatoes cut into chunks.",
        "Roast at 425°F for 60–75 minutes, until the juices run clear and a thermometer reads 165°F. Baste the potatoes in the drippings halfway through.",
        "Rest the chicken for 10 minutes before carving. Serve both proteins family-style with the roasted potatoes and green beans.",
    ],
    "recipe-halloween-meatballs.html": [
        "Preheat oven to 400°F. In a large bowl, combine ground meat, breadcrumbs, egg, and your preferred seasonings (salt, pepper, garlic powder, Italian seasoning). Mix until just combined — don't overwork.",
        "Roll into balls about 1.5 inches in diameter. You should get approximately 30 meatballs. Place on a parchment-lined baking sheet with space between each.",
        "Bake for 18–22 minutes until cooked through and nicely browned. Internal temperature should reach 165°F.",
        "Serve immediately — these are not for sharing.",
    ],
    "recipe-grilled-chicken.html": [
        "Season chicken pieces generously with salt, pepper, and your preferred spices. Let sit at room temperature for 20 minutes.",
        "Preheat grill to medium-high. Grill chicken for 6–8 minutes per side, until grill marks form and internal temperature reaches 165°F. Rest for 5 minutes.",
        "For the mashed potatoes: Boil peeled potatoes until fork-tender. Drain, then mash with generous amounts of homemade butter, salt, and enough warm milk to reach your desired consistency.",
        "Make the gravy: In a small saucepan, whisk together pan drippings, a tablespoon of flour, and chicken broth over medium heat until thickened. Add peas in the last 2 minutes. Serve everything together.",
    ],
    "recipe-french-toast.html": [
        "For the honey butter: Beat softened butter with honey to taste until fluffy. Set aside at room temperature.",
        "Whisk together eggs, milk, cinnamon, and vanilla in a shallow dish. Soak thick-cut bread slices for 30–45 seconds per side.",
        "Cook soaked bread in a buttered skillet or griddle over medium heat for 2–3 minutes per side until golden brown and cooked through.",
        "Serve immediately topped with a generous pat of homemade honey butter and a drizzle of maple syrup.",
    ],
    "recipe-lasagna.html": [
        "Make or heat your sauce. For meat sauce: brown ground meat with onion and garlic, add tomato sauce, and simmer 20 minutes. Season well.",
        "Cook lasagna noodles until just al dente. Drain and lay flat on oiled parchment to prevent sticking. Mix ricotta with an egg, salt, pepper, and a handful of parmesan.",
        "Layer in a 9x13 baking dish: sauce, noodles, ricotta mixture, mozzarella. Repeat layers, finishing with noodles, sauce, and a generous layer of mozzarella and parmesan.",
        "Cover with foil and bake at 375°F for 45 minutes. Uncover and bake 15 more minutes until bubbly and golden. Rest for 15 minutes before slicing.",
    ],
    "recipe-chicken-noodle-soup.html": [
        "Pull rotisserie chicken meat from the bones, shredding into bite-sized pieces. Set aside. If time allows, simmer the carcass in water for 30 minutes to enrich the broth.",
        "In a large Dutch oven, sauté diced carrots, celery, and onion in butter over medium heat until softened, about 8 minutes. Add garlic, thyme, and bay leaf.",
        "Pour in chicken broth and bring to a boil. Add egg noodles and cook according to package directions until tender.",
        "Stir in the shredded chicken, season generously with salt and pepper, and simmer 5 more minutes. Remove bay leaf. Serve hot.",
    ],
    "recipe-yellow-cake.html": [
        "Preheat oven to 350°F. Grease and flour two 9-inch round cake pans. Whisk together flour, baking powder, and salt in a bowl.",
        "Beat butter and sugar together until pale and fluffy, about 4 minutes. Add eggs one at a time, beating after each. Mix in vanilla.",
        "Alternate adding the flour mixture and buttermilk to the butter mixture, beginning and ending with flour. Divide batter evenly between pans.",
        "Bake for 28–32 minutes until a toothpick comes out clean. Cool completely in pans, then turn out onto a wire rack. Frost generously with Pillsbury chocolate frosting.",
    ],
    "recipe-salmon-two-ways.html": [
        "For teriyaki bites: Cut salmon into 1-inch cubes. Toss with teriyaki glaze and let marinate 15 minutes. Sear in a hot skillet for 2 minutes per side. Finish with sesame seeds and sliced green onion.",
        "For lemon herb salmon: Season fillets with salt, pepper, lemon zest, and chopped fresh herbs. Sear in butter over medium-high heat, 3–4 minutes per side.",
        "For the sides: Toss potatoes in olive oil and roast at 425°F for 30–35 minutes until golden. Blanch green beans, then sauté with garlic and butter until tender.",
        "Plate both salmon preparations side by side with the roasted potatoes and garlic green beans.",
    ],
    "recipe-lemon-salmon.html": [
        "Season salmon fillets with salt, pepper, lemon zest, and chopped fresh herbs. Let sit 10 minutes.",
        "Cook orzo in salted boiling water until al dente. Drain and toss with olive oil, chopped sun-dried tomatoes, lemon juice, and fresh herbs. Season to taste.",
        "Sear salmon in a hot skillet with butter or oil, skin-side down first, for 3–4 minutes. Flip and cook 2–3 minutes more until just cooked through.",
        "Blanch green beans in salted water for 3 minutes, then drain. Serve salmon over the orzo with green beans alongside and an extra squeeze of lemon.",
    ],
    "recipe-chili.html": [
        "Brown ground beef or turkey in a large pot or Dutch oven over medium-high heat. Drain excess fat. Add diced onion and peppers and cook until softened.",
        "Stir in garlic, chili powder, cumin, paprika, salt, and pepper. Add canned tomatoes and beans. Bring to a simmer, then reduce heat and cook uncovered for 45 minutes to 1 hour, stirring occasionally.",
        "For the cornbread muffins: Whisk together cornmeal, flour, sugar, baking powder, and salt. Stir in egg, milk, and melted butter until just combined. Fill greased muffin tins ¾ full.",
        "Bake muffins at 400°F for 15–18 minutes until golden. Serve chili hot with muffins, sour cream, shredded cheese, and green onions.",
    ],
    "recipe-lemon-scones.html": [
        "For the lemon curd (make first): Whisk eggs, sugar, and lemon juice in a saucepan over low heat. Add butter a piece at a time, stirring constantly until thickened, about 10 minutes. Refrigerate until set.",
        "For the scones: Preheat oven to 400°F. Whisk flour, sugar, baking powder, and salt. Cut cold butter into the flour until pea-sized pieces form. Stir in lemon zest.",
        "Add heavy cream and mix until just combined. Turn onto a floured surface and gently shape into a round. Cut into 8 wedges and place on a parchment-lined baking sheet.",
        "Bake for 16–18 minutes until golden. Cool slightly before serving warm with a generous spoonful of lemon curd.",
    ],
    "recipe-lettuce-wraps.html": [
        "Cook ground turkey in a skillet over medium-high heat, breaking it up as it cooks. Drain any excess liquid.",
        "Add minced garlic and ginger and cook 1 minute. Stir in hoisin sauce, soy sauce, and sesame oil. Add diced water chestnuts and cook 2 more minutes.",
        "Remove from heat and stir in sliced green onions. Season to taste.",
        "Serve the turkey mixture in whole butter lettuce leaves. Top with extra green onion, sesame seeds, and a drizzle of sriracha if desired.",
    ],
    "recipe-coq-au-vin.html": [
        "Pat chicken dry and season with salt and pepper. Brown in batches in a Dutch oven with butter and oil over medium-high heat. Remove and set aside. Cook lardons until crispy, then remove.",
        "Sauté pearl onions and mushrooms in the same pot until golden. Add garlic and cook 1 minute. Return chicken and lardons to the pot. Pour in red wine and enough broth to nearly cover. Add thyme and bay leaf.",
        "Bring to a simmer, cover, and braise on low heat or in a 325°F oven for 1.5–2 hours until the chicken is deeply tender. Remove bay leaf and adjust seasoning.",
        "For mashed potatoes: Boil potatoes, drain, and mash with butter and warm cream. For the lyonnaise salad: Toss frisée with warm bacon vinaigrette and a poached egg. Serve everything together.",
    ],
    "recipe-honeycomb.html": [
        "Line a baking sheet with parchment and grease lightly. Combine sugar and golden syrup in a deep saucepan over medium heat. Stir until sugar dissolves, then stop stirring and let it boil until it turns a deep amber color (300°F on a candy thermometer).",
        "Remove from heat immediately and whisk in the baking soda quickly — the mixture will foam up dramatically. Pour immediately onto the prepared baking sheet. Do not spread it; let it settle naturally.",
        "Leave undisturbed at room temperature for at least 1 hour until completely set and hardened. Break into irregular pieces.",
        "Melt dark chocolate and dip each piece halfway. Place on parchment to set. Store in an airtight container.",
    ],
    "recipe-wrap-bar.html": [
        "Cook ground turkey in a skillet over medium-high heat. Season with salt, pepper, garlic powder, and ginger. Drain any excess liquid.",
        "Stir in hoisin sauce, soy sauce, and sesame oil. Cook 2 more minutes until the sauce coats the meat. Keep warm.",
        "Set out the toppings bar: whole butter lettuce leaves, diced cucumber, shredded carrots, sliced green onion, sesame seeds, lime wedges, sriracha, and any other desired toppings.",
        "Let everyone build their own wraps — spoon the turkey mixture into lettuce cups and load up with toppings.",
    ],
    "recipe-turkey-chili.html": [
        "Brown ground turkey in a large pot over medium-high heat, breaking it up. Add diced onion, garlic, and bell peppers and cook until softened, about 5 minutes.",
        "Stir in cumin, chili powder, paprika, salt, and pepper. Cook the spices for 1 minute until fragrant.",
        "Add canned tomatoes and kidney beans. Stir to combine, then bring to a boil. Reduce heat and simmer uncovered for 30–45 minutes, stirring occasionally.",
        "Taste and adjust seasoning. Serve with sour cream, shredded cheese, green onion, and crackers or cornbread.",
    ],
    "recipe-chicken-madeira.html": [
        "Pound chicken breasts to an even ½-inch thickness between plastic wrap. Season with salt and pepper.",
        "Sear chicken in butter over medium-high heat for 3–4 minutes per side until golden. Remove and set aside.",
        "In the same pan, sauté sliced mushrooms until browned. Add Madeira or Marsala wine and let it reduce by half, scraping up any browned bits. Add beef broth and simmer until slightly thickened.",
        "Return chicken to the pan and finish with a knob of butter and fresh herbs. Simmer 2–3 minutes until chicken is cooked through. Serve over mashed potatoes or pasta.",
    ],
    "recipe-homemade-soup.html": [
        "Preheat oven to 350°F. Roast chicken bones on a baking sheet for 2 hours until deeply golden. Transfer to a large pot, cover with cold water, and simmer for 2–3 hours to make stock. Strain and reserve.",
        "In a large Dutch oven, sauté diced carrots, celery, and onion in butter until softened, about 8 minutes. Season with salt and pepper.",
        "Add the homemade chicken stock and bring to a boil. Add chicken breasts and simmer for 15–18 minutes until cooked through. Remove, shred, and return to the pot.",
        "Add egg noodles and cook until tender, about 8 minutes. Taste and adjust seasoning generously. Serve hot.",
    ],
    "recipe-pasta-vodka.html": [
        "Make or pull handmade pasta. In a large skillet, sauté finely diced shallots and garlic in olive oil over medium heat until soft, about 5 minutes.",
        "Add a splash of vodka and cook for 2 minutes until the alcohol burns off. Add crushed San Marzano tomatoes and a pinch of red pepper flakes. Simmer 15 minutes.",
        "Stir in heavy cream and simmer another 5 minutes until the sauce is silky and deep pink. Season generously with salt.",
        "Cook pasta in well-salted boiling water. Reserve a cup of pasta water before draining. Toss pasta into the sauce with a splash of pasta water. Finish with grated Pecorino Romano and fresh basil.",
    ],
    "recipe-pot-roast.html": [
        "Pat the chuck and bottom round dry and season generously with salt and pepper. Sear in a Dutch oven over high heat with oil on all sides until deeply browned, about 4 minutes per side. Remove.",
        "Reduce heat to medium. Sauté roughly chopped onion and carrots until golden. Add garlic and tomato paste, cook 1 minute. Deglaze with Cabernet Sauvignon, scraping the bottom of the pot.",
        "Return the beef to the pot. Add beef broth until the liquid comes halfway up the meat. Tuck in fresh herbs. Bring to a simmer, then cover tightly.",
        "Braise in a 325°F oven for 4 hours, turning the meat halfway through, until fork-tender. Rest 15 minutes before slicing or pulling apart. Serve with the braising liquid spooned over top.",
    ],
    "recipe-pot-roast-marrow.html": [
        "Season chuck roast generously with salt and pepper. Sear in a Dutch oven over high heat until deeply browned on all sides. Remove and set aside.",
        "Place beef bone marrow bones cut-side up on a baking sheet. Roast at 450°F for 15–20 minutes until the marrow is soft and bubbling. Set aside.",
        "In the Dutch oven, sauté root vegetables until golden. Add red wine and beef broth, then return the chuck roast. Cover and braise at 325°F for 3.5–4 hours until tender.",
        "Scoop the roasted bone marrow and stir it into the braising liquid for richness. Serve the pot roast over creamy mashed potatoes with the marrow-enriched sauce.",
    ],
    "recipe-julia-coq-au-vin.html": [
        "Cut the chicken into pieces and pat dry. Season with salt and pepper. In a large Dutch oven, render the lardons until crispy. Remove. Brown the chicken pieces in the fat over medium-high heat, then remove.",
        "Pour in cognac and carefully flambé, or just let it cook off for 2 minutes. Add pearl onions and mushrooms and cook until lightly browned.",
        "Return chicken and lardons to the pot. Pour over Burgundy wine until the chicken is nearly submerged. Add thyme, bay leaves, and garlic. Bring to a simmer, cover, and cook on low heat for 1.5 hours.",
        "Remove the chicken. Strain the braising liquid and reduce over high heat until slightly thickened and glossy. Finish with a knob of cold butter. Return chicken to the sauce and serve with crusty bread or potatoes.",
    ],
}

OL_PATTERN = re.compile(
    r'(<ol style="font-family:\'Lato\'[^>]+>).*?(</ol>)',
    re.DOTALL
)

for filename, steps in recipes.items():
    path = os.path.join(DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    items = "\n".join(f'            <li style="margin-bottom:16px;">{step}</li>' for step in steps)
    replacement = r'\g<1>' + f'\n{items}\n          ' + r'\g<2>'
    new_html = OL_PATTERN.sub(replacement, html, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Updated: {filename} ({len(steps)} steps)")

print("All done!")
