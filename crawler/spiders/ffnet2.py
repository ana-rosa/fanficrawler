# -*- coding: utf-8 -*-
import scrapy


class FfnetSpider(scrapy.Spider):
    name = 'ffnet2'
    allowed_domains = ['fanfiction.net']
    start_urls = ['https://www.fanfiction.net/s/5919156/1/Luzes-das-Sombras']
    
    def parse(self, response):
        data = response.css('span.xgray::text')[1].get().split('-')
        language = data[1].strip()
        genre = data[2].strip()
        characters = data[3].strip()
        words = data[4].strip()
        character_a, character_b  = characters.split(",")
        yield {

		    'title': response.css ('b.xcontrast_txt::text').extract_first(),
		    'category': response.css ('a.xcontrast_txt::text').extract_first(),
            'fandom': response.css ('a.xcontrast_txt::text')[1].extract(),
            'ficwriter': response.css ('a.xcontrast_txt::text')[2].extract(),
		    'sinopse': response.css ('div.xcontrast_txt::text').extract_first(),
		    'rated': response.css ('a.xcontrast_txt::text')[3].extract(),
		    'language': language,
		    'genre': genre,
		    #'characters': characters,
		    'character_a': character_a,
		    'character_b': character_b,
		    'chapter_count':response.css ('#chap_select option::attr(value)')[-1].extract(),
		    'words': words,
		    #'reviews':response.css (' ::text').extract_first(),
		    #'favs':response.css (' ::text').extract_first(),
		    #'follows':response.css (' ::text').extract_first(),
		    #'update':response.css (' ::text').extract_first(),
		    #'published':response.css (' ::text').extract_first(),
		    #'chapter':response.css (' ::text').extract_first(),
            #'chapter_name':response.css ('#chap_select option::text').extract_first(),
            #'text':response.css ('div.storytext ::text').extract(),

		    }

	#next_page = response.css (' ').extractfirst()
	#if next_page is not none:
		#yield response.follow(next_page, callback = self.parse)


