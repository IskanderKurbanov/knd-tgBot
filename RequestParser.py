

class InvalidRequest(Exception):
	pass


class Request_parser:
	"A simple http request object"
	
	def __init__(self, raw_request):
		self._raw_request = raw_request
		
		self._method, self._path, self._protocol, self._headers = self.parse_request()
	

	def parse_request(self):
		"Turn basic request headers in something we can use"
		temp = [i.strip() for i in self._raw_request.splitlines()]
		
		if -1 == temp[0].find('HTTP'):
			raise InvalidRequest('Incorrect Protocol')
		
		# Figure out our request method, path, and which version of HTTP we're using
		method, path, protocol = [i.strip() for i in temp[0].split()]
		
		# Create the headers, but only if we have a GET reqeust
		headers = {}
		if 'GET' == method:
			for k, v in [i.split(':', 1) for i in temp[1:-1]]:
				headers[k.strip()] = v.strip()
		else:
			raise InvalidRequest('Only accepts GET requests')
		
		return method, path, protocol, headers


	def get_little_data(self):
		return self._path, self._method, self._protocol
	

	def __repr__(self):
		return repr({'method': self._method, 'protocol': self._protocol, 'path': self._path}) #    'headers': self._headers,