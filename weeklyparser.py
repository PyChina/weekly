import urllib2

import re

import sys
import getopt

class Item:
	def __init__(self, title, title_url, content, website, shared_by_name, shared_by_url):
		self.title = title
		self.title_url = title_url
		self.content = content
		self.website = website
		self.shared_by_name = shared_by_name
		self.shared_by_url = shared_by_url
def Usage():
	print 'weeklyparser.py usage:'
	print '-u, --url: input issue url.'

def GetContent(url):
	return urllib2.urlopen(url).read()

def GenerateIssue(content):
	issue_regex = re.compile('<title>.*?Issue.*?#(\d+):')
	block_regex = re.compile('')
	title_regex = re.compile('')
	title_url_regex = re.compile('')
	content_regex = re.compile('')
	website_regex = re.compile('')
	shared_by_name_regex = re.compile('')
	shared_by_url_regex = re.compile('')

	
def main(argv):
	try:
		opts, args = getopt.getopt(argv[1:], 'u:', ['url='])
	except getopt.GetoptError, err:
		print str(err)
		Usage()
		sys.exit(2)
	for o, a in opts:
		if o in ('-u', '--url'):
			print a
			global content 
			content = GetContent(a)

	GenerateIssue(content)

if __name__ == "__main__":
	main(sys.argv)


