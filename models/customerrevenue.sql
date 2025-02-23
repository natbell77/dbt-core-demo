SELECT
    OS.CustomerId
    , C.CustomerName
    , SUM(OS.OrderCount) AS OrderCount
    , SUM(OS.Revenue) AS Revenue
FROM
    {{ref('orders_fact')}} OS
JOIN
    {{ref('customers_stg')}} C ON C.CustomerId = OS.CustomerId
GROUP BY
    OS.CustomerId
    , C.CustomerName