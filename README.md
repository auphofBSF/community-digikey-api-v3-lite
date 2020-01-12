# community-digikey-api-v3-lite
---------
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZHPF7ZLDCYEYY&source=url)

A community initiative to provide a lite wrapper for the Digikey set of API's  that handles all the necessary Authentication via the require Oauth2 Protocol.


    COMPLETED: productinformation
    COMPLETED: ordersupport
    TODO:barcode
    TODO:Ordering

THis uses that Swagger Codegen client api built by installing community-digikey-api-build-python-client


------------
## IF THIS WORK BENEFITS YOU in a way that you can contribute to my time in supporting Open Source Community Benefiting Software then please contribute here. 

# Any donations are always graciously accepted

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZHPF7ZLDCYEYY&source=url)

---------------------


## Versions
- DIGIKEY API version: v3
- Build Package version: 0.1.0

## Requirements.

Python 3.4+

## Installation

`pip install -e .`

If the python package is hosted on Github, you can install directly from Github

```sh
pip install -e git+https://github.com/auphofBSF/community-digikey-api-build-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install -e git+https://github.com/auphofBSF/community-digikey-api-build-python-client.git`


## Usage

```python
"""
Example of using digikey_api_v3_lite
"""

import os
import pandas as pd
import digikey_api_v3_lite  as digiAPI

from pprint import pprint


# SETUP the Digikey authentication see TODO: provide link to http://developer.digkey.com........
os.environ['DIGIKEY_CLIENT_ID'] = '<DIGIKEY_APPLICATION_ID>'
os.environ['DIGIKEY_CLIENT_SECRET'] = '<DIGIKEY_SECRET>'
os.environ['DIGIKEY_STORAGE_PATH'] = r'<PATH_TO_THE_TOKEN_CACHING_LOCATION>'


# SEARCH for part with Digikey Part Number (dkpn)
dkpn = '296-6501-1-ND'
part = digiAPI.ProductInformation().product_details(dkpn)
pprint(part.manufacturer_part_number)
pprint(part.detailed_description)
pprint(part.to_dict())



def modelItem_to_dict_generator(collection):
"""
Create a lazy comprehension of an iterable collection of model items, effectively returning a generator.

A response from a Digikey API query is often a list of Model items, objects of the particular class representing a model item.

 THis does not get easily consumed into some useful objects such as a Pandas DataFrame that would typically take a dictionary object.

 To convert a query response to a pandas list of model items as dictionary in an efficient manner I would suggest to use a lazy list comprehension, effectively returning a generator on the API response, that Pandas Dataframe can consume.

"""
    return(( item.to_dict() for item in collection))


#for further API info see https://developer.digikey.com/products
#Look up order history ,see the API for other named arguments that can be passed to the order_history or other queries
orderHistory = digiAPI.OrderDetails().order_history(start_date="2019-01-01", end_date="2020-01-01")

pd.DataFrame(modelItem_to_dict_generator(orderHistory))

# Take the first item (salesorder ) in the Order_history and display the order lines
firstSalesOrder =orderHistory[0].salesorder_id
orderStatus = digiAPI.OrderDetails().order_status(salesorder_id=firstSalesOrder)
# display all the tracking URL's
pprint([shippingDetail.tracking_url for shippingDetail in orderStatus.shipping_details])
# produce a Dataframe of the line_items
pd.DataFrame(modelItem_to_dict_generator(orderStatus.line_items))

```
