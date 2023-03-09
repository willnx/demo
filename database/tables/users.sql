create table users (
    id UUID primary key,
    name text not null,
    password text not null -- Just a demo app; don't do this for real
);
