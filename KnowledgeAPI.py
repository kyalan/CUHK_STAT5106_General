class knowledger():
    
    api_key = None
    
    def __init__(self):
        from getpass import getpass        
        self.api_key = getpass('Please input Google MAP API key:')

    def getKnowjs(self, query, languages='en', verbose=False):
        
        import urllib.request, urllib.parse, urllib.error
        import json
        import ssl

        serviceurl = 'https://kgsearch.googleapis.com/v1/entities:search'

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        if len(query) < 1: 
            print('==== Failure To Retrieve ====')
            print('Query is None Value.')
            return {}        

        params = {
            'query': query,
            'limit': 10,
            'indent': True,
            'key': self.api_key,
            'languages': languages,
        }
        url = serviceurl + '?' + urllib.parse.urlencode(params)

        if verbose: print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        if verbose: print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js:
            print('==== Failure To Retrieve ====')
            print(data)
            return {}

        return js        
