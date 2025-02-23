SELECT
    O.OrderId
    , O.OrderDate
    , O.CustomerId
    , O.EmployeeId
    , O.StoreId
    , O.StatusCD
    , O.Status_Desc
    , O.Updated_at
    , COUNT(DISTINCT O.OrderId) AS OrderCount
    , SUM(OI.TotalPrice) AS Revenue
FROM
    {{ref('orders_stg')}} O
JOIN
    {{ref('orderitems_stg')}} OI ON OI.OrderId = O.OrderId
GROUP BY 
    O.OrderId
    , O.OrderDate
    , O.CustomerId
    , O.EmployeeId
    , O.StoreId
    , O.StatusCD
    , O.Status_Desc
    , O.Updated_at