import streamlit as st
from PIL import Image
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Curriculum | Gustavo Boada",
    page_icon=":guardsman:",
    layout="wide")
st.sidebar.caption("CV ITERACTIVO")
imagen1 = Image.open(r"images/perfil.jpg")
st.sidebar.image(imagen1, width=270)

st.sidebar.markdown(
    """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 1.6em;'><b>  GUSTAVO BOADA LUGO</b></span>
    </div>""",unsafe_allow_html=True)

st.sidebar.markdown("### **FECHA DE NACIMIENTO**")
st.sidebar.markdown('''<font color="green">
                <b>23/02/1998
                </font>''', unsafe_allow_html=True)


st.sidebar.markdown("### **ACTUARIO EN FORMACION**")
st.sidebar.markdown('''<font color="green">
                <b>Cursando 6to Semestre de Cs Actuariales
                </font>''', unsafe_allow_html=True)

st.sidebar.divider()
expander = st.sidebar.container()

st.sidebar.image("images/linkedin.png",width=64, caption="Gboada23")
st.sidebar.markdown("[Perfil de Linkedin](https://www.linkedin.com/in/gboada23/)")
  
st.sidebar.image("images/telefono.png",width=42, caption="Phone")
st.sidebar.markdown('''<font color="green">
                <b>0414-1240654 | 0412-6050917
                </font>''', unsafe_allow_html=True) 

st.sidebar.image("images/correo.png", width=40, caption="Email")

st.sidebar.markdown('''<font color="green">
                <b>Gustavoboadalugo@gmail.com
                </font>''', unsafe_allow_html=True)
st.sidebar.write(" ")
st.sidebar.image("images/direccion.png", width=60, caption="Direccion")
st.sidebar.markdown('''<font color="green">
                <b>Caracas, Parroquia La candelaria Sector San Bernardino 
                </font>''', unsafe_allow_html=True)

st.sidebar.divider()


st.sidebar.markdown(
    """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 1.6em;'><center><b>  PERFIL PROFESIONAL </b></center></span>
    </div>""",unsafe_allow_html=True)
st.sidebar.write(" ")
st.sidebar.markdown(
    """<div style='background-color: #160C80; padding: 5px; border-radius: 5px;'>
    <p style='text-align: justify; color: white; font-size: 1em;'>
    <b>Soy un profesional en formación para convertirme en Actuario, 
    cursando 7mo semestre de Cs Actuariales en la UCV con una sólida 
    formación académica y habilidades en análisis de datos. Soy una 
    persona seria y responsable, con actitud proactiva y siempre dispuesto
    a aprender. Tengo experiencia trabajando como analista de datos. Estoy
    enfocado en mi carrera y seguir aumentando mis conocimientos sobre 
    gestión de proyectos, Inteligencia Artificial, finanzas, riesgos y seguros, 
    con la intención de ser un Actuario con todas las herramientas necesarias que se necesitan en el mercado laboral. Confío 
    en que mis habilidades me permitirán contribuir significativamente a cualquier empresa 
    donde pueda aplicar mis conocimientos.</b>
    </p>
    </div>""",
    unsafe_allow_html=True
)
st.markdown(
    """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 1.8em;'><center><b>  EXPERIENCIA PROFESIONAL</b></center></span>
    </div>""",unsafe_allow_html=True)
col1, col2, col3 = st.columns((3,4,2))
with col1:
    st.write("")
    st.write("")
    
with col2:
    st.write("")

st.markdown("")   
with col1:
    st.markdown('''<font color="green" style="font-size:20px">
                <center><b>COORDINADOR DE DATOS</b></center>
                </font>''', unsafe_allow_html=True)
    st.expander(" OCTUBRE 2022 / ACTUAL").markdown("""<p style='text-align: justify; color: white; font-size: 1em;'> 
    Desarrollé una aplicación en AppSheet para la gestión de asistencia y desempeño del personal, 
    que almacena datos en Google Sheets. Creación de dashboard de KPI en Data Studio, que se alimenta
      de la BD de la aplicación a tiempo real que permiten visualizaciones claras y fáciles de entender, 
      lo que facilita la toma de decisiones. Adicionalmente, implementé funciones para crear automatizaciones 
      de procesos manipulando la data usando Python. También creé un bot de Telegram e integré las funciones de
        automatización dentro de él, por lo que el bot ejecuta automáticamente la tarea correspondiente. 
        Esta integración mejoró aún más la eficiencia y eficacia de los procesos en la empres también cree un sistema de 
        incidencias para el departamento de RRHH a través de python.</p>
    </div>""",
    unsafe_allow_html=True)
with col2:
    st.write("")
    st.markdown('''<font color="green" style="font-size:20px">
                <center><b>COORDINADOR DE MATERIA ESTADISTICA</b></center>
                </font>''', unsafe_allow_html=True)
    st.expander("ENERO 2020 / JULLIO 2022").markdown("""<p style='text-align: justify; color: white; font-size: 1em;'> 
    Empresa se encarga de realizar Encuestas de cualquier tipo dependiendo del cliente, 
    Generaba las estadísticas y análisis de esos datos realizando un proceso previo de 
    limpieza y manipulación de datos a través de Python para llegar a conclusiones para que la 
    empresa contratante pudiera tomar decisiones</p>
    </div>""",
    unsafe_allow_html=True)

with col3:
    st.write(" ")
    st.write(" ")
    st.markdown('''<font color="green" style="font-size:20px">
                <center><b>OPERADOR SENIOR</b></center>
                </font>''', unsafe_allow_html=True)
    st.expander("ABRIL 2019 / NOVIEMBRE 2020").markdown("""<p style='text-align: justify; color: white; font-size: 1em;'> 
    Realizaba monitoreo a los ATM a nivel nacional para visualizar fallas o algún 
    inconveniente en el mismo para intentar solventarla, si no podía solventarla 
    llamaba al tesorero de la agencia para que intentará el poner el cajero en 
    funcionamiento de manera presencials</p>
    </div>""",
    unsafe_allow_html=True)
st.divider()
col1, col2, col3 = st.columns((3,4,3))

st.markdown(
    """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 1.8em;'><center><b>  EDUCACION </b></center></span>
    </div>""",unsafe_allow_html=True)
with col2:
    st.write("")
col1, col2 ,col3= st.columns((4,4,4))
with col1:
    st.write("")
    st.markdown('''<font color="green" style="font-size:20px">
                <center><b>PRIMARIA</b></center>
                </font>''', unsafe_allow_html=True)
    st.expander("U.E.B PANTOJA").write("6to Grado Aprobado")
with col2:
    st.write("")
    st.markdown('''<font color="green" style="font-size:20px">
                <center><b>SECUNDARIA</b></center>
                </font>''', unsafe_allow_html=True)
    st.expander("U.E.E ARGELIA LAYA").markdown("""Tecnico medio en comercios y servicios administrativos 
                                               Mencion **Informatica** """)
   
with col3:
    st.write("")
    st.markdown('''<font color="green" style="font-size:20px">
                <center><b>UNIVERSITARIA</b></center>
                </font>''', unsafe_allow_html=True)
    st.expander("UNIVERSIDAD CENTRAL DE VENEZUELA").write("Cursando 7mo Semestre de Estadisticas y Cs Actuariales")
st.divider()
col1,col2,col3=st.columns((2,6,2))
with col2:
    st.markdown(
        """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
        <span style='color: ##1D20FA; font-size: 1.8em;'><center><b>  HABILIDADES </b></center></span>
        </div>""",unsafe_allow_html=True)
    st.markdown("")
    col1, col2, col3 = st.columns((5,5,3))
    with col1 :
        st.image("images/python.jpg",width=100, caption= "PYTHON")
        st.image("images/excel.jpg",width=100, caption= "EXCEL")
                
    with col2 :
        st.image("images/sql.png",width=100, caption= "POSTGRESQL")
        st.image("images/looker.png",width=100, caption= "LOOKER")
        
    with col3 :
        st.image("images/git.jpg",width=100, caption= "GIT")
        st.image("images/docker.png",width=100, caption= "DOCKER")
st.divider()
col1,col2,col3=st.columns((2,6,2))
col2.markdown(
    """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 1.8em;'><center><b>  CURSOS </b></center></span>
    </div>""",unsafe_allow_html=True)
col2.write(" ")
col2.expander("Visualiza todos los cursos aqui puedes tocar el nombre de cada uno para verificar las certificaciones").markdown("""
    ##### ✅   [ESCUELA DE PYTHON 2021](https://www.udemy.com/certificate/UC-7c5b9c4e-9976-45e7-a839-9da004228561/) Aprende python de 0 a Master (21 horas)
    
    ##### ✅   [PYTHON PARA ANALISIS DE DATOS](https://www.udemy.com/certificate/UC-ab461b11-b539-4708-ad54-dfb55865fccc/) Analisis y visualizacion de Datos (7 horas)

    ##### ✅   [PYTHON PARA ANALISIS DE DATOS 2](https://www.udemy.com/certificate/UC-fce6892d-9dec-4c7f-873b-68082cbcc92a/) Analisis avanzado para Data Science (5 horas)
    
    ##### ✅   [MACHINE LEARNING CON PYTHON](https://www.udemy.com/certificate/UC-4288978f-8088-44a0-b0c2-2d90d17fb7bd/) Introductorio y tutorial en la ciencia de datos (7 horas)
    
    ##### ✅   [POSTGRES SQL](https://community.open-bootcamp.com/user/gboada23/certificaciones/c63e16a4-cce9-481e-80d6-96af2ed708b3) Consultas de Bases de datos (7 horas)

    ##### ✅   [GOOGLE DATA STUDIO](https://www.udemy.com/certificate/UC-87f6149e-5d5e-4a04-a74c-2ea8815f3766/) Avanzado tutorial de visualizacion de datos (11 horas)

    ##### ✅   [MATEMATICAS FINANCIERAS CON PYTHON](https://www.udemy.com/certificate/UC-5426e008-959c-487e-aeda-0375ffe9fb10/) Interes simple, Interes compuesto, rentas y sistemas de amortizaciones (7 horas)

        """)
st.divider()
col1,col2,col3=st.columns((2,6,2))

col2.markdown(
        """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
        <span style='color: ##1D20FA; font-size: 1.8em;'><center><b>  IDIOMAS </b></center></span>
        </div>""",unsafe_allow_html=True)
col2.write("")
option = col2.radio("Nivel del Idioma seleccionado",options=["Español","Ingles","Italiano"],key="A")
if option == "Español":
    col2.markdown("### ⭐⭐⭐⭐⭐")
elif option == "Ingles":
    col2.write("### ⭐⭐⭐")
else:
    col2.write("### ⭐")
col2.divider()
col2.markdown(
    """<div style='background-color: #3E1CC4; padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 1.8em;'><center><b>  PORTAFOLIO </b></center></span>
    </div>""",unsafe_allow_html=True)
col2.write(" ")

with col2:
    subcol1,subcol2=st.columns((1,5))
    with subcol1:
        ima = st.image("images/github.png",width=80, caption="gboada23")

    with subcol2:
        st.markdown("")
        st.markdown("Para ver mi portafolio podras acceder a mi perfil de Git-hub haciendo click [Aqui](https://github.com/gboada23)")

def descargar_excel2():
        with open('CV GUSTAVO.pdf', 'rb') as f:
            bytes_data = f.read()
        col2.download_button(label="Descargar PDF", data=bytes_data, file_name='CV GUSTAVO BOADA.pdf', key='descargar_pdf')
col2.write('Descargar el CV como PDF')
descargar_excel2()
st.markdown("#")
st.caption("Curriculum creado con Python por mi persona usando el framework de stremlit")

