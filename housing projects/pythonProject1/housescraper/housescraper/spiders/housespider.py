import scrapy


class HousespiderSpider(scrapy.Spider):
    name = "housespider"
    allowed_domains = ["property24.com"]
    start_urls = ["https://www.property24.com/apartments-for-sale/gauteng/1"]

    def parse(self, response):
        houses = response.css('.p24_regularTile')
        for house in houses:
            yield {
                'floor_size': house.css('.p24_icons.p24_size span::text').get()
            }
            url = house.css('.p24_regularTile a::(href)').get()

            house_url = 'https://www.property24.com/' + url
            yield response.follow(house_url, callback=self.parse_house_page)
            #'price' : house.css('.p24_information .p24_price::text').get(),
            #'discription' : house.css('.p24_information .p24_description::text').get(),
            #'location' : house.css('.p24_information .p24_description .p24_location::text').get(),
            #'featureDetails ' : house.css('.p24_icons .p24_featureDetails span::text').getall(),
            #',


        #next_page = response.css('a.pull-right::attr(href)').get()

        #if next_page is not None:
            #next_page_url = next_page
            #yield response.follow(next_page_url, callback=self.parse)


    def parse_house_page(self, response):
        pass