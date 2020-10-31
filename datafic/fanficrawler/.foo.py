import csv

with open('foo.csv') as f:
    reader = csv.DictReader(f)

    for fic_data in reader:
        _, fandom = Fandom.objecs.get_or_create(name=fic_data['name'])
        _, category = Category.objects.get_or_create(name=fic_data['category'])
        fandom_category = FandomCategory.objects.create(fandom=fandom, category=category)
        ficwriter = Ficwriter.get_or_create(link=fic_data['author_link'])
        fic = Fanfic.objects.create(
            fandom=fandom_category,
            ficwriter=ficwriter,
            title=fic_data['title'],
            ...
        )
