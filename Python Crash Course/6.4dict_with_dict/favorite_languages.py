favorite_languages = {
    'jen': ['Python', 'Ruby'],
    'sarah': ['C'],
    'edward': ['Ruby', 'Go'],
    'phil': ['Python', 'haskell']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages age:")
    for language in languages:
        print("\t" + language.title())
