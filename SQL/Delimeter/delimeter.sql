show databases;
create database ai_kayal;
use ai_kayal;
 
create table Biometric_punch
(Id_no int not null primary key,
User_Name varchar(50) not null,
Bio_id int not null unique,
Shft_Schd int not null,
In_tym datetime,
Out_tym datetime);

insert into  Biometric_punch values
(01,'kayal M',4815,1,'2023-12-12 08:10:00','2023-12-12 02:10:00');
show tables;
select * from Biometric_punch;

truncate Biometric_punch;

delimiter $$
drop procedure if exists make_k;$$
create procedure  make_k(
 in Id_noparam int ,
 in User_Nameparam varchar(50),
 in Bio_idparam int ,
 in Shft_Schdparam int,
 in In_tymparam datetime,
 in Out_tymparam datetime
 )
 begin 
 insert into  Biometric_punch (Id_no,User_Name,Bio_id ,Shft_Schd,In_tym ,Out_tym ) 
 values
(Id_noparam ,
User_Nameparam ,
Bio_idparam ,
Shft_Schdparam ,
In_tymparam ,
Out_tymparam
);
end $$
delimiter ;

call make_k(01,'kayal M',4815,2,'2023-12-12 08:10:00','2023-12-12 02:10:00');




 