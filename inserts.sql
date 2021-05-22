-- Grupo victimas

copy Grupo_victimas(numero_victimas, edad,genero, pais_de_nacimiento)
    from 'C:\CSVsql\Proyecto\Grupo_victimas1.csv'
    with delimiter ',' csv header;
	
copy Grupo_victimas(numero_victimas, edad,genero, pais_de_nacimiento)
    from 'C:\CSVsql\Proyecto\Grupo_victimas2.csv'
    with delimiter ';' csv header;
	
copy Grupo_victimas(numero_victimas, edad,genero, pais_de_nacimiento)
    from 'C:\CSVsql\Proyecto\Grupo_victimas3.csv'
    with delimiter ';' csv header;
	
-- Resultado

copy resultado(condena, captura, a_o_i, ruptura)
	from 'C:\CSVsql\Proyecto\Resultado.csv'
	with delimiter ',' csv header;

-- procesos
copy proceso(estado_actividad,etapa,seccion,imputacion,acusacion,anio_entrada,anio_denuncia,id_resultado_resultado)
	from 'C:\CSVsql\Proyecto\Proceso1.csv'
	with delimiter ';' csv header;
	
copy proceso(estado_actividad,etapa,seccion,imputacion,acusacion,anio_entrada,anio_denuncia,id_resultado_resultado)
	from 'C:\CSVsql\Proyecto\Proceso2.csv'
	with delimiter ';' csv header;
	
copy proceso(estado_actividad,etapa,seccion,imputacion,acusacion,anio_entrada,anio_denuncia,id_resultado_resultado)
	from 'C:\CSVsql\Proyecto\Proceso3.csv'
	with delimiter ';' csv header;
	
-- clasificacion delito
copy calsificacion_delito(delito_especifico, grupo)
	from 'C:\CSVsql\Proyecto\clasificacion_delito.csv'
	with delimiter ';' csv header;
	
-- DELITO
copy delito(h_d_c,hecho,anio_hecho,conexo,municipio,departamento,id_proceso_proceso,"id_grupo_Grupo_victimas",delito_especifico_calsificacion_delito,articulo)
    from 'C:\CSVsql\Proyecto\Delito1.csv'
    with delimiter ';' csv header;
	
copy delito(h_d_c,hecho,anio_hecho,conexo,municipio,departamento,id_proceso_proceso,"id_grupo_Grupo_victimas",delito_especifico_calsificacion_delito,articulo)
    from 'C:\CSVsql\Proyecto\Delito2.csv'
    with delimiter ';' csv header;

copy delito(h_d_c,hecho,anio_hecho,conexo,municipio,departamento,id_proceso_proceso,"id_grupo_Grupo_victimas",delito_especifico_calsificacion_delito,articulo)
    from 'C:\CSVsql\Proyecto\Delito3.csv'
    with delimiter ';' csv header;
	
	
