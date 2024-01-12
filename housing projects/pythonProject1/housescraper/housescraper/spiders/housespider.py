import scrapy


class HousespiderSpider(scrapy.Spider):
    name = "housespider"
    allowed_domains = ["property24.com"]
    start_urls = ["https://www.property24.com/apartments-for-sale/gauteng/1"]

    def parse(self, response):
        houses = response.css('.p24_content')

        for house in houses:
            yield {
                'price' : house.css('.p24_price::attr(content)').get(),
                'discription' : house.css('.p24_title ::text').get(),
                'location' : house.css('.p24_location::text').get(),
                'featureDetails ': house.css('.p24_icons .p24_featureDetails span::text').getall(),
                'floor_size': house.css('.p24_icons .p24_size span::text').get(),
            }

        next_page = response.css('a.pull-right::attr(href)').get()

        if next_page is not None:
            next_page_url = next_page
            yield response.follow(next_page_url, callback=self.parse)


    def parse_house_page(self, response):
        pass