from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "りんご"})
crawler.crawl(keyword="りんご", max_num=10)
