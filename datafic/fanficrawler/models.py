from django.db import models


class Fandom (models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __repr__(self):
        return 'Fandom(name={!r})'.format(self.name)


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
    language =  models.CharField(max_length=200)
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
        
