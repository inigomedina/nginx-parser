import re

def process_log(log):
    #files = get_files(requests)
    #totals = file_occur(files)
    requests = get_requests(log)
    for r in requests:
	if 'Googlebot' in r[4]:
	    print r[0],

def get_requests(f):
    log_line = f.read()
    pat = (r''
           '(\d+.\d+.\d+.\d+)\s-\s-\s' #IP address
           '\[(.+)\]\s' #datetime
	   '"GET\s(.+)\s\w+/.+"\s\d+\s'
	   '\d+\s"(.+)"\s' #referrer
           '"(.+)"' #user agent
        )
    requests = find(pat, log_line, None)
    return requests

def find(pat, text, match_item):
    match = re.findall(pat, text)
    if match:
        return match
    else:
        return False

def get_files(requests):
    #get requested files with req
    requested_files = []
    for req in requests:
        #req[2] for req file match, change to
        #data you want to count totals
        requested_files.append(req[2])
    return requested_files

def file_occur(files):
    #file occurrences in requested files
    d = {}
    for file in files:
        d[file] = d.get(file,0)+1
    return d

def test_log(log):
    for f in log:
	r = re.search(r'(.*) - (.*) \[(.*)\] \"(.*)\"', f)
	#r = re.search(r'(.*) - (.*) \[(.*)\] \"(.*)\" (\d+) (\d+) "(\S+)" ["](.*)["] ["](.*)', f)
        if r.groups()[0]:
	    print r.groups()[0]
        if r.groups()[1]:
	    print r.groups()[1]

if __name__ == '__main__':

    #nginx access log, standard format
    log_file = open('access.log', 'r')

    #return dict of files and total requests
    print(process_log(log_file))
    #print(test_log(log_file))
