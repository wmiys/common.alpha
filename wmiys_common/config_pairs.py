"""
************************************************************************************
The ConfigPair class is used for configuring different variable values based on if 
the application execution enviornment is development or production.

This is somewhat of an ~interface~ that many strongly-typed/object-oriented languages
offer. Basically, every instance of a ConfigPair MUST provide values for both the DEV
and PRODUCTION properties each time the class is implemented.

For example, when in development the connection for the database requires the remote
IP address of the VPS, but when the application is running in production, it should 
use 'localhost' instead of the IP address.

Throughout the code, the variables that use the values found here SHOULD default to
the production value. That way, they only get altered when the application is being
run in development mode.
***************************************************************************************
"""

from collections import namedtuple

ConfigPair = namedtuple('ConfigPair', ['DEV', 'PRODUCTION'])


ApiUrls      = ConfigPair('http://10.0.0.82:5000', 'https://api.wmiys.com')
FrontEndUrls = ConfigPair('http://10.0.0.82:8000', 'https://wmiys.com')
DbHosts      = ConfigPair('104.225.208.163',       'localhost')

