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


