----------------
Changes in this Fork
----------------
In original version, settings from django.conf are used for all gatewate and integration properties. 
This fork modifies it and instead looks up the same properties from settings.GATEWAY_SETTINGS object. 

This changes things from being strictly static/global to more flexible. For example, this object could be populated from database (Model). 

Obviously, need to be smart about where this data is stored. Keep in mind that this data is sensative and needs to be secured.

----------------
Django-Merchant
----------------

Django-Merchant is a django application that enables you to use
multiple payment processors from a single API.

Gateways
---------

Following gateways are supported:

* Authorize.net
* Paypal
* Eway
* Braintree Payments (Server to Server)

Off-Site Processing
--------------------

* Paypal
* RBS WorldPay
* Google Checkout
* Amazon FPS
* Braintree Payments (Transparent Redirect)

Documentation
--------------

Documentation is automatically built and published online at:

http://readthedocs.org/docs/django-merchant/en/latest/
