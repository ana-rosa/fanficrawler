import csv 
import time

from fanficrawler.models import FandomCategory, Ficwriter, Fanfic, Fandom, Category

Fanfic.objects.all().delete()

with open("lotr.csv") as f:
    reader = csv.DictReader(f) #leitor do csv'
    fandom, _ = Fandom.objects.get_or_create(name='Lord of the Rings')
    category, _ = Category.objects.get_or_create(name='Books')
    fandom, _ = FandomCategory.objects.get_or_create(category=category, fandom=fandom)
    counter = 0
    t0 = time.time()
    for line in reader:
        ficwriter, _ = Ficwriter.objects.get_or_create(name=line["ficwriter"])
        fanfic= Fanfic.objects.create(
            #fandom=fandom,
            #ficwriter=ficwriter,
            link=line.get('link', ''),
            title = line.get('title', ''),
            rated= line.get('rated', ''),
            genre= line.get('genre', ''),
            reviews= (line.get('reviews', '') or '').replace(',', '') or None,# remove vírgulas como separador decimal do FFN
            favs= (line.get('favorites', '') or '').replace(',', '') or None,
            follows= (line.get('follows', '') or '').replace(',', '') or None,
            update= (line.get('updated', '') or '').replace(',', '') or None,
            published= (line.get('publish', '') or '').replace(',', '') or None,
            chapter= (line.get('chapters', '') or '').replace(',', '') or None,
            language= (line.get('language', '')).replace(',', '') or None,
            words= (line.get('words', '') or '').replace(',', '') or None,
            ship= line.get('ship', ''),
            )
            
        fanfic.ficwriter.add(ficwriter) #add ficwriter a uma fanfic
        fanfic.fandom.add(fandom)
        
        counter += 1
        if counter % 100 == 1:
            ellapsed_time = time.time() - t0
            print('Inserted {} fics / {}s'.format(counter, ellapsed_time))
