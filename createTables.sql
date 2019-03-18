/*admin table */
CREATE TABLE [Admins](
	[id] [nvarchar](50) PRIMARY KEY,
	[password] [nvarchar](50) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
)
/*user table */
CREATE TABLE [User](
	[uid] [nvarchar](50) PRIMARY KEY,
	[password] [nvarchar](50),
	[firstName] [nvarchar](50),
	[lastName] [nvarchar](50),
	[mid] [nvarchar](50),
	[age] [int],
	[gender] [nchar](10),
	[birthday] [date],
	[phone] [int],
	[address] [nvarchar](100),
	[contact1] [int],
	[contact2] [int],
	[medical] [nvarchar](150),
	[diet] [nvarchar](150),
)
/*mentor table */
CREATE TABLE [Mentor](
	[mid] [nvarchar](50) PRIMARY KEY,
	[password] [nvarchar](50) NOT NULL,
	[firstName] [nvarchar](50) NOT NULL,
	[lastName] [nvarchar](50) NOT NULL,
	[phone] [int],
)
/*images table */
CREATE TABLE [Images](
	[imagesID] [int],
	[name] [nvarchar](50),
	[role] [nvarchar](50),
	[link] [nvarchar](150),
	[uid] [nvarchar](50),
	[mid] [nvarchar](50),
)
/*patients table */
CREATE TABLE [Patients](
	[mid] [nvarchar](50),
	[uid] [nvarchar](50),
)
/*titles table */
CREATE TABLE [Titles](
	[titleID] [int],
	[action] [nvarchar](150),
	[uid] [nvarchar](50),
	[mid] [nvarchar](50),
)