import scrapy
from bs4 import BeautifulSoup


class PlayersSpider(scrapy.Spider):
    name = "players"
    start_urls = [
        'https://www.futhead.com/18/players/?bin_platform=ps',
    ]

    def parse(self,response):
        #goes into the players links on main page
        for href in response.css('li.list-group-item.list-group-table-row.player-group-item.dark-hover a::attr(href)'):
            yield response.follow(href,self.parse_player)
        #Goes to next page
        for href in response.css('li.list-group-item.list-group-pagination.text-center a::attr(href)'):
            yield response.follow(href,self.parse)

    def parse_player(self, response):
        #grabs data from players
        for stats in response.css('div.col-lg-2.col-sm-4.col-xs-6.igs-group'):
            yield { 
                    'PlayerName':response.css('div').xpath('@data-player-full-name').extract(),
                    'skills': stats.css('span').xpath('@data-chembot-field').extract(),
                    'points': stats.css('span').xpath('@data-chembot-base').extract(),
                 }
        
