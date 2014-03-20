from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
import os
import time


def getScores(url):
  scores = []
  jsn = json.loads(urlopen(url).read())
  html = jsn['content']
  soup = BeautifulSoup(html, 'lxml')
  game = soup.findAll('div', {'class': 'game'})
  for g in game:
    a = g.find('a')
    if a.has_attr('title'):
      if a['title'][0:7] == 'Current':
        score = a['title']
        status = g.find('dd', {'class': 'status'}).text.strip()
        scores.append({'score': score, 'status': status})
      elif a['title'][0:5] == 'Final':
        score = a['title']
        status = g.find('dd', {'class': 'state'}).text.strip()
        scores.append({'score': score, 'status': status})
  return scores


def main():
  final = 0
  url = 'http://sports.yahoo.com/__xhr/sports/scorestrip-gs/?d=full&b=&format=realtime&league=ncaab'
  scores = getScores(url)
  while final < len(scores):
    final = 0
    os.system('clear')
    scores = getScores(url)
    for game in scores:
      print game['score'], game['status']
      if game['score'][0:7] != 'Current':
        final += 1
    time.sleep(30)


if __name__ == '__main__':
  main()
