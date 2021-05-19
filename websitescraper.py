from urllib.request import urlopen
import urllib.parse, urllib.error
import json
import ssl
from datetime import date

today = str(date.today())
enddate = today.strip('-')
enddate = enddate[0] + enddate[1] + enddate[2]
print(enddate)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
APIKEY = None #Insert API Key here
fields = ['Technology', 'Medical', 'Economics', 'Politics', 'Environment', 'Sports']
data = {'q':'Medical','fq':'source:{"The Guardian"}','facet_fields':'source','facet': 'true',
'begin_date': '20201201', 'end_date': enddate,'api-key' : APIKEY}
defaulturl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'
def execute():
    link = defaulturl + urllib.parse.urlencode(data)
    print(link)
    fhandle = urllib.request.urlopen(link, context = ctx).read()
    return fhandle

def sortresults():
    data = execute()
    data = json.loads(data)
    hello = json.dumps(str(data),sort_keys = True, indent = 4, separators = ('\n', '\n'))
    count = 0
    while True:
        try:
            summary = data['response']['docs'][count]
            for splice in summary:
                if splice == 'abstract' or splice == 'lead_paragraph' or splice == 'source':
                    print(splice, summary[splice], '\n')
            count += 1
        except:
            break
        print('\n\n')
    print('End of Document')

sortresults()
