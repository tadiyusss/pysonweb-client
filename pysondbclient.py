import requests
import json

class PysonWeb:
        def __init__(self, ip, username, password, port=3363):
            try:
                requests.get('http://' + ip + ':' + str(port))
            except requests.exceptions.ConnectionError:
                raise Exception("Unable to establish new connection to server.")
            self.ip = ip
            self.username = username
            self.password = password
            self.port = str(port)

        def remove(self, tbl_name, search_query):
            host = 'http://' + self.ip + ':' + self.port + '/remove'
            request_post = requests.post(host, data={'tbl_name': tbl_name, 'search_query': str(search_query), 'username': self.username, 'password': self.password})
            return json.loads(request_post.text)

        def insert(self, tbl_name, data):
            host = 'http://' + self.ip + ':' + self.port + '/insert'
            request_post = requests.post(host , data={'tbl_name': tbl_name, 'data': str(data), 'username': self.username, 'password': self.password})
            return json.loads(request_post.text)

        def update(self, tbl_name, search_query, update_data):
            host = 'http://' + self.ip + ':' + self.port + '/update'
            data = {
                'tbl_name': tbl_name,
                'data': str(update_data),
                'search_query': str(search_query),
                'username': self.username,
                'password': self.password
            }
            request_post = requests.post(host, data)
            return json.loads(request_post.text)

        def search(self, tbl_name, search_query):
            host = 'http://' + self.ip + ':' + self.port + '/search'
            request_post = requests.post(host, data={'tbl_name': tbl_name, 'search_query': str(search_query), 'username': self.username, 'password': self.password})
            return json.loads(request_post.text)

        def drop(self, tbl_name):
            host = 'http://' + self.ip + ':' + self.port + '/drop'
            request_post = requests.post(host, data={'tbl_name': tbl_name, 'username': self.username, 'password': self.password})
            return json.loads(request_post.text)

        def create(self, tbl_name):
            host = 'http://' + self.ip + ':' + self.port + '/create'
            request_post = requests.post(host, data={'tbl_name': tbl_name, 'username': self.username, 'password': self.password})
            return json.loads(request_post.text)

        def list_tbl(self):
            host = 'http://' + self.ip + ':' + self.port + '/list'
            request_post = requests.post(host, data={'username': self.username, 'password': self.password})
            return json.loads(request_post.text)



