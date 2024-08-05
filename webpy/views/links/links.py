import reflex as rx
from webpy.components.link_button import link_button
from webpy.components.title import title
from webpy.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
        
        title("Proyectos"),
        
        link_button("Electronica 📡",
                    "Sensores IoT con LoRa",
                    "icon/chip.svg",
                    "https://github.com/maufranzar"),
        
        link_button("Data Science 📈",
                    "Extraccion, Procesamiento y Visualizacion de Datos",
                    "icon/data.svg",
                    "https://www.kaggle.com/maufranzar"),
        
        link_button("Machine Learning 🦾",
                    "Prediccion, Clasificacion, Clustering",
                    "icon/brain.svg",
                    "https://streamlit.io/"),
        
        link_button("Deep Learning 🤗",
                    "Hugging Face Transformers",
                    "icon/robot.svg",
                    "https://huggingface.co/maufranzar"),
        
        title("Contacto"),
        
        link_button("LinkedIn",
                    "Mi experiencia y formacion academica",
                    "icon/linkedin.svg",
                    "https://linkedin.com/in/maufranzar"),
        
        link_button("Contacto 📨",
                    "Escribeme un mail",
                    "icon/mail.svg",
                    "https://github.com/maufranzar"),
              
        
        width="100%",
        spacing=Size.MEDIUM.value,
    )