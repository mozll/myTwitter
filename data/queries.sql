SELECT * FROM customers;
SELECT * FROM customers ORDER BY Companyname ASC;
SELECT * FROM customers ORDER BY Companyname DESC;

SELECT * FROM Products;
-- CI = case insensitive

-- Aggregate functions
-- Select the most expensive product
SELECT MAX(UnitPrice) from Products;
--ALIAS
SELECT MAX(UnitPrice) as most_expensive_product from Products;

-- Select the cheapest product
SELECT MIN(UnitPrice) from Products;
SELECT MIN(UnitPrice) as least_expensive_product from Products;

-- Select the average product price
SELECT AVG(UnitPrice) from Products;
SELECT AVG(UnitPrice) AS average_product_price from Products;

-- Give me the total number of products in the table
SELECT COUNT(*) FROM products;
--ALIAS
SELECT COUNT(*) AS total_products FROM products;

-- Pagination
SELECT * FROM Products LIMIT 0,5;
-- Get 5 products, ordered by cheapest to highest
SELECT * FROM Products order by UnitPrice ASC LIMIT 0,5;


-- LIKE with wildcard
SELECT * FROM Customers WHERE ContactName LIKE "Ma%";
SELECT * FROM Customers WHERE ContactName LIKE "%R";
SELECT * FROM Customers WHERE ContactName LIKE "%wa%";


-- JOIN
SELECT * FROM Customers;
SELECT * FROM Orders
SELECT * FROM Products;


SELECT * FROM Orders 
JOIN Customers 
ON Orders.CustomerID = customers.CustomerID
WHERE customers.CustomerID = "VINET" LIMIT 0,2;


