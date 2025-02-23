SELECT 
    OrderId
    , OrderDate
    , CustomerId
    , EmployeeId
    , StoreId
    , Status AS StatusCD
    , CASE 
        WHEN Status = '01' THEN 'In Progress'
        WHEN Status = '02' THEN 'Completed'
        WHEN Status = '03' THEN 'Cancelled'
        ELSE NULL
    END Status_Desc
    , Updated_at
FROM
    orders