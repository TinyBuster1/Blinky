USE [BlinkyDB]
GO

/****** Object:  Table [dbo].[Admins]    Script Date: 25/04/2019 9:42:40 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Admins](
	[id] [nvarchar](50) NULL,
	[password] [nvarchar](50) NULL,
	[name] [nvarchar](50) NULL,
	[email] [nvarchar](50) NULL
) ON [PRIMARY]

GO


USE [BlinkyDB]
GO

/****** Object:  Table [dbo].[Images]    Script Date: 25/04/2019 9:43:10 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Images](
	[imagesID] [int] NULL,
	[name] [nvarchar](50) NULL,
	[role] [nvarchar](50) NULL,
	[link] [nvarchar](150) NULL,
	[uid] [nvarchar](50) NULL,
	[mid] [nvarchar](50) NULL
) ON [PRIMARY]

GO


USE [BlinkyDB]
GO

/****** Object:  Table [dbo].[Mentor]    Script Date: 25/04/2019 9:43:24 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Mentor](
	[mid] [nvarchar](50) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[firstName] [nvarchar](50) NOT NULL,
	[lastName] [nvarchar](50) NOT NULL,
	[phone] [int] NULL,
	[email] [nvarchar](50) NOT NULL
) ON [PRIMARY]

GO


USE [BlinkyDB]
GO

/****** Object:  Table [dbo].[Patients]    Script Date: 25/04/2019 9:43:44 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Patients](
	[mid] [nvarchar](50) NULL,
	[uid] [nvarchar](50) NULL
) ON [PRIMARY]

GO


USE [BlinkyDB]
GO

/****** Object:  Table [dbo].[Titles]    Script Date: 25/04/2019 9:43:57 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Titles](
	[titleID] [int] NULL,
	[phrase] [nvarchar](150) NULL,
	[uid] [nvarchar](50) NULL,
	[mid] [nvarchar](50) NULL,
	[role] [nvarchar](50) NULL
) ON [PRIMARY]

GO


USE [BlinkyDB]
GO

/****** Object:  Table [dbo].[User]    Script Date: 25/04/2019 9:44:07 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[User](
	[uid] [nvarchar](50) NULL,
	[password] [nvarchar](50) NULL,
	[firstName] [nvarchar](50) NULL,
	[lastName] [nvarchar](50) NULL,
	[mid] [nvarchar](50) NULL,
	[age] [int] NULL,
	[gender] [nvarchar](50) NULL,
	[birthday] [date] NULL,
	[phone] [int] NULL,
	[address] [nvarchar](50) NULL,
	[contact1] [nvarchar](50) NULL,
	[contact2] [nvarchar](50) NULL,
	[medical] [nvarchar](250) NULL,
	[diet] [nvarchar](250) NULL
) ON [PRIMARY]

GO


