import convertapi
def url2png(url):
	convertapi.api_secret = 'Z7Z4HpVF3n7e9I8H'
	x=convertapi.convert('png', {
	'Url': url
	}, from_format = 'web')
	return x.response['Files'][0]['Url']

