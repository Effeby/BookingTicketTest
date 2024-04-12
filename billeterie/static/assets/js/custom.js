function updateBookingSummary() {
    var ticketQuantity = document.getElementById('ticket-quantity').value;
    var ticketPrice = document.getElementById('ticket-quantity').getAttribute('data-ticket-price');
    var totalPrice = ticketQuantity * ticketPrice;

    document.getElementById('ticket-quantity-display').innerText = ticketQuantity;
    document.getElementById('ticket-price').innerText = ticketPrice;
    document.getElementById('total-price').innerText = totalPrice;
    document.getElementById('amount-payable').innerText = totalPrice; // Mise à jour du montant total à payer
}
