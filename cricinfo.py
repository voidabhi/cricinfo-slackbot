

import requests
from xmltodict import parse
from pprint import pprint

class Match(object):
    '''
        Represents a cricinfo match
    '''

    def __init__(self, title, link, description, guid):
        self.title = title
        self.link = link
        self.description = description
        self.guid = guid

    @staticmethod
    def from_dict(d):
        # if type(d) is not type(dict):
        #     raise TypeError('expected argument to be dictionary got %s' % type(dict))
        title = d.get('title', 'No Title')
        link = d.get('link', 'No Link')
        description = d.get('description', 'No description')
        guid = d.get('guid', 'No Guid')
        return Match(title, link, description, guid)

    def __repr__(self):
        return '<Match=%s>'%(self.title)

class Cricinfo(object):
    RSS_URL='http://static.cricinfo.com/rss/livescores.xml'

    def __init__(self):
        pass

    def _fetch(self):
       r = requests.get(self.RSS_URL)
       return parse(r.text)

    def matches(self):
        matches = []
        try:
            matches_xml = self._fetch()['rss']['channel']['item']
        except Exception as e:
            print e
            return []
        for match_xml in matches_xml:
            matches.append(Match.from_dict(match_xml))
        return matches



if __name__=='__main__':
    pass
