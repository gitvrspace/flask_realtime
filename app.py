from flask import Flask,request
import json
import urllib.parse as parse
import urllib.request as req
import  requests
from  bs4  import  BeautifulSoup  as  bs
import schedule
import time

old_links  = []
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Telegram RealTime Bot'

def  get_new_links(old_links):
  url  = f'https://finance.naver.com/'
  response  =  requests.get(url)
  soup  =  bs(response.text , 'html.parser')
  section  =  soup.select_one('div.section_strategy')
  item  =  section.find_all('a')
  list_links  = [i.text for  i  in  item]
  new_links  = [link  for  link  in  list_links  if  link  not  in  old_links]
  #print(new_links)
  return  new_links

def  send_links():
  global old_links
  new_links  =  get_new_links(old_links)

  if  new_links:
    for  link  in  new_links:
      baseURL = 'https://api.telegram.org/bot6876786031:AAHPnC8_plNa-58NlyMzYy_qhU1nVHaCCxo/'
      query = parse.urlencode([
        ('chat_id', 7167388284),
        ('text', link)
      ])
      command = 'sendMessage?'+query
      req.urlopen(baseURL+command)
    else:
      pass

  old_links +=  new_links.copy()

@app.route('/6876786031:AAHPnC8_plNa-58NlyMzYy_qhU1nVHaCCxo', methods=['POST','GET'])
def telegram():
    send_links()
    return json.dumps({'success':True})


