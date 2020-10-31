import re

import scrapy


class FfnetSpider(scrapy.Spider):
    name = 'ffnet'
    allowed_domains = ['fanfiction.net']
    start_urls = [
        'https://www.fanfiction.net/book/Lord-of-the-Rings/?&srt=1&r=10',
    ]
    meta_block_regex = re.compile((
        'Rated: (?P<rated>[\\w+ ]+) - '
        '(?P<language>[\\w ]+) - '
        '((?P<genre>[\\w/\- ]+) - )?'
        "((?P<ship>[\[\]\\w.,\-/' ]+) - )?"
        '(Chapters: (?P<chapters>[\\d ]+) - )?'
        'Words: (?P<words>[\\d, ]+) - '
        '(Reviews: (?P<reviews>[\\d\\w, ]+) - )?'
        '(Favs: (?P<favorites>[\\d\\w, ]+) - )?'
        '(Follows: (?P<follows>[\\d\\w, ]+) - )?'
        '(Updated: (?P<updated>[\\d\\w/ ]+) - )?'
        'Published: (?P<publish_date>[\\w\\d/ ]+)'
        '(Status: (?P<status>[\w ]+) - )?'
    ))
    
     #def parse(self,response):
     #   for link in response.css('#list_output td div a::attr(href)').extract():
     #       yield response.follow(link, self.parse_first_page)
    
    def parse(self, response):
        last_page_url = response.css('center a::attr(href)').extract()[4]
        last_page_number = int(last_page_url.split('=')[-1])
        self.current_page = last_page_number
        self.base_url = response.url
        yield response.follow(last_page_url, self.parse_fanfics)

         
    def parse_fanfics(self, response):
        for link in response.css('a.stitle::attr(href)').extract():
            yield response.follow(link, self.parse_fanfic)
            
        self.current_page = self.current_page - 1
        if self.current_page > 0:
            next_page = '{url}&p={page_number}'.format(url=self.base_url, page_number=self.current_page)
            yield response.follow(next_page, self.parse_fanfics)    

    def parse_fanfic(self, response):
        meta_block = response.xpath('//span[@class="xgray xcontrast_txt"]//text()')
        meta_block_text = ''.join(meta_block.extract())
        try:
            meta = self.meta_block_regex.search(meta_block_text).groupdict()
        except AttributeError:
            print('Failed to parse: ', response.url, meta_block_text)
            raise
        yield {
            'link': response.url,
            'title': response.css ('b.xcontrast_txt::text').extract_first(),
            'category': response.css ('a.xcontrast_txt::text').extract_first(),
            'fandom': response.css ('a.xcontrast_txt::text')[1].extract(),
            'ficwriter': response.css ('a.xcontrast_txt::text')[2].extract(),
            # 'sinopse': response.css ('div.xcontrast_txt::text').extract_first(),
            'rated': meta['rated'],
            'reviews': meta['reviews'],
            'favs': meta['favorites'],
            'follows': meta['follows'],
            'updated_at': meta['updated'],
            'published_at': meta['publish_date'],
            'chapters': meta['chapters'],
            'language': meta['language'],
            'words': meta['words'],
            'genre': meta['genre'],
            'status': meta['status'],
            'characters': meta['ship'],
        }

# scrapy crawl ffnet -t csv -o ficteste.csv
