class geographer():
    
    api_key = None
    
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