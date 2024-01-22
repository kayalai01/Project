show databases;
use ai_kayalmahe;
show tables;
create table  Railway_Timing
(Train_No int  not null primary key,
Train_Name varchar(60) not null,
From_place varchar(50) not null,
Destination_place varchar(50) not null,
Fair int not null);

delimiter $$
drop procedure if exists insertH;$$
create procedure insertH(
in Train_Noparam int,
in Train_Nameparam varchar(60),
in From_placeparam varchar(50),
in Destination_placepram varchar(50),
in Fairparam int
)
begin 
insert into Railway_Timing(Train_no,Train_Name,From_place,Destination_place,Fair)
values (Train_Noparam,Train_Nameparam,From_placeparam,Destination_placepram,Fairparam);
end$$
delimiter ;

call insertH(123987,'Guruvaiur Express','kerala','chennai',2200);
select * from Railway_Timing;

delimiter $$

drop procedure if exists insertJ;$$
create procedure insertJ
(
in tablename varchar(60),
in columnname1 varchar(30),
in columnvalue1 int,
in columnname2 varchar(30),
in columnvalue2 varchar(60),
in columnname3 varchar(30),
in columnvalue3 varchar(60),
in columnname4 varchar(30),
in columnvalue4 varchar(60),
in condname varchar(30),
in condvalue int
)
begin
set @ticket=concat(' update ',tablename,' set ',columnname1, '=',columnvalue1,',',
columnname2, '=\'',columnvalue2,'\',',columnname3, '=\'',columnvalue3,'\',',
columnname4, '=\'',columnvalue4,'\'where ',condname,'=',condvalue);
prepare ddu from @ticket;
execute ddu ;

end $$
delimiter ;


call insertJ ('Railway_Timing','Fair',2500,'Train_Name','Mysore Express', 
'From_place','Delhi','Destination_place','Bangalore','Train_no',12723);

select * from Railway_Timing;

delimiter $$

drop procedure if exists insertk;$$
create procedure insertk
(
in tablename varchar(60),
in columnname1 varchar(30)
)
begin
set @checker=concat('alter table ', tablename, ' drop column ', columnname1);
prepare kkt from @checker;
execute kkt ;

end $$
delimiter ;

call insertk ( 'Railway_Timing' , 'Fair');