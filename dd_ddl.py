import duckdb

con = duckdb.connect('dev.duckdb')

#Dates
con.execute('''
    CREATE TABLE IF NOT EXISTS Dates (
    Date DATE NOT NULL,
    Day VARCHAR(3) NULL,
    Month VARCHAR(10) NULL,
    Year VARCHAR(4) NULL,
    Quarter INT NULL,
    DayOfWeek VARCHAR(10) NULL,
    WeekOfYear INT NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (Date));
''')

#customers
con.execute('''
    CREATE TABLE IF NOT EXISTS customers (
    CustomerID VARCHAR(10),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(100),
    Address VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(2),
    ZipCode VARCHAR(10),
    Updated_at TIMESTAMP);
''')

#Employees
con.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT NOT NULL,
    FirstName VARCHAR(100) NULL,
    LastName VARCHAR(100) NULL,
    Email VARCHAR(200) NULL,
    JobTitle VARCHAR(100) NULL,
    HireDate DATE NULL,
    ManagerID INT NULL,
    Address VARCHAR(200) NULL,
    City VARCHAR(50) NULL,
    State VARCHAR(50) NULL,
    ZipCode VARCHAR(10) NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (EmployeeID));
''')

#Stores
con.execute('''
    CREATE TABLE IF NOT EXISTS Stores (
    StoreID INT NOT NULL,
    StoreName VARCHAR(100) NULL,
    Address VARCHAR(200) NULL,
    City VARCHAR(50) NULL,
    State VARCHAR(50) NULL,
    ZipCode VARCHAR(10) NULL,
    Email VARCHAR(200) NULL,
    Phone VARCHAR(50) NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (StoreID));
''')

#Suppliers
con.execute('''
    CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID INT NOT NULL,
    SupplierName VARCHAR(100) NULL,
    ContactPerson VARCHAR(100) NULL,
    Email VARCHAR(200) NULL,
    Phone VARCHAR(50) NULL,
    Address VARCHAR(50) NULL,
    City VARCHAR(50) NULL,
    State VARCHAR(10) NULL,
    ZipCode VARCHAR(10) NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (SupplierID));
''')

#Products
con.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    ProductID INT NOT NULL,
    Name VARCHAR(100) NULL,
    Category VARCHAR(100) NULL,
    RetailPrice DECIMAL(10,2) NULL,
    SupplierPrice DECIMAL(10,2) NULL,
    SupplierID INT NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (ProductID));
''')

#OrderItems
con.execute('''
    CREATE TABLE IF NOT EXISTS OrderItems (
    OrderItemID INT NOT NULL,
    OrderID INT NULL,
    ProductID INT NULL,
    Quantity INT NULL,
    UnitPrice DECIMAL(10,2) NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (OrderItemID));
''')

#orders
con.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT NOT NULL,
    OrderDate DATE NULL,
    CustomerID VARCHAR(10) NULL,
    EmployeeID INT NULL,
    StoreID INT NULL,
    Status VARCHAR(10) NULL,
    Updated_at TIMESTAMP NULL,
    PRIMARY KEY (OrderID));
''')