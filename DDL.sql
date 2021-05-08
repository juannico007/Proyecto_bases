-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.3
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- ddl-end --


-- object: public.delito | type: TABLE --
-- DROP TABLE IF EXISTS public.delito CASCADE;
CREATE TABLE public.delito (
	id_delito serial NOT NULL,
	articulo varchar(80),
	h_d_c char(2) NOT NULL,
	hecho char(2) NOT NULL,
	anio_hecho integer NOT NULL,
	conexo char(2) NOT NULL,
	municipio varchar(100),
	departamento varchar(100),
	delito_especifico_calsificacion_delito varchar(40),
	id_proceso_proceso integer,
	"id_grupo_Grupo_victimas" integer,
	CONSTRAINT "Delito_pk" PRIMARY KEY (id_delito)

);
-- ddl-end --
ALTER TABLE public.delito OWNER TO postgres;
-- ddl-end --

-- object: public."Grupo_victimas" | type: TABLE --
-- DROP TABLE IF EXISTS public."Grupo_victimas" CASCADE;
CREATE TABLE public.Grupo_victimas (
	id_grupo serial NOT NULL,
	numero_victimas integer NOT NULL,
	edad varchar(40),
	genero varchar(10),
	pais_de_nacimiento varchar(80),
	CONSTRAINT "Grupo_victimas_pk" PRIMARY KEY (id_grupo)

);
-- ddl-end --
ALTER TABLE public.Grupo_victimas OWNER TO postgres;
-- ddl-end --

-- object: public.resultado | type: TABLE --
-- DROP TABLE IF EXISTS public.resultado CASCADE;
CREATE TABLE public.resultado (
	id_resultado serial NOT NULL,
	condena char(2) NOT NULL,
	captura char(2) NOT NULL,
	a_o_i char(2) NOT NULL,
	ruptura char(2) NOT NULL,
	CONSTRAINT sentencia_pk PRIMARY KEY (id_resultado)

);
-- ddl-end --
ALTER TABLE public.resultado OWNER TO postgres;
-- ddl-end --

-- object: public.proceso | type: TABLE --
-- DROP TABLE IF EXISTS public.proceso CASCADE;
CREATE TABLE public.proceso (
	id_proceso serial NOT NULL,
	estado_actividad varchar(40) NOT NULL,
	etapa varchar(40) NOT NULL,
	seccion varchar(60),
	imputacion char(2) NOT NULL,
	acusacion char(2) NOT NULL,
	anio_entrada integer NOT NULL,
	anio_denuncia integer NOT NULL,
	id_resultado_resultado integer,
	CONSTRAINT proceso_pk PRIMARY KEY (id_proceso)

);
-- ddl-end --
ALTER TABLE public.proceso OWNER TO postgres;
-- ddl-end --

-- object: public.calsificacion_delito | type: TABLE --
-- DROP TABLE IF EXISTS public.calsificacion_delito CASCADE;
CREATE TABLE public.calsificacion_delito (
	delito_especifico varchar(80) NOT NULL,
	grupo varchar(80) NOT NULL,
	CONSTRAINT calsificacion_delito_pk PRIMARY KEY (delito_especifico)

);
-- ddl-end --
ALTER TABLE public.calsificacion_delito OWNER TO postgres;
-- ddl-end --

-- object: calsificacion_delito_fk | type: CONSTRAINT --
-- ALTER TABLE public.delito DROP CONSTRAINT IF EXISTS calsificacion_delito_fk CASCADE;
ALTER TABLE public.delito ADD CONSTRAINT calsificacion_delito_fk FOREIGN KEY (delito_especifico_calsificacion_delito)
REFERENCES public.calsificacion_delito (delito_especifico) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: resultado_fk | type: CONSTRAINT --
-- ALTER TABLE public.proceso DROP CONSTRAINT IF EXISTS resultado_fk CASCADE;
ALTER TABLE public.proceso ADD CONSTRAINT resultado_fk FOREIGN KEY (id_resultado_resultado)
REFERENCES public.resultado (id_resultado) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: proceso_fk | type: CONSTRAINT --
-- ALTER TABLE public.delito DROP CONSTRAINT IF EXISTS proceso_fk CASCADE;
ALTER TABLE public.delito ADD CONSTRAINT proceso_fk FOREIGN KEY (id_proceso_proceso)
REFERENCES public.proceso (id_proceso) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: "Grupo_victimas_fk" | type: CONSTRAINT --
-- ALTER TABLE public.delito DROP CONSTRAINT IF EXISTS "Grupo_victimas_fk" CASCADE;
ALTER TABLE public.delito ADD CONSTRAINT Grupo_victimas_fk FOREIGN KEY ("id_grupo_Grupo_victimas")
REFERENCES public.Grupo_victimas (id_grupo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

