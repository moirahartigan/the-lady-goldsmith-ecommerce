from django.http import HttpResponse


class StripeWH_Handler:
    """
    A class to handle Stripe webhooks
    """

    def __init__(self, request):
        """
        Initilisation of handler
        Args:
            request (object): Request object
        Returns:
            Request
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        Args:
            self (object): Self object
            event: event
        Returns:
            HttpResponse object
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        Args:
            self (object): Self object
            event: event
        Returns:
            HttpResponse object
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        Args:
            self (object): Self object
            event: event
        Returns:
            HttpResponse object
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
