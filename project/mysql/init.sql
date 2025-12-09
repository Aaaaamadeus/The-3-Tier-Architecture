create database  if not exists testdb;
use testdb;
create table if not exists access_log(
       id int auto_increment primary key,
       access_time timestamp default current_timestamp,
       container_id varchar(255)
);
