from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import requests
from bs4 import BeautifulSoup
import os

# Initialize Spark session and context
spark = SparkSession.builder.appName("Web Crawler DFS").master("yarn").getOrCreate()
sc = spark.sparkContext    

# Hiển thị phiên bản của Spark
print(f"SPARK VERSION: {spark.version}")

# Hiển thị tên của Spark Master
print(f"SPARK MASTER: {spark.sparkContext.master}")

# Seeds to start crawling
seeds = [
    #"https://vnexpress.net"
    "https://dantri.com.vn"
    #"https://vietnamnet.vn"
]

# Set the maximum depth for crawling
MAX_DEPTH = 3

# Function to extract article content
def get_article_content(html_content):
    title = html_content.find("h1", {"class": "title-detail"})
    desc = html_content.find("p", {"class": "description"})
    content = html_content.find("article", {"class": "fck_detail"})
    if title is None:
        title = html_content.find("h1", {"class": "title-page detail"})
        desc = html_content.find("h2", {"class": "singular-sapo"})
        content = html_content.find("div", {"class": "singular-content"})
    if title is not None:
        title = title.get_text(strip=True)
        desc = desc.get_text(strip=True)
        content = content.get_text(strip=True)
        return title + "\n" + desc + "\n" + content
    return ""

# Recursive function to fetch data by DFS
def fetch_by_dfs(url, base, max_depth=MAX_DEPTH, depth=0):
    if depth < max_depth:
        try:
            html_content = BeautifulSoup(requests.get(url).text, "html.parser")
            article_content = get_article_content(html_content)
            if article_content:
                file_name = url.split('/')[-1].replace('.html', '').replace('.htm', '') + '.txt'
                current_directory = os.getcwd()
                file_path = os.path.join(current_directory, 'output', file_name)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "w") as file:
                    print("WRITING TO FILE: " + file_name)
                    file.write(article_content)
                    
            a_tags = html_content.find_all("a")
            for link in a_tags:
                href = link.get("href")
                if href and not href.startswith("#") and not href.startswith("javascript:"):
                    if href.startswith("http"):
                        fetch_by_dfs(href, "", max_depth, depth + 1)
                    else:
                        fetch_by_dfs(base + href, base, max_depth, depth + 1)
        except Exception as ex:
            print(f"Error fetching URL {url}: {ex}")

# Parallelize the seed URLs
seed_rdd = sc.parallelize(seeds)

# Apply the crawling function to each URL in the seed set
seed_rdd.foreach(lambda url: fetch_by_dfs(url, url))

# Stop the Spark context
sc.stop()
