alter table Grupo_victimas alter column pais_de_nacimiento type varchar(60);
DELETE FROM Grupo_victimas

select count(*) from Grupo_victimas
INSERT INTO public.grupo_victimas(
	numero_victimas)
	VALUES (2);

ALTER SEQUENCE grupo_victimas_id_grupo_seq RESTART WITH 1;
UPDATE grupo_victimas SET id_grupo=nextval('grupo_victimas_id_grupo_seq');
	
	
alter table Ubicacion alter column departamento type varchar(80);
alter table Ubicacion alter column municipio type varchar(50);
DELETE FROM Ubicacion

alter table proceso alter column seccion type varchar(100);
alter table proceso alter column anio_entrada type char(6);
alter table proceso alter column anio_denuncia type char(6);
alter table proceso alter column etapa type varchar(100);
DELETE FROM proceso;

select count(*) from proceso

ALTER SEQUENCE proceso_id_proceso_seq RESTART WITH 1;
UPDATE proceso SET id_proceso=nextval('proceso_id_proceso_seq');

DELETE FROM calsificacion_delito;
alter table calsificacion_delito alter column delito_especifico type varchar(150);

alter table delito alter column delito_especifico_calsificacion_delito type varchar(150);
alter table delito alter column articulo type varchar(200);

ALTER SEQUENCE delito_id_delito_seq RESTART WITH 1;
UPDATE delito SET id_delito=nextval('delito_id_delito_seq');

DELETE FROM delito;
