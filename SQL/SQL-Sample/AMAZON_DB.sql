use ai_kayalmahe;
create table Amazon_DB
(Reg_id int not null ,Cus_id int not null primary key,Usr_id varchar(30) not null,Pss_wrd varchar(20) not null,
email_id varchar(40) not null,Ph_no long not null, Teams_id varchar(40) not null);

show tables;

select * from Amazon_DB;
insert into  Amazon_DB
(Reg_id ,Cus_id,Usr_id,Pss_wrd,email_id,Ph_no,Teams_id) values
(101,8821,'Ajay_Mothra','Ajmt@mx','ajay007@hot.mail',6485347912,'Art_Ajay');

insert into  Amazon_DB
(Reg_id ,Cus_id,Usr_id,Pss_wrd,email_id,Ph_no,Teams_id) values
(102,8822,'Anjali','Anjali@sd','anjali87@hotmail.com',6486178912,'At_Anjali');
(103,8823,'Barathi_iyer','Barathi@iy','ajay007@hotmail.com',6485347912,'');
(104,8824,'Charumathi','Charu@kwng','charu13@gmail.com',6485347912,'Art_Ajay');
(105,8825,'Fathima_Begam','Fathima@Bg','Fathima68@gmail.com',6485347912,'Art_Ajay');
(106,8826,'Suresh','Suresh@jiki','suresh488@hotmail.com',6485347912,'Art_Ajay');
(107,8827,'Uthra','Uthra@ui','uthraui5@gmail.com',6485347912,'Art_Ajay');