delete from privileges;
delete from resources;
delete from actions;
delete from controllers;
delete from users;
delete from roles;

---
--  Roles
---


insert into roles (id, name) values (1, 'administrador');
insert into roles (id, name) values (2, 'usuário');


insert into users (username, password, role_id, email) values ('admin', 'sha256$l2ygbSdF$2d03f994b4d99fdf6ca30832852826564189f3438a9f6abc7249bc74c08b7843', 1, 'nivardo00@gmail.com');

---
--  Controllers
---


insert into controllers (id, name) values (1, 'users');
insert into controllers (id, name) values (2, 'cidade');
---
--  Actions
---

insert into actions (id, name) values (1, 'all');
insert into actions (id, name) values (2, 'view');
insert into actions (id, name) values (3, 'add');
insert into actions (id, name) values (4, 'edit');
insert into actions (id, name) values (5, 'delete');


---
--Resources
---


insert into resources (id, controller_id, action_id) values (  1, 1, 1); -- users/all
insert into resources (id, controller_id, action_id) values (  2, 1, 2); -- users/view
insert into resources (id, controller_id, action_id) values (  3, 1, 3); -- users/add
insert into resources (id, controller_id, action_id) values (  4, 1, 4); -- users/edit
insert into resources (id, controller_id, action_id) values (  5, 1, 5); -- users/delete

--administrator


insert into privileges (role_id, resource_id, allow) values (1, 1, true); -- users/all
insert into privileges (role_id, resource_id, allow) values (1, 2, true); -- users/view
insert into privileges (role_id, resource_id, allow) values (1, 3, true); -- users/add
insert into privileges (role_id, resource_id, allow) values (1, 4, true); -- users/edit
insert into privileges (role_id, resource_id, allow) values (1, 5, true); -- users/delete


--user


insert into privileges (role_id, resource_id, allow) values (2, 1, true); -- users/all
insert into privileges (role_id, resource_id, allow) values (2, 2, true); -- users/view
insert into privileges (role_id, resource_id, allow) values (2, 3, false); -- users/add
insert into privileges (role_id, resource_id, allow) values (2, 4, true); -- users/edit
insert into privileges (role_id, resource_id, allow) values (2, 5, false); -- users/delete
