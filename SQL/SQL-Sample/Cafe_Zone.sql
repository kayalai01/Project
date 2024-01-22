use ai_kayalmahe;
show tables;
create table Cafe_Zone
(sl_no int not null primary key,
product varchar(80) not null,
qty int not null,
price int not null, 
Amt int not null);

select * from Cafe_Zone;

insert into Cafe_Zone( sl_no, product, qty, price, Amt)
values (1,'cofee',2,10,20),
(2,'samosa',2,5,10),
(3,'puffs',5,15,75),
(4,'plain cake',10,10,100);

create table Cafe_Cus_dtls
(sl_no int not null ,
Bill_no int not null primary key auto_increment,
Bill_Date date ,
cus_name varchar(50) not null,
Phone_no long not null);


insert into Cafe_Cus_dtls 
(sl_no, Bill_no, Bill_Date ,  cus_name, Phone_no)
values(1,101, 

