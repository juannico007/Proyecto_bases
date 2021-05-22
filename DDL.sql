-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- object: instructor | type: ROLE --
-- DROP ROLE IF EXISTS instructor;
CREATE ROLE instructor WITH 
	INHERIT
	LOGIN
	ENCRYPTED PASSWORD '********';
-- ddl-end --

-- object: estudiante | type: ROLE --
-- DROP ROLE IF EXISTS estudiante;
CREATE ROLE estudiante WITH 
	INHERIT
	LOGIN
	ENCRYPTED PASSWORD '********';
-- ddl-end --

-- object: coordinador | type: ROLE --
-- DROP ROLE IF EXISTS coordinador;
CREATE ROLE coordinador WITH 
	INHERIT
	LOGIN
	ENCRYPTED PASSWORD '********';
-- ddl-end --


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: conteo_victimas | type: DATABASE --
-- -- DROP DATABASE IF EXISTS conteo_victimas;
-- CREATE DATABASE conteo_victimas
-- 	ENCODING = 'UTF8'
-- 	LC_COLLATE = 'Spanish_Colombia.1252'
-- 	LC_CTYPE = 'Spanish_Colombia.1252'
-- 	TABLESPACE = pg_default
-- 	OWNER = postgres;
-- -- ddl-end --
-- 

-- object: public.delito_id_delito_seq | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public.delito_id_delito_seq CASCADE;
CREATE SEQUENCE public.delito_id_delito_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public.delito_id_delito_seq OWNER TO postgres;
-- ddl-end --

-- object: public.delito | type: TABLE --
-- DROP TABLE IF EXISTS public.delito CASCADE;
CREATE TABLE public.delito (
	id_delito integer NOT NULL DEFAULT nextval('public.delito_id_delito_seq'::regclass),
	articulo character varying(200),
	h_d_c character(2) NOT NULL,
	hecho character(2) NOT NULL,
	anio_hecho integer NOT NULL,
	conexo character(2) NOT NULL,
	municipio character varying(100),
	departamento character varying(100),
	delito_especifico_calsificacion_delito character varying(150),
	id_proceso_proceso integer,
	"id_grupo_Grupo_victimas" integer,
	CONSTRAINT "Delito_pk" PRIMARY KEY (id_delito)

);
-- ddl-end --
-- ALTER TABLE public.delito OWNER TO postgres;
-- ddl-end --

-- object: public.grupo_victimas_id_grupo_seq | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public.grupo_victimas_id_grupo_seq CASCADE;
CREATE SEQUENCE public.grupo_victimas_id_grupo_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public.grupo_victimas_id_grupo_seq OWNER TO postgres;
-- ddl-end --

-- object: public.grupo_victimas | type: TABLE --
-- DROP TABLE IF EXISTS public.grupo_victimas CASCADE;
CREATE TABLE public.grupo_victimas (
	id_grupo integer NOT NULL DEFAULT nextval('public.grupo_victimas_id_grupo_seq'::regclass),
	numero_victimas integer NOT NULL,
	edad character varying(40),
	genero character varying(10),
	pais_de_nacimiento character varying(80),
	CONSTRAINT "Grupo_victimas_pk" PRIMARY KEY (id_grupo)

);
-- ddl-end --
-- ALTER TABLE public.grupo_victimas OWNER TO postgres;
-- ddl-end --

-- object: public.resultado_id_resultado_seq | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public.resultado_id_resultado_seq CASCADE;
CREATE SEQUENCE public.resultado_id_resultado_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public.resultado_id_resultado_seq OWNER TO postgres;
-- ddl-end --

-- object: public.resultado | type: TABLE --
-- DROP TABLE IF EXISTS public.resultado CASCADE;
CREATE TABLE public.resultado (
	id_resultado integer NOT NULL DEFAULT nextval('public.resultado_id_resultado_seq'::regclass),
	condena character(2) NOT NULL,
	captura character(2) NOT NULL,
	a_o_i character(2) NOT NULL,
	ruptura character(2) NOT NULL,
	CONSTRAINT sentencia_pk PRIMARY KEY (id_resultado)

);
-- ddl-end --
-- ALTER TABLE public.resultado OWNER TO postgres;
-- ddl-end --

-- object: public.proceso_id_proceso_seq | type: SEQUENCE --
-- DROP SEQUENCE IF EXISTS public.proceso_id_proceso_seq CASCADE;
CREATE SEQUENCE public.proceso_id_proceso_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START WITH 1
	CACHE 1
	NO CYCLE
	OWNED BY NONE;
-- ddl-end --
-- ALTER SEQUENCE public.proceso_id_proceso_seq OWNER TO postgres;
-- ddl-end --

-- object: public.proceso | type: TABLE --
-- DROP TABLE IF EXISTS public.proceso CASCADE;
CREATE TABLE public.proceso (
	id_proceso integer NOT NULL DEFAULT nextval('public.proceso_id_proceso_seq'::regclass),
	estado_actividad character varying(40),
	etapa character varying(40),
	seccion character varying(100),
	imputacion character(2) NOT NULL,
	acusacion character(2) NOT NULL,
	anio_entrada character(6) NOT NULL,
	anio_denuncia character(6) NOT NULL,
	id_resultado_resultado integer,
	CONSTRAINT proceso_pk PRIMARY KEY (id_proceso)

);
-- ddl-end --
-- ALTER TABLE public.proceso OWNER TO postgres;
-- ddl-end --

-- object: public.calsificacion_delito | type: TABLE --
-- DROP TABLE IF EXISTS public.calsificacion_delito CASCADE;
CREATE TABLE public.calsificacion_delito (
	delito_especifico character varying(150) NOT NULL,
	grupo character varying(80),
	CONSTRAINT calsificacion_delito_pk PRIMARY KEY (delito_especifico)

);
-- ddl-end --
-- ALTER TABLE public.calsificacion_delito OWNER TO postgres;
-- ddl-end --

-- object: proceso_fk | type: CONSTRAINT --
-- ALTER TABLE public.delito DROP CONSTRAINT IF EXISTS proceso_fk CASCADE;
ALTER TABLE public.delito ADD CONSTRAINT proceso_fk FOREIGN KEY (id_proceso_proceso)
REFERENCES public.proceso (id_proceso) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: grupo_victimas_fk | type: CONSTRAINT --
-- ALTER TABLE public.delito DROP CONSTRAINT IF EXISTS grupo_victimas_fk CASCADE;
ALTER TABLE public.delito ADD CONSTRAINT grupo_victimas_fk FOREIGN KEY ("id_grupo_Grupo_victimas")
REFERENCES public.grupo_victimas (id_grupo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
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


