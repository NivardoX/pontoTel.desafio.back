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

-- companies

INSERT INTO companies (name,symbol,peso,populated) VALUES ('VALE','VALE3','9.7',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BRADESCO','BBDC4','8.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('PETROBRAS','PETR4','6.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('B3','B3SA3','4.8',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('PETROBRAS','PETR3','4.7',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('AMBEV S/A','ABEV3','4.6',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BANCO DO BRASIL','BBAS3','4.0',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ITAUSA','ITSA4','3.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('JBS','JBSS3','2.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('LOJAS RENNER','LREN3','2.1',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ITAU UNIBANCO','ITUB4','10.0',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BRADESCO','BBDC3','1.8',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BRF S/A','BRFS3','1.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('RUMO S/A','RAIL3','1.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('SUZANO S/A','SUZB5','1.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('LOCALIZA','RENT3','1.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('TELEF BRASIL','VIVT4','1.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BB SEGURIDADE','BBSE3','1.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ULTRAPAR','UGPA3','1.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('EQUATORIAL','EQTL3','1.0',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('KROTON','KROT3','1.0',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('SANTANDER BR','SANB11','1.0',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('WEG','WEGE3','0.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('CCR S/A','CCRO3','0.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('RAIADROGASIL','RADL3','0.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('SABESP','SBSP3','0.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('MAGAZINE LUIZA','MGLU3','0.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('AZUL','AZUL4','0.9',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('EMBRAER','EMBR3','0.8',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('GERDAU','GGBR4','0.8',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('PÃO DE AÇÚCAR - CBD','PCAR4','0.8',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('CEMIG','CMIG4','0.8',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BR MALLS PAR','VRML3','0.7',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ENGIE BRASIL','ENGIE3','0.7',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('IRB BRASIL RE','IRBR3','0.7',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('LOJAS AMERICANAS','LAME4','0.6',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('HYPERA','HYPE3','0.6',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('SID NACIONAL','CSNA3','0.6',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ELETROBRAS','ELET3','0.6',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ESTACIO PART','YDUQ3','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('TIM PART S/A','TIMP3','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('KLABIN S/A','KLBN11','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('NATURA','NATU3','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BRASKEM','BRKM5','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ELETROBRAS','ELET6','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('PETROBRAS BR','BRDT3','0.5',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('COSAN','CSAN3','0.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('CIELO','CIEL3','0.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('MULTIPLAN','MULT3','0.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('BRADESPAR','BRAP4','0.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('CVC BRASIL','CVCB3','0.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('FLEURY','FLRY3','0.4',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('TAESA','TAEE11','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('B2W DIGITAL','BTOW3','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('CYRELA REALT','CYRE3','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ENERGIAS BR','ENBR3','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('MRV','MRVE3','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('QUALICORP','QUAL3','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('GOL','GOLL4','0.3',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('USIMINAS','USIM5','0.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('IGUATEMI','IGTA3','0.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('GERDAU MET','GOAU4','0.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('VIA VAREJO','VVAR3','0.2',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('MARFRIG','MRFG3','0.1',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('ECORODOVIAS','ECOR3','0.1',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('SMILES','SMLS3','0.1',false);
INSERT INTO companies (name,symbol,peso,populated) VALUES ('IBOVESPA','^BVSP','100',false);


-- user_comapny_privileges
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','1');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','2');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','3');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','4');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','5');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','6');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','7');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','8');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','9');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','10');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','11');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','12');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','13');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','14');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','15');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','16');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','17');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','18');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','19');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','20');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','21');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','22');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','23');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','24');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','25');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','26');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','27');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','28');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','29');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','30');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','31');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','32');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','33');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','34');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','35');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','36');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','37');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','38');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','39');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','40');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','41');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','42');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','43');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','44');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','45');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','46');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','47');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','48');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','49');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','50');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','51');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','52');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','53');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','54');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','55');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','56');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','57');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','58');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','59');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','60');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','61');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','62');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','63');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','64');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','65');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','66');
INSERT INTO user_company_privileges (user_id,company_id) VALUES ('1','67');


