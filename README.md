# community-digikey-api-v3-lite
---------
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZHPF7ZLDCYEYY&source=url)

A community initiative to provide a lite wrapper for the Digikey set of API's  that handles all the necessary Authentication via the required Oauth2 Protocol.


    COMPLETED: productinformation
    COMPLETED: ordersupport
    TODO:barcode
    TODO:Ordering

This module requires [community-digikey-api-codegen-python-clients](https://github.com/auphofBSF/community-digikey-api-codegen-python-clients)
 a module that takes the digikey API V3 Swagger specification and locally builds  a set of python digikey client api's through the Swagger-Codegen, a java application.  
 
These API clients don't have full OAuth2 protocol handling. The Client App authentication (Oauth2 Protocol) is handled by a customized fork of Github@peeter123's  digikey-api. This  is originally a python digikey api Version 1 module. This fork has been altered to support V2 and the branch (https://github.com/auphofBSF/digikey-api.git@dev20w02apiV3) is used by these modules to handle the authentication by OAuth2.

The necessary production application needs to be registered with https://developer.digikey.com . Creating a free account is linked to your digikey account after first login into https://digikey.com or your local account such as https://digikey.co.nz.  Then login/create account with https://developer.digikey.com  and then register an `App`  where you will be asked to establishes the OAuth2 callback url(recommended to use https://localhost) and the the registration generates the `Client Id` and `Client Secret` for the client app. You will want to enable the api's you require. Presently these modules only support `Product Information API` and `Order Support API` see: https://developer.digikey.com/documentation/organization

see  requirements and installation for detail on the install procedures with regard to the 2 key requirements.

------------
## IF THIS WORK BENEFITS YOU in a way that you can contribute to my time in supporting Open Source Community Benefiting Software then please contribute here. 

# Any donations are always graciously accepted

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZHPF7ZLDCYEYY&source=url)

---------------------


## Versions
- DIGIKEY API version: v3
- community-digikey-api-codegen-python-clients,   version: 0.1.0
- 

## Requirements.

1) Python 3.4+
2) [community-digikey-api-codegen-python-clients](https://github.com/auphofBSF/community-digikey-api-codegen-python-clients)
3) [digikey-api V1 -Custom Branch](https://github.com/auphofBSF/digikey-api.git@dev20w02apiV3) (extended for OAuth authentication to digikey API V2)

## Installation

1) First ensure the [community-digikey-api-codegen-python-clients](https://github.com/auphofBSF/community-digikey-api-codegen-python-clients) are installed
2) Install digikey-api v1 modified to provide OAuth2 support for digikey V2
     `pip install -e git+https://github.com/auphofBSF/digikey-api.git@dev20w02apiV3#egg=digikey-api
`
1) Proceed to install this Lite wrapper `community-digikey-api-v3-lite` for the `community-digikey-api-codegen-python-clients`
2) Create a new or configure the example application using the Lite API



This python package `community-digikey-api-v3-lite` is hosted on Github, you can install directly from Github

```sh
pip install -e git+https://github.com/auphofBSF/community-digikey-api-build-python-client.git#egg=community-digikey-api-v3-lite

```
(you may need to run `pip` with root permission: `sudo pip install -e git+https://github.com/auphofBSF/community-digikey-api-build-python-client.git#egg=community-digikey-api-v3-lite`

Alternatively if this Repository is cloned into a local directory
```
cd <rootlocationforGitClones>
git clone https://github.com/auphofBSF/community-digikey-api-build-python-client.git#egg=community-digikey-api-v3-lite <my-community-digikey-api-buid-python-client>
cd <my-community-digikey-api-buid-python-client>
pip install -e .
```

## Usage

additional requirements for the `example/example.py` that need to be installed by your package manager of choice, `conda install -r /example/example-requirements.txt` or `pip install -r /example/example-requirements.txt` where `<mod>` is one of the following

    pandas >= 1.0.0
    tabulate >= 0.8.6

Copy and paste the following into a python code file or use the `example/example.py`

```python
"""
Example of using digikey_api_v3_lite
"""
import os
import pandas as pd
import digikey_api_v3_lite  as digiAPI


def modelItem_to_dict_generator(collection):
    """Create a lazy comprehension of an iterable collection of model items, effectively returning a generator.
    A response from a Digikey API query is often a list of Model items, objects of the particular class representing a model item.
    THis does not get easily consumed into some useful objects such as a Pandas DataFrame that would typically take a dictionary object.
    To convert a query response to a pandas list of model items as dictionary in an efficient manner I would suggest to use a lazy list comprehension, effectively returning a generator on the API response, that Pandas Dataframe can consume.

    """
    return(( item.to_dict() for item in collection))



# SETUP the Digikey authentication see https://developer.digikey.com/documentation/organization#production
os.environ['DIGIKEY_CLIENT_ID'] = '<DIGIKEY_APPLICATION_ID>'
os.environ['DIGIKEY_CLIENT_SECRET'] = '<DIGIKEY_SECRET>'
os.environ['DIGIKEY_STORAGE_PATH'] = r'<PATH_TO_THE_TOKEN_CACHING_LOCATION>'

# https://sso.digikey.com/as/authorization.oauth2?client_id=BHlFCi7SdXFoiMwgjYxaTUWCfrQW8vZR&response_type=code&redirect_uri=https%3A%2F%2Flocalhost%3A8139%2Fdigikey_callback

# SEARCH for part with Digikey Part Number (dkpn)
dkpn = '296-6501-1-ND'
part = digiAPI.ProductInformation().product_details(dkpn)
part
print(
f"""
Manufacturer Part Num: {part.manufacturer_part_number}
Detailed Desc:
---------------------
{part.detailed_description}


parameters:
---------------------
{pd.DataFrame(modelItem_to_dict_generator(part.parameters))[['parameter','value','value_id']].to_markdown()}

""")





#for further API info see https://developer.digikey.com/products
#Look up order history ,see the API for other named arguments that can be passed to the order_history or other queries
orderHistory = digiAPI.OrderDetails().order_history(start_date="2019-01-01", end_date="2020-01-01")

print(pd.DataFrame(modelItem_to_dict_generator(orderHistory)).to_markdown())

# Take the first item (salesorder ) in the Order_history and display the order lines


firstSalesOrder =orderHistory[0].salesorder_id
orderStatus = digiAPI.OrderDetails().order_status(salesorder_id=firstSalesOrder)

print(chr(10).join([shippingDetail.tracking_url for shippingDetail in orderStatus.shipping_details]))

# display all the tracking URL's
print(
f"""
Sales Order ID:{orderStatus.salesorder_id}

Shipping Tracking details:
---------------------------------------------------------------------------
{chr(10).join([shippingDetail.tracking_url for shippingDetail in orderStatus.shipping_details])}

Sales Order Line Items:
---------------------------------------------------------------------------
{pd.DataFrame(modelItem_to_dict_generator(orderStatus.line_items)).to_markdown()}
"""
)




```
