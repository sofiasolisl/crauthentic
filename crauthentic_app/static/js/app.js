const price = document.getElementById('price').textContent
console.log(price)
paypal.Buttons({
    
    createOrder: (data, actions) => {
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: price
                }
            }]
        });
    },

    onApprove: (data, actions) => {
        return fetch(`/payments/${data.orderID}/capture`, {
            method: "post",
        })
            .then((response) => response.json())
            .then((orderData) => {
                console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                const transaction = orderData.purchase_units[0].payments.captures[0];
                window.location.href ="http://127.0.0.1:5000/confirmation";
            });
    }
}).render('#paypal-button-container');

 





//https://medium.com/@andrii.gorshunov/paypal-flask-integration-python-2022-1c012322801d