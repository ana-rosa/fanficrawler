



#####Geral#####

#Quantidade de fanfics no banco
Fanfic.objects.count()

#Quantidade de autores
Ficwriter.objects.count()






####Ranking Geral ####


#Ficwriter que mais escreveu fics
Fanfic.objects.values('ficwriter__name').annotate(ficwriter_count=Count('ficwriter')).order_by('-ficwriter_count')


#Fanfic com o maior número de palavras
Fanfic.objects.values('title', 'words').order_by('-words')

#Fanfic com o maior número de reviews
Fanfic.objects.exclude(reviews=None).values('title', 'reviews').order_by('-reviews')


#Popularidade dos gêneros
Fanfic.objects.values('genre').annotate(genre_count=Count('genre')).order_by('-genre_count')  

#Popularidade das clasificações etárias
Fanfic.objects.values('rated').annotate(rated_count=Count('rated')).order_by('-rated_count') 

#Popularidade das linguagens
Fanfic.objects.values('language').annotate(language_count=Count('language')).order_by('-language_count') 

#Tamanho mais comum de fanfics (em palavras)
Fanfic.objects.values('genre').annotate(genre_count=Count('genre')).order_by('-genre_count')  

#Tamanho mais comum de fanfics (em capítulos)
Fanfic.objects.values('chapter').annotate(chapter_count=Count('chapter')).order_by('-chapter_count')  







###Fandom###

#Harry Potter#

#Quantidade de fanfics no fandom
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").count()

#Ficwriter que mais escreveu fics
 Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('ficwriter__name').annotate(ficwriter_count=Count('ficwriter')).order_
    ...: by('-ficwriter_count')

#Fanfic com o maior número de palavras
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('title', 'words').order_by('-words')

#Fanfic com o maior número de reviews
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").exclude(reviews=None).values('title', 'reviews').order_by('-reviews')

#Popularidade dos gêneros
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('genre').annotate(genre_count=Count('genre')).order_by('-genre_count')

#Popularidade das clasificações etárias
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('rated').annotate(rated_count=Count('rated')).order_by('-rated_count')

#Popularidade das linguagens
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('language').annotate(language_count=Count('language')).order_by('-language_count')   

#Tamanho mais comum de fanfics (em palavras)
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('words').annotate(words_count=Count('words')).order_by('-words_count')

#Tamanho mais comum de fanfics (em capítulos)
Fanfic.objects.filter(fandom__fandom__name="Harry Potter").values('chapter').annotate(chapter_count=Count('chapter')).order_by('-chapter_count')

