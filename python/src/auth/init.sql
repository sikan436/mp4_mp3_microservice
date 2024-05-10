create user 'auth_user'@'localhost' identified by 'Aauth123';
create database auth;
grant all privileges on auth.* to 'auth_user'@'localhost';
use auth;

create table user( id INT not null auto_increment PRIMARY KEY,
    email Varchar(255) not null unique,
    password Varchar(255) not null
);
insert into user(email,password) values('sik@gmail.com','1234')