from django.db import models
from django.utils.functional import cached_property

class Fandom(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image_url = models.URLField(blank=True)
        
    def __repr__(self):
        return 'Fandom(name={!r})'.format(self.name)

    @cached_property
    def fics_count(self):
        return Fanfic.objects.filter(fandom__fandom=self).count()
        
    @cached_property
    def languages_count(self):
        return Fanfic.objects.filter(fandom__fandom=self).values('language').order_by('language').distinct().count()

    @cached_property
    def most_popular_language(self):
        return Fanfic.objects.filter(fandom__fandom=self) \
            .values('language__name').annotate(language_count=models.Count('language')) \
            .order_by('-language_count').first()
            
    @cached_property
    def ficwriter_who_most_wrote(self):
        return Fanfic.objects.filter(fandom__fandom=self) \
            .values('ficwriter__name').annotate(ficwriter_count=models.Count('ficwriter')) \
            .order_by('-ficwriter_count').first()

    @cached_property        
    def longest_fanfic_by_words(self):
        return Fanfic.objects.filter(fandom__fandom=self) \
            .exclude(words=None).values('title', 'words') \
            .order_by('-words').first()
                        
    @cached_property
    def most_commented_fanfic(self):
        return Fanfic.objects.filter(fandom__fandom=self) \
            .exclude(reviews=None).values('title', 'reviews') \
            .order_by('-reviews').first()
            
    @cached_property        
    def most_popular_genre(self):
       return Fanfic.objects.filter(fandom__fandom=self) \
            .exclude(genre=None).values('genre').annotate(genre_count=models.Count('genre')) \
            .order_by('-genre_count').first()
   
    @cached_property        
    def most_popular_rated(self):
       return Fanfic.objects.filter(fandom__fandom=self) \
            .exclude(rated=None).values('rated').annotate(rated_count=models.Count('rated')) \
            .order_by('-rated_count').first()
  
            
class Language(models.Model):
    name = models.CharField(max_length=200, unique=True)

    @cached_property
    def fics_count(self):
        return Fanfic.objects.filter(language=self).count()
        
    @cached_property
    def ficwriter_who_most_wrote(self):
        return Fanfic.objects.filter(language=self) \
            .values('ficwriter__name').annotate(ficwriter_count=models.Count('ficwriter')) \
            .order_by('-ficwriter_count').first()

    @cached_property        
    def longest_fanfic_by_words(self):
        return Fanfic.objects.filter(language=self) \
            .exclude(words=None).values('title', 'words') \
            .order_by('-words').first()
                        
    @cached_property
    def most_commented_fanfic(self):
        return Fanfic.objects.filter(language=self) \
            .exclude(reviews=None).values('title', 'reviews') \
            .order_by('-reviews').first()
            
    @cached_property        
    def most_popular_genre(self):
       return Fanfic.objects.filter(language=self) \
            .exclude(genre=None).exclude(genre='').values('genre').annotate(genre_count=models.Count('genre')) \
            .order_by('-genre_count').first()
   
    @cached_property        
    def most_popular_rated(self):
       return Fanfic.objects.filter(language=self) \
            .exclude(rated=None).values('rated').annotate(rated_count=models.Count('rated')) \
            .order_by('-rated_count').first()
        
    
        
class Category (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __repr__(self):
        return 'Category(name={!r})'.format(self.name)
        

class FandomCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #  remove um fandom e junto com ele suas fics
    fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE)
    
    def __repr__(self):
        return 'FandomCategory(fandom={!r}, category={!r})'.format(self.fandom.name, self.category.name)
        
        
    class Meta:
        unique_together = ("category", "fandom") 
    
    
class Ficwriter(models.Model):
    
    link = models.URLField(max_length=200, blank=True, default="")
    name = models.CharField(max_length=200)
    joined = models.DateField(blank=True, null=True) #campo pode vir vazio
    update = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, default="")
    
    def __repr__(self):
        return 'Ficwriter(name={!r})'.format(self.name)
        
    
    
class Fanfic(models.Model):
    link = models.TextField() # Para URLs
    title = models.CharField(max_length=200) # Texto com um número limitado de caracteres.
    fandom = models.ManyToManyField(FandomCategory)
    ficwriter = models.ManyToManyField(Ficwriter) 
    sinopse = models.TextField(blank=True, default="") #   Para textos longos, sem um limite.
    genre = models.CharField(max_length=200, blank=True, default="")
    rated =  models.CharField(max_length=200)
    language = models.TextField()
    ship =  models.CharField(max_length=200, blank=True, default="")
    chapter = models.IntegerField(blank=True, null=True)
    words = models.IntegerField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    favs = models.IntegerField(blank=True, null=True)
    follows = models.IntegerField(blank=True, null=True)
    update = models.DateField(blank=True, null=True) # Para data sem horas
    published = models.DateField(blank=True, null=True)
    
    def __repr__(self):
        return 'Fanfic(title={!r}, link={!r})'.format(self.title, self.link)
        
