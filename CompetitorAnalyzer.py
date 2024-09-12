import scrapy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class CompetitorAnalyzer(scrapy.Spider):
    name = "CompetitorAnalyzer"
    description = "Scrapes competitor products, compares features and provides a comprehensive landscape report for product design."

    def __init__(self, competitors_urls):
        self.competitors_urls = competitors_urls
        self.feature_vectors = []

    def start_requests(self):
        for url in self.competitors_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_data = response.xpath('//div[@class="product-details"]').getall()  # Adjust the XPath to match your target site
        self.feature_vectors.append(product_data)

    def compare_features(self):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(self.feature_vectors)
        similarity_matrix = cosine_similarity(vectors)
        return pd.DataFrame(similarity_matrix)

# Usage Example:
# analyzer = CompetitorAnalyzer(competitors_urls=["https://example.com/product1", "https://example.com/product2"])
# analyzer.compare_features()
