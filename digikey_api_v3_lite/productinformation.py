"""
Top-level API, provides access to the Digikey API for order_support
without directly instantiating a client object.
Also wraps the response JSON in types that provide easier access
to various fields.
"""

import os, logging
import digikey
import digikey_productinformation

from digikey_productinformation.rest import ApiException

class Digikey_ProductInformation():
    def __init__(self):
        # Configure API key authorization: apiKeySecurity
        configuration = digikey_productinformation.Configuration()
        configuration.api_key['X-DIGIKEY-Client-Id'] = os.getenv('DIGIKEY_CLIENT_ID')
        # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
        # configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'
        #Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
        configuration = digikey_productinformation.Configuration()
        self._digikeyApiTokenObject = digikey.oauth2.TokenHandler().get_access_token()
        configuration.access_token = self._digikeyApiTokenObject.access_token
        # create an instance of the API class
        self._api_instance = digikey_productinformation.PartSearchApi( 
                                digikey_productinformation.ApiClient(configuration))

    def product_details(self,digi_key_part_number,**kwargs):
        authorization = self._digikeyApiTokenObject.get_authorization()
        x_digikey_client_id = os.getenv('DIGIKEY_CLIENT_ID')
        try:
            api_response = self._api_instance.product_details(
                digi_key_part_number,
                authorization, 
                x_digikey_client_id, 
                **kwargs)

            return api_response
        except ApiException as e:
            print("Exception when calling digikey_productinformation->product_details: %s\n" % e)
            return {}

