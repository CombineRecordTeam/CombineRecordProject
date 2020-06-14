##unitedproject v0.1
##create_date:20200614
##Feature of v0.1：update/combine/check of data stream
##more invisible recorder

class ConfigHttp:
	def __init__(self, host, port, headers):
		self.host = host
		self.port = port
		self.headers = headers

	# Pack HTTP GET Request 

	def get(self, url, params=None):
		# params = urllib.parse.urlencode(params)
		url = "http://"+self.hosts+":"+self.port+url
		print(url)
		try:
			r = request.get(url, params=params, headers=self.headers)
			r.encoding = 'UTF-8'
			dcit_r = json.loads(r.text)
			print(json.loads(r.text))
			return dcit_r
		except Exception:
			print('no json data returned')
			return {}

	# Pack HTTP POST request method，including photo pattern
	def post(self, url, data=None, files=None):
		# data = eval(data)
		url = 'http://' + self.host + ':' + str(self.port)+url
		r = requests.post(url, files=files, data=data)
		json_response = r.text
		print(json_response)
		return json_response


	# video upload module
	def upload():
		getToken()
		f = {'Filename':'video_test',
				  'Filedata':('1.mp4',open(u'/app/dgm/1.mp4', 'rb'),'application/octet-stream'),
				  'Upload':'video_test2'
		}
		up = baseHttp.ConfigHttp(host=UPLOAD_HOST, port=UPLOAD_PORT,headers=HEADER)
		url = "/api/upload?do=upload&type=4&op=video&sid="+CODE +"&token=" + TOKEN 
		res = up.post(url=url, files=f)


	# data combine module (not complete)
	def combine():
		getcombine
		s = {'Filename':}

	def swipeUp(dr,n,t=2000):
		L = dr.get_window_size()
		x1 = L['width'] * 0.5
		y1 = L['height'] * 0.75
		y2 = L['height'] * 0.25
		for i in range(n):
			dr.swipe(x1,y1,x1,y2,t)

			

def main():
