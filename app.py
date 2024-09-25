import streamlit as st
import streamlit_shadcn_ui as ui 

layout = "centered"
page_title = "Portafolio | Gustavo Boada"
page_icon = "⭐️"
archivo_cv = "assets/CV.pdf"
telefono = "+584141240654"
mensaje = "Hola Gustavo, te estoy contactando desde tu sitio web"
mensaje_url = mensaje.replace(' ', '%20') 

css_file = "styles/main.css"
# LINK REDES SOCIALES
social_media = {
    "Whatsapp": f"https://api.whatsapp.com/send?phone={telefono}&text={mensaje_url}",
    "LinkedIn": "https://www.linkedin.com/in/gboada23/",
    "GitHub": "https://github.com/gboada23",
    "Upwork": "https://www.upwork.com/freelancers/~010f8d70b496d73cb5?mp_source=share",
    "Get-on-board": "https://www.getonbrd.com/p/gustavo-boada-lugo",
    "Instagram": "https://www.instagram.com/boada_g/"
}

proyectos = {
    "🏆 Predicción calidad vino - Redes neuronales": "https://colab.research.google.com/drive/1VY5EUhygd16_uwqlOfNyh5UU525bO2Jq?usp=sharing",
    "🏆 Análisis y visualización de datos - Pandemia Colombia": "https://github.com/gboada23/DATA-ANALYST",
    "🏆 Web scraping - MLB": "https://github.com/gboada23/scpraping-web-MLB",
    "🏆 Análisis y storytelling - MLB 2022": "https://analisis-pitchers-2022.streamlit.app/",
    "🏆 Envío automático de correos masivos": "https://github.com/gboada23/calculo-de-evaluaciones-GG",
    "🏆 API en Flask - Integración CRM": "https://github.com/gboada23/API-EVALUACIONES-FLASK",
    "🏆 App Tkinter - Negociaciones": "https://github.com/gboada23/APP-TKINTER",
    "🏆 Generador de PDFS - Presupuestos de refrigeración": "https://presupuestos-refrimamat05.streamlit.app/",
    "🏆 Generador de códigos QR": "https://qr-generador-gustavo-boada.streamlit.app/",
    "🏆 Interpolación e integración numérica": "https://github.com/gboada23/Interpolacion-e-integracion-numerica/",
    "🏆 Bot de telegram - Python": "https://github.com/gboada23/BOT-TELEGRAM-CAPITALES",
    "🏆 Test técnico resuelto usando Python":"https://colab.research.google.com/drive/1wvh7shTS5IFkHh74Iaacflt319Ag1gpD#scrollTo=Y1iOzdz0w--V",
    "🏆 Dashboard Rentabilidades de Productos":"https://lookerstudio.google.com/reporting/c4b454cb-1542-485d-9fda-fcc0fc4bf4fc",
    "🏆 Dashboard de Gestión de personal operativo":"https://lookerstudio.google.com/reporting/9bf1e9af-08d1-42cb-9856-1d22b96f6dbf",
    "🏆 Dashboard de Hoteles afiliados a empresa de transporte":"https://lookerstudio.google.com/reporting/4b4cd7e9-cae6-4349-a704-810e1e8056d1"
    }

Cursos ={
    "✅ Python de cero a Master" :"https://www.udemy.com/certificate/UC-7c5b9c4e-9976-45e7-a839-9da004228561/",
    
    "✅ Análisis y visualización de datos" : "https://www.udemy.com/certificate/UC-ab461b11-b539-4708-ad54-dfb55865fccc/",

    "✅ Análisis avanzado para Data Science": "https://www.udemy.com/certificate/UC-fce6892d-9dec-4c7f-873b-68082cbcc92a/",
    
    "✅ Machine learning":"https://www.udemy.com/certificate/UC-4288978f-8088-44a0-b0c2-2d90d17fb7bd/",
    
    "✅ SQL usando Postgresql" :"https://www.udemy.com/certificate/UC-812dc016-3225-460e-9093-e0f210ece11e/" ,

    "✅ Visualizacion de datos con Looker studio": "https://www.udemy.com/certificate/UC-87f6149e-5d5e-4a04-a74c-2ea8815f3766/",

    "✅ Matemáticas Financieras con python y excel" :"https://www.udemy.com/certificate/UC-5426e008-959c-487e-aeda-0375ffe9fb10/",
    
    "✅ Machine Learning Aplicado a Python y ciencia de datos" :"https://www.udemy.com/certificate/UC-0ef6ae17-20b1-4ef0-9b55-258978c17580/",
    
    "✅ Scraping web con python usando Bs4, Selenium y Scrapy" :"https://www.udemy.com/certificate/UC-635b173a-564f-40c8-8a9d-fbc8a80757ab/",	

    "✅ Google Cloud Platform- Fundamentos Laborarios y practicas" :"https://www.udemy.com/certificate/UC-5c04b559-2cad-4f94-bf69-12ba3069cd49/"	
    }
# Configuracion de la pagina
st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=layout)

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(archivo_cv, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# PORTAFOLIO PERSONAL
# Centrando el título usando HTML y CSS
st.markdown("<h1 style='text-align: center;'>Portafolio Data Analyst Sr.</h1>", unsafe_allow_html=True)

# PORTADA
st.write("##")
col1, col2 = st.columns(2)

with col1:
    st.image('assets/profile.png', width=250)
with col2:
    st.title("Gustavo Boada")
    st.markdown("##### Data Analyst / Actuario en formación")
    st.markdown(
    """
    <style>
    .justificado {
        text-align: justify;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
# Texto justificado usando la clase CSS 'justificado'
    st.markdown(
        """
        <div class="justificado">
        Tengo amplios conocimientos en estadística y análisis de datos, 
        con experiencia en la automatización de procesos mediante bots de Telegram, 
        predicciones y redes neuronales y el uso de Python, tambien en web scraping, 
        creación de dashboards interactivos, entre otros. 
        Mi enfoque está en maximizar la eficiencia y extraer valor de los datos mediante soluciones innovadoras.
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write(" ")
    #st.write("Conocimientos en: Python, SQL, Power Bi, Looker studio, GCP")
    st.write("📬", "gustaboadalugo@gmail.com")
    st.download_button(
        label="📄 Descargar CV ⬇️",
        data=PDFbyte,
        file_name="CV_Gustavo_Boada.pdf",
        mime="application/pdf")
 
# PROYECTOS

st.write("##")
st.subheader("Proyectos")
st.write("---")

for proyecto, url in proyectos.items():
    st.write(f"[{proyecto}]({url})")

# HABILIDADES TECNICAS

st.write("##")
st.subheader("Habilidades Técnicas")
st.write("---")

st.write("""
- 💻 Programación: Python, R, HTML, CSS
- ⚙️ Software: SPSS, Appsheet, Power Automate, Microsoft 365 office
- 🛢 Bases de datos: MySQL, SQL-Server, PostgreSQL, SQlite, Firebase, Bigquery
- 📊 Visualización de datos: Power Bi, Looker studio, Dash, Streamlit, Tableu""")

# ESTUDIOS 

st.write("##")
st.subheader("Educación")
st.write("---")

st.write("""
- 🎓 Licenciatura en Ciencias Actuariales (UCV-Venezuela) - Cursando 8vo Semestre
""")
st.write("""
         
- 🎓 Tecnico medio en informatica
""")
# EXPERIENCIA
st.write("##")
st.subheader("Experiencia")
st.write("---")

# TRABAJO 1
st.markdown("<h4 style='text-align: center;'>Especialista en Analisis de datos</h1>", unsafe_allow_html=True)
st.write("**Zudalpro C.A.  /  Julio 2024 - Actualidad**")
st.write("""
- ▶️ Análisis de datos en Python para encontrar patrones.
- ▶️ Creación y mantenimiento de reportes en Power BI y Looker studio.
- ▶️ Automatización de tareas con Power Automate.
- ▶️ Conexiones a SQL para crear sistema CRUD (ETL). 
- ▶️ Alimentar base de datos de MySQL a SQL server con python.
- ▶️ Automatizar reportes de PDF dinámicos con resumenes semanales.
- ▶️ Crear tablas y bases de datos relacionales en Sql-Server.
- ▶️ Crear vistas resumidas en Sql-server con varias relaciones en una sola tabla.
         
                           """)
st.write("---")

# TRABAJO 2

st.markdown("<h4 style='text-align: center;'>Coordinador de datos</h1>", unsafe_allow_html=True)
st.write("**Serviplus, C.A.  /  Octubre 2022 a Julio 2024**")
st.write("""
- ▶️ Análisis de datos en Python para encontrar patrones.
- ▶️ Creación y mantenimiento de dashboard de KPI en Looker studio.
- ▶️ Automatización de reportes.
- ▶️ Implementar soluciones innvadoras para manipulacion y limpieza de datos. 
- ▶️ Desarrollo de Bot de telegram que te generan resumenes diarios.
- ▶️ Web scraping para obtener informacion y evaluar a la competencia.
- ▶️ Creación de dashboards interactivos con Tableau.
- ▶️ Proporcionar insights valiosos para la toma de decisiones.""")
st.write("---")

# TRABAJO 3

st.markdown("<h4 style='text-align: center;'>Coordinado de Materia Estadistica</h1>", unsafe_allow_html=True)
st.write("**Data Eppa Consultores, C.A.  /  Enero 2020 a Julio 2022**")
st.write("""
- ▶️ Limpieza y transformacion de datos.
- ▶️ Analisis exploratorio de datos para llegar a conclusiones.
- ▶️ Conexiones a SQL para insertar la data obtenida de googlesheets. 
- ▶️ Crear dashboard de la data limpia en SQL.""")

# CURSOS
st.write("##")
st.subheader("Cursos con certificados")
st.write("---")
for curso, url in Cursos.items():
    st.write(f"[{curso}]({url})")

# CONTACTO

st.subheader("Redes Sociales")
st.write("---")
# Añadir clases CSS manualmente dentro del bucle

# BOTONES REDES SOCIALES
cols = st.columns(len(social_media))
# Crear botones con estilos de ui.link_button
for index, (platform, url) in enumerate(social_media.items()):
    with cols[index]:  # Asignar la clase correspondiente
        ui.link_button(text=platform, url=url, key=f"link_button_{platform}")