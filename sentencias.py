def grupo_victimas():
    return """ select * from Grupo_victimas """

def clasificacion_delito():
    return """ select * from clasificacion_delito """

def delito():
    return """ select * from delito """

def proceso():
    return """ select * from proceso """

def resultado():
    return """ select * from resultado """

def analisis1():
    return """ select departamento, count(departamento) as numero_casos
               from delito
               group by departamento
               order by numero_casos desc"""


def analisis2():
    return """ select cd.grupo, count(cd.grupo) as numero_casos
               from calsificacion_delito cd inner join delito de on cd.delito_especifico = de.delito_especifico_calsificacion_delito
               group by cd.grupo
               order by numero_casos desc"""

def analisis3():
    return """ select etapa, count(etapa) as numero_casos
               from proceso
               group by etapa
               order by numero_casos desc"""

def analisis4():
    return """ select gv.genero, re.condena, count(re.condena) as numero_casos
               from ((delito de inner join grupo_victimas gv on gv.id_grupo = de."id_grupo_Grupo_victimas") inner join proceso pr on pr.id_proceso = de.id_proceso_proceso) inner join resultado re on re.id_resultado = pr.id_resultado_resultado
               group by gv.genero, re.condena
               order by numero_casos desc"""

def analisis4_m():
    return """select re.condena, count(re.condena) as numero_casos
               from ((delito de inner join grupo_victimas gv on gv.id_grupo = de."id_grupo_Grupo_victimas") inner join proceso pr on pr.id_proceso = de.id_proceso_proceso) inner join resultado re on re.id_resultado = pr.id_resultado_resultado
               where gv.genero = 'MASCULINO'
			   group by re.condena
               order by numero_casos desc"""

def analisis4_f():
    return """select re.condena, count(re.condena) as numero_casos
               from ((delito de inner join grupo_victimas gv on gv.id_grupo = de."id_grupo_Grupo_victimas") inner join proceso pr on pr.id_proceso = de.id_proceso_proceso) inner join resultado re on re.id_resultado = pr.id_resultado_resultado
               where gv.genero = 'FEMENINO'
			   group by re.condena
               order by numero_casos desc"""
               # select gv.genero, re.condena, count(re.condena) as numero_casos
