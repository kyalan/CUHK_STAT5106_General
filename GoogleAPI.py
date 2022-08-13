class googler():
    
    def __init__(self):
        from getpass import getpass        
        self.api_key = getpass('Please input Google MAP API key:')

    def getGeojs(self, address, verbose=False):

        import urllib.request, urllib.parse, urllib.error
        import json
        import ssl

        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json'

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        if len(address) < 1: 
            print('==== Failure To Retrieve ====')
            print('Address is None Value.')
            return {}        

        parms = {}
        parms['address'] = address
        parms['key'] = self.api_key
        url = serviceurl + '?' + urllib.parse.urlencode(parms)

        if verbose: print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        if verbose: print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            return {}

        return js
    
    def getKnowjs(self, query, verbose=False):
        
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

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            return {}

        return js         
