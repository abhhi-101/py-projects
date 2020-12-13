import os 
import queue
import requests
import threading

directory = 'C:\\Users\shweta birdawade\Downloads\wordpress-5.6\wordpress'
target = 'https://starleaf.com'
filters = ['.jpg','.png','.gif','.css','.scss']
threads = 10
os.chdir(directory)

web_paths = queue.Queue()

for r,d,f in os.walk('.'):
	for file in f:
		remote_path = '%s%s'%(r,file)
	if remote_path.startswith('.'):
		remote_path = remote_path[1:]
		
	if os.path.splitext(file)[1] not in filters:
		web_paths.put(remote_path)

def test_remote():
	while not web_paths.empty():
		path = web_paths.get()
		if path == 'xmlrpc.php':
			path = '/xmlrpc.php'
		path = path.replace('\\','/')
		
		url = '%s%s'%(target,path)
		req = requests.get(url)
		print('[%d] => %s' %(req.status_code,req.url))
		req.close()
for i in range(1,10):
	print('thread : %d'%i)
	t = threading.Thread(target=test_remote())
	t.start