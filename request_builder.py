




class RequestBuilder(object):
	def __init__(self, url):
		self.url = url



	def run(self):
		self.r = requests.get(url)
		return self.r