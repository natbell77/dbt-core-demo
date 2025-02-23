SELECT CustomerID
    , FirstName
    , LastName
    , Email
    , Phone
    , Address
    , City
    , State
    , ZipCode
    , Updated_at
    , CONCAT(FirstName, ' ', LastName) CustomerName
FROM 
    customers