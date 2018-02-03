SELECT customers.name 'Customers'
FROM customers
WHERE customers.id not in
(SELECT customerid FROM orders);
