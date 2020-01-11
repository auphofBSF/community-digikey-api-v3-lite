"""
Top-level API, provides access to the Digikey API for order_support
without directly instantiating a client object.
Also wraps the response JSON in types that provide easier access
to various fields.
"""

import os, logging
import digikey
import digikey_ordersupport as digikey_ordersupport

from digikey_ordersupport.rest import ApiException

class OrderDetails():
    def __init__(self):
        # Configure API key authorization: apiKeySecurity
        configuration = digikey_ordersupport.Configuration()
        configuration.api_key['X-DIGIKEY-Client-Id'] = os.getenv('DIGIKEY_CLIENT_ID')
        # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
        # configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'
        #Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
        configuration = digikey_ordersupport.Configuration()
        self._digikeyApiTokenObject = digikey.oauth2.TokenHandler().get_access_token()
        configuration.access_token = self._digikeyApiTokenObject.access_token
        # create an instance of the API class
        self._api_instance = digikey_ordersupport.OrderDetailsApi( 
                                digikey_ordersupport.ApiClient(configuration))


    def order_history( self, **kwargs):
        authorization = self._digikeyApiTokenObject.get_authorization()
        # authorization = 'authorization_example' # str | OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" style=\"color:blue\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info.
        x_digikey_client_id = os.getenv('DIGIKEY_CLIENT_ID') # str | The Client Id for your App.

        # customer_id = 0 # int | CustomerId that is on the Digi-Key account with which you authenticated. If not provided, will  default to the first CustomerId on the Digi-Key account. (optional) (default to 0)
        # open_only = False # bool | If true will only return open orders. If false, will return open and closed orders. (optional) (default to false)
        # include_company_orders = False # bool | Include all company orders for the location associated with the given CustomerId. (optional) (default to false)
        # start_date = '2019-01-01' # str | Begining of date range in ISO 8601 format. For example: 2018-10-31 (optional) (default to )
        # end_date = '2020-01-01' # str | End of date range in ISO 8601 format. For example: 2018-10-31 (optional) (default to )
        # includes = '' # str | Comma separated list of fields to return. Used to customize response to reduce bandwidth with  fields that you do not wish to receive. For example: \"SalesOrderId,PurchaseOrder\" (optional)


        try:
            # Retrieves a list of SalesorderIds and dates for all Salesorders within a date range belonging to a CustomerId.
            api_response = self._api_instance.order_history(authorization, x_digikey_client_id, **kwargs)
            # start_date=start_date, end_date=end_date)
            # ,customer_id=customer_id, open_only=open_only, include_company_orders=include_company_orders, start_date=start_date, end_date=end_date, includes=includes)
            # dir(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling OrderDetailsApi->order_history: %s\n" % e)
            return {}


    def order_status( self, salesorder_id, **kwargs):
        authorization = self._digikeyApiTokenObject.get_authorization()
        # authorization = 'authorization_example' # str | OAuth Bearer Token. Please see<a href= \"https://developer.digikey.com/documentation/oauth\" style=\"color:blue\" target= \"_blank\" > OAuth 2.0 Documentation </a > page for more info.
        x_digikey_client_id = os.getenv('DIGIKEY_CLIENT_ID') # str | The Client Id for your App.


        try:
            # Retrieves a list of SalesorderIds and dates for all Salesorders within a date range belonging to a CustomerId.
            api_response = self._api_instance.order_status(salesorder_id, authorization, x_digikey_client_id, **kwargs)
            # start_date=start_date, end_date=end_date)
            # ,customer_id=customer_id, open_only=open_only, include_company_orders=include_company_orders, start_date=start_date, end_date=end_date, includes=includes)
            # dir(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling OrderDetailsApi->order_status: %s\n" % e)
            return {}

