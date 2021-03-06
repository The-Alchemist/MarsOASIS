# need this for curl command
import os

# need this for json formatting
import json

class REST:

	def __init__(self, url):

		# url for website
		self.url = url

	def GET(self, table):

		# wrap the bash command with python
		os.system("curl '" + self.url + table + "' > /tmp/data.json")

		# load json file
		with open('/tmp/data.json') as data_file: data = json.load(data_file)

		# clean up
		os.system("rm /tmp/data.json")

		# return dictionary
		return data

	def PUT(self, entry, table):

		# wrap the bash command with python
		os.system("curl -X PUT -d '" + json.dumps(entry) + "' '" + self.url + table + "'")

	def PATCH(self, entry, table):

		# wrap the bash command with python
		os.system("curl -X PATCH -d '" + json.dumps(entry) + "' '" + self.url + table + "'")

	def DELETE(self, entry):

		os.system("curl -X DELETE '" + self.url + entry + "'")
