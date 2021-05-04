copy Grupo_victimas
	from 'C:\Bases_de_Datos\region.csv'
	with delimiter ';' csv header;

copy calsificacion_delito
	from 'C:\Bases_de_Datos\region.csv'
	with delimiter ';' csv header;

copy delito 
	from 'C:\Bases_de_Datos\region.csv'
	with delimiter ';' csv header;

copy proceso
	from 'C:\Bases_de_Datos\region.csv'
	with delimiter ';' csv header;

copy resultado
	from 'C:\Bases_de_Datos\region.csv'
	with delimiter ';' csv header;

copy ubicacion
	from 'C:\Bases_de_Datos\region.csv'
	with delimiter ';' csv header;