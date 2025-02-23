SELECT
    OrderItemId
    , OrderId
    , ProductId
    , Quantity
    , UnitPrice
    , UnitPrice * Quantity AS TotalPrice
    , Updated_at
FROM
    OrderItems