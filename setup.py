from distutils.core import setup

if __name__ == '__main__':
	import sys

	setup(
		name = 'Flickr.API',
		version = '0.4.4',

		author = "Gilad Raphaelli",
		author_email = "gilad@raphaelli.com",
		description = "A Python interface to the Flickr API",
		keywords = "flickr api",
		license = "Python",
		long_description = """This package implements an interface to the Flickr
		API, defined at http://flickr.com/services/api/.  It does not parse the
		response from Flickr allowing for any response format desired
		(xml/json/etc).""",
		platforms = 'any',
		packages = ['Flickr'],
		url = "http://g.raphaelli.com",
		classifiers = [
			"Development Status :: 4 - Beta",
			"Intended Audience :: Developers",
			"Operating System :: OS Independent",
			"Programming Language :: Python",
			"Topic :: Software Development :: Libraries :: Python Modules",
		]
	)
