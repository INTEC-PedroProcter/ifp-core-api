-- People

CREATE TABLE MaritalStatus (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(20) UNIQUE
);

INSERT INTO MaritalStatus(name) VALUES ('single'), ('engaged'), ('married'), ('widow');

CREATE TABLE Person (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    national_id VARCHAR(32) UNIQUE NOT NULL,
    national_id_type CHAR(1) DEFAULT 'C' NOT NULL,
    names VARCHAR(50) NOT NULL,
    last_names VARCHAR(100) NOT NULL,
    gender CHAR(1) NOT NULL,
    birthday DATE NOT NULL,
    birth_place VARCHAR(128),
    marital_status_id BIGINT NOT NULL,
    occupation VARCHAR(64),
    photo_url VARCHAR(512),
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE Person 
ADD CONSTRAINT CK_Person_Valid_National_ID_Type
CHECK (national_id_type in ('C', 'P'));

ALTER TABLE Person 
ADD CONSTRAINT FK_Person_Marital_Status 
FOREIGN KEY (marital_status_id) REFERENCES MaritalStatus(id);

ALTER TABLE Person 
ADD CONSTRAINT CK_Person_Valid_Gender
CHECK (gender in ('M', 'F', 'O'));

ALTER TABLE Person 
ADD CONSTRAINT FK_Person_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user;

CREATE INDEX IX_Person_MaritalStatus
ON Person (marital_status_id);

CREATE INDEX IX_Person_CreatedBy
ON Person (created_by_id);

-- Deceased

CREATE TABLE Deceased (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    person_id BIGINT UNIQUE NOT NULL,
    place_of_death VARCHAR(128) NOT NULL,
    date_of_death DATE NOT NULL,
    cause_of_death VARCHAR(256) NOT NULL,
    death_certificate_number VARCHAR(64) NOT NULL,
    certified_by VARCHAR(128) NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE Deceased 
ADD CONSTRAINT FK_Deceased_Person
FOREIGN KEY (person_id) REFERENCES Person(id);

ALTER TABLE Deceased 
ADD CONSTRAINT FK_Deceased_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user;

CREATE INDEX IX_Deceased_Person
ON Deceased (person_id);

CREATE INDEX IX_Deceased_CreatedBy
ON Deceased (created_by_id);

-- Staffs

CREATE TABLE Staff (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    person_id BIGINT UNIQUE NOT NULL,
    user_id INT UNIQUE NOT NULL,
    department VARCHAR(128) NOT NULL,
    job_title VARCHAR(128) NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE Staff 
ADD CONSTRAINT FK_Staff_Person
FOREIGN KEY (person_id) REFERENCES Person(id);

ALTER TABLE Staff 
ADD CONSTRAINT FK_Staff_User
FOREIGN KEY (user_id) REFERENCES auth_user(id);

ALTER TABLE Staff 
ADD CONSTRAINT FK_Staff_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE INDEX IX_Staff_Person
ON Staff (person_id);

CREATE INDEX IX_Staff_User
ON Staff (user_id);

CREATE INDEX IX_Staff_CreatedBy
ON Staff (created_by_id);

-- Person contact information

CREATE TABLE PersonAddress (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    person_id BIGINT NOT NULL,
    street VARCHAR(128) NOT NULL,
    township VARCHAR(128) NOT NULL,
    city VARCHAR(128) NOT NULL,
    province VARCHAR(128) NOT NULL,
    country_code CHAR(2) NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE PersonAddress 
ADD CONSTRAINT FK_PersonAddress_Person
FOREIGN KEY (person_id) REFERENCES Person(id);

ALTER TABLE PersonAddress 
ADD CONSTRAINT UQ_PersonAddress_Person_Full_Address
UNIQUE (person_id, street, city, province, country_code);

ALTER TABLE PersonAddress 
ADD CONSTRAINT CK_PersonAddress_Country_Code
CHECK (country_code LIKE '[A-Z][A-Z]' and country_code = UPPER(country_code));

ALTER TABLE PersonAddress
ADD CONSTRAINT CK_PersonAddress_Country_Code_ISO2
CHECK (country_code IN (
    'AF','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ',
    'BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BQ','BA','BW','BR',
    'IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX',
    'CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CW','CY','CZ','DK','DJ',
    'DM','DO','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF',
    'PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GG',
    'GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE',
    'IM','IL','IT','JM','JP','JE','JO','KZ','KE','KI','KP','KR','KW','KG','LA',
    'LV','LB','LS','LR','LY','LI','LT','LU','MO','MG','MW','MY','MV','ML','MT',
    'MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','ME','MS','MA','MZ','MM',
    'NA','NR','NP','NL','NC','NZ','NI','NE','NG','NU','NF','MK','MP','NO','OM',
    'PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO',
    'RU','RW','BL','SH','KN','LC','MF','PM','VC','WS','SM','ST','SA','SN','RS',
    'SC','SL','SG','SX','SK','SI','SB','SO','ZA','GS','SS','ES','LK','SD','SR',
    'SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN',
    'TR','TM','TC','TV','UG','UA','AE','GB','US','UM','UY','UZ','VU','VE','VN',
    'VG','VI','WF','EH','YE','ZM','ZW'
));

ALTER TABLE PersonAddress 
ADD CONSTRAINT FK_PersonAddress_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE INDEX IX_PersonAddress_Person
ON PersonAddress (person_id);

CREATE INDEX IX_PersonAddress_CreatedBy
ON PersonAddress (created_by_id);

CREATE TABLE PhoneNumberType (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(20) UNIQUE
);

INSERT INTO PhoneNumberType(name) 
VALUES ('residence'), ('office'), ('mobile'), ('other');

CREATE TABLE PersonPhoneNumber (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    person_id BIGINT NOT NULL,
    phone_number VARCHAR(128) NOT NULL,
    type_id BIGINT NOT NULL,
    is_preferred_contact BIT DEFAULT 1 NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE PersonPhoneNumber 
ADD CONSTRAINT FK_PersonPhoneNumber_Type
FOREIGN KEY (type_id) REFERENCES PhoneNumberType(id);

ALTER TABLE PersonPhoneNumber 
ADD CONSTRAINT FK_PersonPhoneNumber_Person
FOREIGN KEY (person_id) REFERENCES Person(id);

ALTER TABLE PersonPhoneNumber 
ADD CONSTRAINT UQ_PersonPhoneNumber_Person_PhoneNumber
UNIQUE (person_id, phone_number);

ALTER TABLE PersonPhoneNumber 
ADD CONSTRAINT FK_PersonPhoneNumber_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE INDEX IX_PersonPhoneNumber_Person
ON PersonPhoneNumber (person_id);

CREATE INDEX IX_PersonPhoneNumber_Type
ON PersonPhoneNumber (type_id);

CREATE INDEX IX_PersonPhoneNumber_CreatedBy
ON PersonPhoneNumber (created_by_id);

-- Products

CREATE TABLE FuneralType (
    id BIGINT PRIMARY KEY IDENTITY,
    name CHAR(9) UNIQUE,
    description VARCHAR(512),
    service_price DECIMAL(8, 2) NOT NULL
);

INSERT INTO FuneralType(name, service_price) 
VALUES ('cremation', 10), ('burial', 10);

CREATE TABLE FuneralPackage (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    type_id BIGINT NOT NULL,
    name VARCHAR(50) UNIQUE,
    description VARCHAR(512) NOT NULL,
    package_price DECIMAL(8, 2) NOT NULL,
    include_memorial BIT DEFAULT 0 NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE FuneralPackage 
ADD CONSTRAINT FK_FuneralPackage_Type
FOREIGN KEY (type_id) REFERENCES FuneralType(id);

ALTER TABLE FuneralPackage 
ADD CONSTRAINT FK_FuneralPackage_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

-- Mechandises

CREATE TABLE MerchandiseType (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(20) UNIQUE,
    description VARCHAR(512)
);

INSERT INTO MerchandiseType(name) 
VALUES ('urn'), ('casket'), ('flower arragement'), ('keepsake book');

CREATE TABLE Merchandise (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    type_id BIGINT NOT NULL,
    name VARCHAR(50) UNIQUE,
    description VARCHAR(512) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    photo_url VARCHAR(512),
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE Merchandise 
ADD CONSTRAINT FK_Merchandise_Type
FOREIGN KEY (type_id) REFERENCES MerchandiseType(id);

ALTER TABLE Merchandise 
ADD CONSTRAINT FK_Merchandise_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE TABLE FuneralPackageMerchandise (
    id BIGINT PRIMARY KEY IDENTITY,
    package_id BIGINT NOT NULL,
    merchandise_id BIGINT NOT NULL,
    quantity INT NOT NULL DEFAULT 1
);

ALTER TABLE FuneralPackageMerchandise
ADD CONSTRAINT FK_FuneralPackageMerchandise_Package
FOREIGN KEY (package_id)
REFERENCES FuneralPackage(id)
ON DELETE CASCADE;

ALTER TABLE FuneralPackageMerchandise
ADD CONSTRAINT FK_FuneralPackageMerchandise_Merchandise
FOREIGN KEY (merchandise_id)
REFERENCES Merchandise(id)
ON DELETE CASCADE;

-- Funeral

CREATE TABLE FuneralStatus (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(50) UNIQUE,
    description VARCHAR(512)
);

INSERT INTO FuneralStatus(name) 
VALUES ('draft'), ('arranged'), ('in progress'), ('completed'), ('closed'), ('cancelled');

CREATE TABLE Funeral (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    package_id BIGINT,
    client_id BIGINT NOT NULL,
    deceased_id BIGINT NOT NULL,
    status_id BIGINT NOT NULL,
    notes VARCHAR(512) NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE Funeral 
ADD CONSTRAINT FK_Funeral_Package
FOREIGN KEY (package_id) REFERENCES FuneralPackage(id);

ALTER TABLE Funeral 
ADD CONSTRAINT FK_Funeral_Client
FOREIGN KEY (client_id) REFERENCES Person(id);

ALTER TABLE Funeral 
ADD CONSTRAINT FK_Funeral_Deceased
FOREIGN KEY (deceased_id) REFERENCES Deceased(id);

ALTER TABLE Funeral
ADD CONSTRAINT CK_Funeral_Client_Deceased_Not_Equal
CHECK (client_id <> deceased_id);

ALTER TABLE Funeral 
ADD CONSTRAINT FK_Funeral_Status
FOREIGN KEY (status_id) REFERENCES FuneralStatus(id);

ALTER TABLE Funeral 
ADD CONSTRAINT FK_Funeral_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE INDEX IX_Funeral_Client
ON Funeral (client_id);

CREATE INDEX IX_Funeral_Deceased
ON Funeral (deceased_id);

CREATE INDEX IX_Funeral_Status
ON Funeral (status_id);

CREATE INDEX IX_Funeral_Package
ON Funeral (package_id);

CREATE INDEX IX_Funeral_CreatedAt
ON Funeral (created_at DESC);

CREATE TABLE FuneralStatusHistory (
    id BIGINT PRIMARY KEY IDENTITY,
    funeral_id BIGINT NOT NULL,
    past_status_id BIGINT NOT NULL,
    new_status_id BIGINT NOT NULL,
    created_at DATETIME2,
    created_by INT NOT NULL
);

ALTER TABLE FuneralStatusHistory 
ADD CONSTRAINT FK_FuneralStatusHistory_Funeral
FOREIGN KEY (funeral_id) REFERENCES Funeral(id);

ALTER TABLE FuneralStatusHistory 
ADD CONSTRAINT FK_FuneralStatusHistory_Past_Status
FOREIGN KEY (past_status_id) REFERENCES FuneralStatus(id);

ALTER TABLE FuneralStatusHistory 
ADD CONSTRAINT FK_FuneralStatusHistory_New_Status
FOREIGN KEY (new_status_id) REFERENCES FuneralStatus(id);

ALTER TABLE FuneralStatusHistory 
ADD CONSTRAINT FK_FuneralStatusHistory_Created_By
FOREIGN KEY (created_by) REFERENCES auth_user(id);

CREATE INDEX IX_FuneralStatusHistory_Funeral
ON FuneralStatusHistory (funeral_id, created_at DESC);

CREATE INDEX IX_FuneralStatusHistory_CreatedBy
ON FuneralStatusHistory (created_by);

-- Events

CREATE TABLE EventLocation (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(512) NOT NULL,
    photo_url VARCHAR(512),
    max_capacity INT DEFAULT 1 NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

CREATE TABLE EventType (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(50) UNIQUE
);

INSERT INTO EventType(name) 
VALUES ('viewing'), ('wake'), ('funeral service'), ('burial'), ('cremation'), ('memorial');

CREATE TABLE FuneralEvent (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    type_id BIGINT NOT NULL,
    funeral_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,
    start_at DATETIME2 NOT NULL,
    ends_at DATETIME2 NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE FuneralEvent 
ADD CONSTRAINT FK_FuneralEvent_Type
FOREIGN KEY (type_id) REFERENCES FuneralType(id);

ALTER TABLE FuneralEvent 
ADD CONSTRAINT FK_FuneralEvent_Funeral
FOREIGN KEY (funeral_id) REFERENCES Funeral(id);

ALTER TABLE FuneralEvent 
ADD CONSTRAINT FK_FuneralEvent_Location
FOREIGN KEY (location_id) REFERENCES EventLocation(id);

ALTER TABLE FuneralEvent 
ADD CONSTRAINT CK_FuneralEvent_Duration
CHECK (ends_at > start_at);

ALTER TABLE FuneralEvent 
ADD CONSTRAINT FK_FuneralEvent_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE INDEX IX_FuneralEvent_Funeral
ON FuneralEvent (funeral_id);

CREATE INDEX IX_FuneralEvent_Location_Start
ON FuneralEvent (location_id, start_at);

CREATE INDEX IX_FuneralEvent_TimeRange
ON FuneralEvent (start_at, ends_at);

-- Invoices

CREATE TABLE FuneralInvoice (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    funeral_id BIGINT NOT NULL,
    subtotal DECIMAL(8, 2) NOT NULL,
    discount DECIMAL(8, 2) NOT NULL,
    tax DECIMAL(8, 2) NOT NULL,
    is_closed BIT DEFAULT 0 NOT NULL,
    is_active BIT DEFAULT 1 NOT NULL,
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE FuneralInvoice 
ADD CONSTRAINT FK_FuneralInvoice_Funeral
FOREIGN KEY (funeral_id) REFERENCES Funeral(id);

ALTER TABLE FuneralInvoice
ADD CONSTRAINT CK_FuneralInvoice_Valid_Decimals
CHECK (subtotal >= 0 AND discount >= 0 AND tax >= 0);

ALTER TABLE FuneralInvoice 
ADD CONSTRAINT FK_FuneralInvoice_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

ALTER TABLE FuneralInvoice
ADD CONSTRAINT UQ_Active_FuneralInvoice
UNIQUE (funeral_id, is_active);

CREATE INDEX IX_FuneralInvoice_Funeral
ON FuneralInvoice (funeral_id);

CREATE INDEX IX_FuneralInvoice_IsClosed
ON FuneralInvoice (is_closed);

CREATE INDEX IX_FuneralInvoice_CreatedAt
ON FuneralInvoice (created_at DESC);

-- Payments

CREATE TABLE PaymentMethod (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(11) UNIQUE
);

INSERT INTO PaymentMethod(name) 
VALUES ('cash'), ('credit card'), ('debit card'), ('transfer'), ('insurance');

CREATE TABLE PaymentStatus (
    id BIGINT PRIMARY KEY IDENTITY,
    name VARCHAR(9) UNIQUE
);

INSERT INTO PaymentStatus(name) 
VALUES ('pending'), ('completed'), ('failed'), ('refunded'), ('reversed');

CREATE TABLE Payment (
    id BIGINT PRIMARY KEY IDENTITY,
    public_id VARCHAR(32) UNIQUE NOT NULL,
    invoice_id BIGINT NOT NULL,
    method_id BIGINT NOT NULL,
    status_id BIGINT NOT NULL,
    amount DECIMAL(8, 2) NOT NULL,
    notes VARCHAR(512),
    updated_at DATETIME2,
    created_at DATETIME2 NOT NULL,
    created_by_id INT NOT NULL
);

ALTER TABLE Payment 
ADD CONSTRAINT FK_Payment_Invoice
FOREIGN KEY (invoice_id) REFERENCES FuneralInvoice(id);

ALTER TABLE Payment 
ADD CONSTRAINT FK_Payment_Method
FOREIGN KEY (method_id) REFERENCES PaymentMethod(id);

ALTER TABLE Payment 
ADD CONSTRAINT FK_Payment_Status
FOREIGN KEY (status_id) REFERENCES PaymentStatus(id);

ALTER TABLE Payment 
ADD CONSTRAINT CK_Payment_Amount
CHECK (amount > 0);

ALTER TABLE Payment 
ADD CONSTRAINT FK_Payment_Created_By
FOREIGN KEY (created_by_id) REFERENCES auth_user(id);

CREATE INDEX IX_Payment_Invoice
ON Payment (invoice_id);

CREATE INDEX IX_Payment_Method
ON Payment (method_id);

CREATE INDEX IX_Payment_Status
ON Payment (status_id);

CREATE INDEX IX_Payment_CreatedAt
ON Payment (created_at DESC);

-- Soft Delete Indexes

CREATE INDEX IX_Person_Active
ON Person (id)
WHERE is_active = 1;

CREATE INDEX IX_Deceased_Active
ON Deceased (id)
WHERE is_active = 1;

CREATE INDEX IX_Staff_Active
ON Staff (id)
WHERE is_active = 1;

CREATE INDEX IX_PersonAddress_Active
ON PersonAddress (id)
WHERE is_active = 1;

CREATE INDEX IX_PersonPhoneNumber_Active
ON PersonPhoneNumber (id)
WHERE is_active = 1;

CREATE INDEX IX_FuneralPackage_Active
ON FuneralPackage (id)
WHERE is_active = 1;

CREATE INDEX IX_Merchandise_Active
ON Merchandise (id)
WHERE is_active = 1;

CREATE INDEX IX_EventLocation_Active
ON EventLocation (id)
WHERE is_active = 1;