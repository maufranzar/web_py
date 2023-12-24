import reflex as rx
from web_py.components.link_button import link_button
from web_py.components.title import title
from web_py.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
        
        title("Proyectos"),
        
        link_button("Electronica",
                    "Proyecto: Sensor IoT - ESP32",
                    "icon/chip.svg",
                    "https://github.com/maufranzar"),
        
        link_button("Data Science",
                    "Extraccion, Procesamiento y Visualizacion de Datos",
                    "icon/data.svg",
                    "https://www.kaggle.com/maufranzar"),
        
        link_button("Machine Learning",
                    "Prediccion, Clasificacion, Clustering",
                    "icon/brain.svg",
                    "https://streamlit.io/"),
        
        link_button("Deep Learning",
                    "Procesamiento de Imagenes",
                    "icon/robot.svg",
                    "https://huggingface.co/maufranzar"),
        
        title("Contacto"),
        
        link_button("LinkedIn",
                    "Mi experiencia y formacion academica",
                    "icon/linkedin.svg",
                    "https://linkedin.com/in/maufranzar"),
        
        link_button("Email",
                    "En construccion... 🚧",
                    "icon/mail.svg",
                    "https://github.com/maufranzar"),
              
        
        width="100%",
        spacing=Size.MEDIUM.value,
    )