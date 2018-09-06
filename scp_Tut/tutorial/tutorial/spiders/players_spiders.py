import scrapy

class PlayersSpider(scrapy.Spider):
    #name of crawler
    name = "players"
    start_urls = [
        #crawler starts at this location first
        'https://www.futhead.com/18/players/?bin_platform=ps',
    ]

    def parse(self,response):
        #goes into the players links on main page and grabs player name and rating
        for hrefMain in response.css('li.list-group-item.list-group-table-row.player-group-item.dark-hover a::attr(href)'):
            yield response.follow(hrefMain,self.parse_player)
        #Goes to next page
        for href in response.css('li.list-group-item.list-group-pagination.text-center a::attr(href)'):
            yield response.follow(href,self.parse)

    def parse_player(self, response):
        #grabs data from players
            yield { 
                    #player stats grabbed from website
                    'PlayerName': response.css('div').xpath('@data-player-full-name').extract_first(),
                    'PlayerType': response.css('div').xpath('@data-player-revision-type').extract_first(),
                    'PlayerRating': response.css('div').xpath('@data-player-rating').extract_first(),
                    'PlayerPosition': response.css('div.playercard-position::text').extract_first().strip(),
                    'PlayerClub': response.css('div.playercard-club img::attr(alt)').extract_first(),
                    'PlayerNation': response.css('div.playercard-nation img::attr(alt)').extract_first(),
                    'Pace': response.css('span.chembot-value::text').extract()[0],
                    'Shooting': response.css('span.chembot-value::text').extract()[1],
                    'Passing': response.css('span.chembot-value::text').extract()[2],
                    'Dribbling': response.css('span.chembot-value::text').extract()[3],
                    'Defense': response.css('span.chembot-value::text').extract()[4],
                    'Physical': response.css('span.chembot-value::text').extract()[5],
                 }
                 
        