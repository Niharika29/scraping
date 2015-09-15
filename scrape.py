import mwclient
from time import mktime
from datetime import datetime
import re
import time
from mwclient.page import Page

# site = mwclient.Site('en.wikipedia.org')
# page = 'Barack Obama'

# response = site.api(action = 'query', prop = 'info' )
# print response

# page = site.Pages['Wikipedia:Database reports/Forgotten articles']
# rev = page.revisions(limit = 1, prop = 'timestamp|comment|content').next()
# print datetime.fromtimestamp(mktime(rev['timestamp']))

def main():
	# P229 paste by Krenair. Query only available to people with shell access. 
	# More info: https://wikitech.wikimedia.org/wiki/Wikimedia_binaries#mwgrep
	fa = open( 'Source.txt' )
	lines = fa.readlines()
	final = open( 'final.txt', 'w' )
	i = 0

	while i < len( lines ):
		comp = map(str, lines[i].split())
		site = comp[0]
		page = comp[1]

		res = findch( site )
		host = res[0]
		url = res[1]
		i = i + 1
		if res > 0:
			try:
				website = mwclient.Site( str(host) + '.' + str(url) + '.org' )
			except:
				final.write('Error: no site such as: ' + str(host) + '.' + str(url) + '.org' + '\n' )
				continue

			webpage = Page( website, page )
			if webpage.exists is True:
				final.write( str(host) + str(url) + '\t\t' + page + '\t\t' + str(webpage.length) + '\n' )
			else: 
				final.write( 'Error: ' +  str(host) + str(url) + '\t' + page + ' :Page doesnt exist' + '\n' )


def findch( site ):
	if site.find('wikinews') > 0:
		return [ site[0:site.find( 'wikinews' )], site[site.find('wikinews'):] ]
	elif site.find('wikibooks') > 0:
		return [ site[0:site.find( 'wikibooks' )], site[site.find('wikibooks'):] ]
	elif site.find('wikiquote') > 0:
		return [ site[0:site.find( 'wikiquote' )], site[site.find('wikiquote'):] ]
	elif site.find('wikisource') > 0:
		return [ site[0:site.find( 'wikisource' )], site[site.find('wikisource'):] ]
	elif site.find('wikiversity') > 0:
		return [ site[0:site.find( 'wikiversity' )], site[site.find('wikiversity'):] ]
	elif site.find('wiktionary') > 0:
		return [ site[0:site.find( 'wiktionary' )], site[site.find('wiktionary'):] ]
	elif site.find('wikivoyage') > 0:
		return [ site[0:site.find( 'wikivoyage' )], site[site.find('wikivoyage'):] ]
	elif site.find('wikimedia') > 0:
		return [ site[0:site.find( 'wikimedia' )], site[site.find('wikimedia'):] ]
	elif site.find('mania') > 0:
		return [ site[0:13], 'wikimedia' ]
	elif site.find('commons') > 0:
		return [ 'commons', 'wikimedia' ]
	elif site.find('meta') > 0:
		return [ 'meta', 'wikimedia' ]
	elif site.find('strategy') > 0:
		return [ 'strategy', 'wikimedia' ]
	elif site.find('incubator') > 0:
		return [ 'incubator', 'wikimedia' ]
	elif site.find('outreach') > 0:
		return [ 'outreach', 'wikimedia' ]
	elif site.find('wiki') > 0:
		return [ site[0:site.find('wiki')], 'wikipedia' ]
	else:
		return [ -1, -1 ]


main()

# 	print code + '\n'


# 	ls = map(str, lines[i].split())
# 	code.append( ls[0][0:2] )
# 	i = i + 1
# code.sort()
# code = set(code)
# for x in code:
# 	final.write( x + '\n' )


