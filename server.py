from fastmcp import FastMCP
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

mcp = FastMCP("Get News Flash")

@mcp.tool(
	name= "get_news_flash",
	description= "Get the latest news flash about crypto (usually the up-to-date events). It can be used to query the latest happened event in crypto community. (e.g. the famous CEX launched a new activity, a trending project emerges in market, etc.)",
  tags= {"news", "cryptocurrency", "events", "market"}
)
def get_news_flash() -> str:
  blockbeat_new_uri = "https://api.theblockbeats.news/v2/rss/newsflash"
  try:
    response = requests.get(blockbeat_new_uri, timeout=10)
    response.raise_for_status()
  except requests.RequestException as e:
    return f"Error fetching news flash: {str(e)}"
  
	
  try:
    root = ET.fromstring(response.text)
  except ET.ParseError as e:
    return f"Parsing news flash data error: {str(e)}"
  
  results = []
  channel = root.find('channel')
  for item in channel.findall('item'):
    title = item.find('title').text
    link = item.find('link').text
    description = item.find('description').text
    pubdate = item.find('pubDate').text
    clean_description = BeautifulSoup(description, 'html.parser').get_text()
    results.append(f"Title: {title}\nLink: {link}\nDescription: {clean_description}\nPubdate: {pubdate}")
  
  if results:
    return '\n\n'.join(results)
  else:
    return "No news flash data found"
  
@mcp.tool(
	name= "get_article",
	description= "Get the latest crypto-related articles. Articles are always about the deep research of an crypto project / a company. Besides this, they can also be about the analysis of the crypto market and etc.",
  tags= {"article", "cryptocurrency", "market", "market analysis"}
)
def get_article() -> str:
  blockbeat_new_uri = "https://api.theblockbeats.news/v2/rss/article"
  try:
    response = requests.get(blockbeat_new_uri, timeout=10)
    response.raise_for_status()
  except requests.RequestException as e:
    return f"Error fetching article: {str(e)}"
  
	
  try:
    root = ET.fromstring(response.text)
  except ET.ParseError as e:
    return f"Parsing article data error: {str(e)}"
  
  results = []
  channel = root.find('channel')
  for item in channel.findall('item'):
    title = item.find('title').text
    link = item.find('link').text
    description = item.find('description').text
    pubdate = item.find('pubDate').text
    clean_description = BeautifulSoup(description, 'html.parser').get_text()
    results.append(f"Title: {title}\nLink: {link}\nDescription: {clean_description}\nPubdate: {pubdate}")
  
  if results:
    return '\n\n'.join(results)
  else:
    return "No article data found"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")