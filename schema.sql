drop table if exists users;
drop table if exists clients;
drop table if exists projects;
drop table if exists strainerBars;
drop table if exists panels;
drop table if exists pedestals;
drop table if exists customProjects;
create table users (
  userID integer primary key autoincrement,
  username text not null,
  password text not null
);
create table clients (
  clientID integer primary key autoincrement,
  first_name text not null,
  last_name text not null,
  email text not null,
  phone text not null
);
create table projects (
  projectID integer primary key autoincrement,
  clientID integer not null,
  create_date text not null,
  due_date text not null,
  completion_date text,
  project_title text not null,
  status integer not null,
  deposit integer default 0,
  discount integer default 0,
);
create table strainerBars (
  id integer primary key autoincrement,
  projectID integer not null,
  width real not null,
  height real not null,
  thickness real not null,
  price integer not null,
  notes text
);
create table panels (
  id integer primary key autoincrement,
  projectID integer not null,
  width real not null,
  height real not null,
  thickness real not null,
  price integer not null,
  notes text
);
create table pedestals (
  id integer primary key autoincrement,
  projectID integer not null,
  width real not null,
  height real not null,
  thickness real not null,
  float real not null,
  price integer not null,
  notes text
);
create table customProjects (
  id integer primary key autoincrement,
  price real not null,
  notes text not null
);
INSERT INTO users (username, password)
       VALUES ('admin', 'password');
