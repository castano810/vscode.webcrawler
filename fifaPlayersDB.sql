CREATE DATABASE Fifa
GO
use Fifa
GO
drop table PlayerStatsExmp
go 

--- Creates a PlayerStatsExmp Table
CREATE TABLE PlayerStatsExmp(
        PlayerType varchar(255),
        PlayerName varchar(255),
        Dribbling int,
        PlayerRating int ,
        PlayerPosition varchar(255),
        Pace int , 
        PlayerNation varchar(255), 
        Defense int, 
        Physical int , 
        Passing int ,  
        Shooting int , 
        PlayerClub varchar(255) 
)
GO


/*importing JSON file,
 declaring a varibale that will 
 hold all data in one row and column
 */
Declare @JSON varchar(max)


/*
    Path to file that holds data
    assigns to a column 'BulkColumn
*/
SELECT @JSON = BulkColumn
FROM OPENROWSET (BULK '/home/castano810/Documents/PyEnvironments/Tutorial/scp_Tut/tutorial/tutorial/spiders/players.json', SINGLE_CLOB) as j
/*
SELECT * FROM OPENJSON (@JSON) 
WITH(   
        PlayerType varchar(255) '$.PlayerType',
        PlayerName varchar(255) '$.PlayerName',
        Dribbling int '$.Dribbling',
        PlayerRating int '$.PlayerRating',
        PlayerPosition varchar(255) '$.PlayerPosition',
        Pace int '$.Pace', 
        PlayerNation varchar(255) '$.PlayerNation', 
        Defense int '$.Defense', 
        Physical int '$.Physical', 
        Passing int '$.Passing',  
        Shooting int '$.Shooting', 
        PlayerClub varchar(255) '$.PlayerClub'
        
) 
*/

/*
    Insert data into the table 
    Using Json's $ to select the name of each column that will
    be inserted into table
*/
INSERT INTO PlayerStatsExmp
SELECT PlayerType, PlayerName, Dribbling, PlayerRating, PlayerPosition, Pace, PlayerNation, Defense, Physical, Passing, Shooting, PlayerClub
FROM OPENJSON(@JSON)
WITH(   
        PlayerType varchar(255) '$.PlayerType',
        PlayerName varchar(255) '$.PlayerName',
        Dribbling int '$.Dribbling',
        PlayerRating int '$.PlayerRating',
        PlayerPosition varchar(255) '$.PlayerPosition',
        Pace int '$.Pace', 
        PlayerNation varchar(255) '$.PlayerNation', 
        Defense int '$.Defense', 
        Physical int '$.Physical', 
        Passing int '$.Passing',  
        Shooting int '$.Shooting', 
        PlayerClub varchar(255) '$.PlayerClub'
        
) 


-- Making sure it works by selecting the table
-- Where there exists a player, Lionel Messi the G.O.A.T
SELECT * FROM PlayerStatsExmp
WHERE PlayerName = 'Lionel Messi'
---