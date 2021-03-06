from billing import Integration
from django.conf import settings
from paypal.standard.conf import POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT
from django.conf.urls.defaults import patterns, include
from paypal.standard.ipn.signals import payment_was_flagged, payment_was_successful
from billing.signals import transaction_was_successful, transaction_was_unsuccessful

class PayPalIntegration(Integration):
    def __init__(self):
        # Required Fields. Just a template for the user
        self.fields = {"item_name": "",
                       "invoice": "",
                       "amount": 0,
                       }

    @property
    def test_mode(self):
        return getattr(settings.GATEWAY_SETTINGS, "PAYPAL_TEST_MODE", True)


    @property
    def service_url(self):
        if self.getattr(settings.GATEWAY_SETTINGS, "PAYPAL_TEST_MODE", True):
            return SANDBOX_POSTBACK_ENDPOINT
        return POSTBACK_ENDPOINT

    def get_urls(self):
        urlpatterns = patterns('',
           (r'^', include('paypal.standard.ipn.urls')),
            )
        return urlpatterns

def unsuccessful_txn_handler(sender, **kwargs):
    transaction_was_unsuccesful.send(sender=sender.__class__,
                                     type="purchase",
                                     response=self)

def successful_txn_handler(sender, **kwargs):
    transaction_was_succesful.send(sender=sender.__class__,
                                   type="purchase",
                                   response=self)

payment_was_flagged.connect(unsuccessful_txn_handler)
payment_was_successful.connect(successful_txn_handler)
