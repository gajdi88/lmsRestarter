import requests

def restart_url(url):
    response = requests.get(url+'/cgi-bin/restartsqlt.cgi')
    return response

def stop_url(url):
    response = requests.get(url+'/cgi-bin/stop.cgi')
    return response

def stop_lms(url):
    response = requests.get(url + '/cgi-bin/lms.cgi',params={'ACTION': 'Stop'})
    return response

def start_lms(url):
    response = requests.get(url + '/cgi-bin/lms.cgi',params={'ACTION': 'Start'})
    return response

lms_url = 'http://192.168.0.115'
urls= ['http://192.168.0.111','http://192.168.0.113']

print(stop_lms(lms_url))
print(start_lms(lms_url))

for url in urls:
    print(stop_url(url))
    print(restart_url(url))

