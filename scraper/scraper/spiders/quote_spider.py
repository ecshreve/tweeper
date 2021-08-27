import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://www.tv-quotes.com/shows/the-oc.html',
    ]

    def parse(self, response):
        for quote in response.xpath(
                './/div[contains(@class, "padded quote_mobile")]'):
            qt = quote.xpath(".//text()").getall()
            # quote_text = list(filter(
            #     lambda x: not x.isspace() and x != "View Quote",
            #     quote.xpath(".//text()").getall()))

            yield {
                'lines': qt,
            }
