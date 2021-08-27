import scrapy


# This spider is configured to scrape from https://www.tv-quotes.com/.
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://www.tv-quotes.com/shows/the-oc.html',
        'https://www.tv-quotes.com/shows/veronica-mars.html',
        'https://www.tv-quotes.com/shows/twin-peaks.html',
        'https://www.tv-quotes.com/shows/jersey-shore.html',
        'https://www.tv-quotes.com/shows/gossip-girl.html',
    ]

    def parse(self, response):
        # Grab the show title and strip off the extra characters.
        show = response.css('div.rounded h1').get()[4:-12]

        # Grab the quote and all of it's text.
        for quote in response.xpath(
                './/div[contains(@class, "padded quote_mobile")]'):
            qt = quote.xpath(".//text()").getall()

            yield {
                'show': show,
                'lines': qt,
            }

        # Go to the next page.
        next_page = response.css('span.right a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
