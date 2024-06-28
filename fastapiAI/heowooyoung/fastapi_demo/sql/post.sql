create table if not exists post (
    id int auto_increment primary key,
    title varchar(255) not null,
    content text not null
);
