import streamlit as st
import paypalrestsdk
import stripe
from config import get_config
from utils.session_manager import activate_premium

config = get_config()

# Configure PayPal
paypalrestsdk.configure({
    "mode": config.PAYPAL_MODE,
    "client_id": config.PAYPAL_CLIENT_ID,
    "client_secret": config.PAYPAL_SECRET
})

# Configure Stripe
stripe.api_key = config.STRIPE_SECRET_KEY

def handle_payment_success():
    """Handle successful payment from query parameters"""
    try:
        st.session_state.is_premium = True
        activate_premium(duration_days=30)
        st.success("🎉 Payment verified! Welcome to Premium Access.")
        st.balloons()
    except Exception as e:
        st.error(f"Error activating premium: {str(e)}")

def create_paypal_payment(amount, description):
    """Create PayPal payment"""
    try:
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": str(amount),
                    "currency": "USD"
                },
                "description": description
            }],
            "redirect_urls": {
                "return_url": "http://localhost:8501/?payment=success",
                "cancel_url": "http://localhost:8501/?payment=cancelled"
            }
        })
        
        if payment.create():
            return payment
        else:
            st.error(f"PayPal Error: {payment.error}")
            return None
    except Exception as e:
        st.error(f"Error creating PayPal payment: {str(e)}")
        return None

def create_stripe_checkout(price_id):
    """Create Stripe checkout session"""
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price": price_id,
                "quantity": 1
            }],
            mode="payment",
            success_url="http://localhost:8501/?payment=success",
            cancel_url="http://localhost:8501/?payment=cancelled"
        )
        return session
    except stripe.error.StripeError as e:
        st.error(f"Stripe Error: {str(e)}")
        return None

def generate_paypal_button_html(amount, description):
    """Generate PayPal Smart Buttons HTML"""
    return f"""
    <div id="paypal-button-container" style="max-width: 100%; margin: 20px 0;"></div>
    <script src="https://www.paypal.com/sdk/js?client-id={config.PAYPAL_CLIENT_ID}&currency=USD"></script>
    <script>
        paypal.Buttons({{
            createOrder: function(data, actions) {{
                return actions.order.create({{
                    purchase_units: [{{
                        amount: {{
                            value: '{amount}'
                        }},
                        description: '{description}'
                    }}]
                }});
            }},
            onApprove: function(data, actions) {{
                return actions.order.capture().then(function(details) {{
                    console.log('Payment successful:', details);
                    window.parent.location.href = window.parent.location.origin + window.parent.location.pathname + "?payment=success";
                }});
            }},
            onError: function(err) {{
                console.error('PayPal Error:', err);
                window.parent.location.href = window.parent.location.origin + window.parent.location.pathname + "?payment=cancelled";
            }}
        }}).render('#paypal-button-container');
    </script>
    """
