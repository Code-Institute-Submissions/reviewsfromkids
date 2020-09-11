// Stripe javascript. Unfortunately, for each donation 'product' a new, same function with specific ID.
// Not very DRY

// 3 euro donation
(function() {

    var stripe = Stripe('pk_test_51HFc5ZFApEuWmDdSU11sbZEpbxfiXgwExMFnwH2f5K2ZCpgoiKtyZ10OyrSQ08hxayUS06kazNOKvnPdV7kV7GMV00hh13Vif4');

    var checkoutButton = document.getElementById('checkout-button-price_1HQ9OgFApEuWmDdSIun3qPzm');

    checkoutButton.addEventListener('click', function () {

        stripe.redirectToCheckout({
            
            lineItems: [{price: 'price_1HQ9OgFApEuWmDdSIun3qPzm', quantity: 1}],
            mode: 'payment',
            successUrl: 'https://reviewsfromkids.herokuapp.com/donations/success',
            cancelUrl: 'https://reviewsfromkids.herokuapp.com/donations',

        })

        .then(function (result) {

            if (result.error) {
            
                var displayError = document.getElementById('error-message');
                displayError.textContent = result.error.message;

            }

        });

    });

})();

// 10 euro donation
(function() {

    var stripe = Stripe('pk_test_51HFc5ZFApEuWmDdSU11sbZEpbxfiXgwExMFnwH2f5K2ZCpgoiKtyZ10OyrSQ08hxayUS06kazNOKvnPdV7kV7GMV00hh13Vif4');

    var checkoutButton = document.getElementById('checkout-button-price_1HQ9PJFApEuWmDdS9ngMsse0');

    checkoutButton.addEventListener('click', function () {

        stripe.redirectToCheckout({

            lineItems: [{price: 'price_1HQ9PJFApEuWmDdS9ngMsse0', quantity: 1}],
            mode: 'payment',
            successUrl: 'https://reviewsfromkids.herokuapp.com/donations/success',
            cancelUrl: 'https://reviewsfromkids.herokuapp.com/donations',

        })

        .then(function (result) {

            if (result.error) {
            
                var displayError = document.getElementById('error-message');
                displayError.textContent = result.error.message;
                
            }

        });

    });

})();

// BFF 2,50 euro per month
(function() {

    var stripe = Stripe('pk_test_51HFc5ZFApEuWmDdSU11sbZEpbxfiXgwExMFnwH2f5K2ZCpgoiKtyZ10OyrSQ08hxayUS06kazNOKvnPdV7kV7GMV00hh13Vif4');

    var checkoutButton = document.getElementById('checkout-button-price_1HQA0OFApEuWmDdSNkDKmpmY');
    
    checkoutButton.addEventListener('click', function () {
    
        stripe.redirectToCheckout({

            lineItems: [{price: 'price_1HQA0OFApEuWmDdSNkDKmpmY', quantity: 1}],
            mode: 'subscription',
            successUrl: 'https://reviewsfromkids.herokuapp.com/donations/success',
            cancelUrl: 'https://reviewsfromkids.herokuapp.com/donations',

        })

        .then(function (result) {

            if (result.error) {
            
                var displayError = document.getElementById('error-message');
                displayError.textContent = result.error.message;

            }

        });

    });

})();

// BBFF 5 euro per month
(function() {

    var stripe = Stripe('pk_test_51HFc5ZFApEuWmDdSU11sbZEpbxfiXgwExMFnwH2f5K2ZCpgoiKtyZ10OyrSQ08hxayUS06kazNOKvnPdV7kV7GMV00hh13Vif4');

    var checkoutButton = document.getElementById('checkout-button-price_1HQ9RXFApEuWmDdSrg3dcS0J');

    checkoutButton.addEventListener('click', function () {
    
        stripe.redirectToCheckout({

            lineItems: [{price: 'price_1HQ9RXFApEuWmDdSrg3dcS0J', quantity: 1}],
            mode: 'subscription',
            successUrl: 'https://reviewsfromkids.herokuapp.com/donations/success',
            cancelUrl: 'https://reviewsfromkids.herokuapp.com/donations',

        })

        .then(function (result) {

            if (result.error) {
            
                var displayError = document.getElementById('error-message');
                displayError.textContent = result.error.message;

            }

        });

    });

})();


