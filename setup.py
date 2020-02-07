# coding: utf-8

"""
    An easy/lite wrapper for Digikey V3 API's  offering the full API responses from the swagger Codegen API clients

    This wrapper handles the Oauth2 protocol by leveraging the work done by @peeter123 in the digikey-apiV2 to access part information.
    Digikey's V3 of the API breaks structure from V2. As yet there is no compatability layer between V3 and V2 to back support.

    This series of packages identified by community-digikey-api-* leverages the Swagger Configurations (JSON format) to generate the API's and thus avoid hand coding

    This wrapper module and the builder are the only hand coded modules.  THis wrapper is were any further customization should take place.
    The full API queries and responses are available for the api's currenty enabled

    COMPLETED: productinformation
    COMPLETED: ordersupport
    TODO:barcode
    TODO:Ordering


    See README.md for installation and examples

    Digikey API's use OpenAPI spec version: v3
    Contact: auphofBSF_GH1@blacksheepfarm.co.nz
    Builder and community produced Digikey interface by: https://github.com/auphofBSF with Oauth2 token management from the Digikey V2 api https://github.com/peeter123/digikey-api
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "community-digikey-api-v3-lite"
VERSION = "0.1.0"
# To install the library, run the following
#
# pip install -e .
#
# prerequisite: pip, gitpython
# 

REQUIRES = [
    # "community-digikey-api-client-productinformation @ git+https://github.com/auphofBSF/community-digikey-api-productinformation.git"
    # ,"community-digikey-api-client-ordersupport @ git+https://github.com/auphofBSF/community-digikey-api-ordersupport.git"
    "digikey-api @ git+https://github.com/auphofBSF/digikey-api/@dev20w02apiV3",
    "community-digikey-api-codegen-python-clients @ git+https://github.com/auphofBSF/community-digikey-api-codegen-python-clients.git",
    
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Lite implementation of Digikey V3 API's ",
    author_email="auphofBSF_GH1@blacksheepfarm.co.nz",
    url="https://github.com/auphofBSF/community-digikey-api-v3-lite",
    keywords=["Swagger", "Digikey Api"],
    install_requires=REQUIRES,
    package_dir={'': 'src'},
    packages=find_packages('src'), #['digikey_api_v3_lite'], 
    include_package_data=True,
    long_description="""\
       This wrapper handles the Oauth2 protocol by leveraging the work done by @peeter123 in the digikey-apiV2 to access part information.
       Digikey's V3 of the API breaks structure from V2. As yet there is no compatability layer between V3 and V2 to back support..  # noqa: E501
    """
)

