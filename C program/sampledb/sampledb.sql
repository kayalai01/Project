show databases;
create database ai_kayalmahe;
use ai_kayalmahe;
create table  KM_Emplyoee_Application_Table (APP_no int not null primary key,
APP_Date  int	, Name varchar (25) not null, 
 Ph_no int not null , Addhar_No  varchar(16) not null  , 
DOB int not null ,Qualification varchar(25) not null, 
Desgination varchar (30) not null, Address varchar(280) not null ,District varchar (18) not null);
show tables;


select * from  KM_Emplyoee_Application_Table;
insert into KM_Emplyoee_Application_Table(App_no,App_Date,Name,Ph_no,Addhar_No,DOB,
Qualification,Desgination, Address ,District)values(101,'0000-00-00','Kayal M','6204 4815 3395','0000-00-00''BE',
'Developer','Door number:2/125A,koothur','Trichy');

alter table KM_Emplyoee_Application_Table modify column Ph_no long not null;

alter table KM_Emplyoee_Application_Table drop column App_Date;

alter table KM_Emplyoee_Application_Table drop column DOB;



alter table KM_Emplyoee_Application_Table add  APP_Date date;

alter table KM_Emplyoee_Application_Table add DOB date;

update KM_Emplyoee_Application_Table set App_Date='2023-12-12' where Name = 'Kayal M';

select * from  KM_Emplyoee_Application_Table;

update KM_Emplyoee_Application_Table set DOB ='1999-12-12' where Name = 'Kayal M';

update KM_Emplyoee_Application_Table set Ph_no ='7339221973' where Name = 'Kayal M';

insert into KM_Emplyoee_Application_Table(App_no,Name,Ph_no,Addhar_No,
Qualification,Desgination, Address ,District,App_Date,DOB)values(102,'Sangari S','6322323221', '6584 6915 3255','BE',
'Developer','Budhallur','Tanjore','2023-12-11','1999-01-21');

describe KM_Emplyoee_Application_Table ;

insert into KM_Emplyoee_Application_Table(App_no,Name,Ph_no,Addhar_No,
Qualification,Desgination, Address ,District,App_Date,DOB)values(104,'Priya S','6523523551', '6265 6855 3255','B.Sc',
'Developer','Woraiur','Trichy','2023-12-11','2001-05-04'),(105,'Lavanya P','6533523221', '6265 6915 8555','B.Sc',
'Developer','BKS Apartment','Trichy','2023-12-11','2000-09-13'),(106,'Saranya B','9556523221', '6265 2256 3255','MCA',
'Developer','Kauvery','Trichy','2023-12-11','1998-05-06'),(107,'Malar M','9559523221', '6265 6915 8225','BE',
'Developer','Tolgate','Trichy','2023-12-11','2002-08-15');

update KM_Emplyoee_Application_Table set Qualification =
case APP_no
when 101 then 'MSc'
when 103 then 'BE'
when 105 then 'MCA'
end,

 District=
case APP_no
when 101 then 'Chennai'
when 103 then 'Banglore'
when 105 then 'Madurai'
end
where APP_no in (101,103,105);

alter table KM_Emplyoee_Application_Table
Add column email_id varchar (18) first Ph_no;

alter table KM_Emplyoee_Application_Table
Add column Age varchar (18) after App_Date ;

alter table KM_Emplyoee_Application_Table
modify column email_id varchar (50) first;

update KM_Emplyoee_Application_Table set 
email_id =

case App_no
  when 101 then 'kayalKM@gmail.com'
  when 102 then 'sangariKM@gmail.com'
  when 103 then 'jayaKM@gmail.com'
  when 104 then 'priyaKM@gmail.com'
  when 105 then 'lavanyaKM@gmail.com'
  when 106 then 'saranyaKM@gmail.com'
  end,
 
  Age=
  case App_no
  when 101 then 24
  when 102 then 24
  when 103 then 24
  when 104 then 22
  when 105 then 23
  when 106 then 25
  end
  where App_no in (101,102,103,104,105,106);
  
  delete from KM_Emplyoee_Application_Table
  where App_no=107;
  
  Rename table KM_Emplyoee_Application_Table to KM_official;
  
  select *from KM_official;
  
  create table KM_status
  (Long_in int not null primary key ,
  user_name varchar (30) not null unique,
  password varchar (20) not null,
  App_no int not null,
  New_password varchar(20),
  foreign key (App_no) references KM_official (App_no) 
  );
   
 insert into  km_status values
  (1,'TLkayal','KMkayal',101,'MKkayal'),
  (2,'GNCsangari','KMsangari',102,'MKsangari'),
  (3,'TLjaya','KMjaya',103,'MKjaya'),
  (4,'GNCpriya','KMpriya',104,'MKpriya'),
  (5,'TLlavanya','KMlavanya',105,'MKlavanya'),
  (6,'GNCsaranya','KMsaranya',106,'MKsaranya');
select * from KM_official;
select * from KM_status;
select * from KM_status join KM_official on KM_status . App_no =KM_official.App_no ;

alter table km_official
drop column Address;

