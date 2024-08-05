import reflex as rx
import datetime
from webpy.styles.styles import Size as Size
from webpy.styles.colors import TextColor as TextColor
from webpy.components.info_text import info_text

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.image(
                src="img/logo_.png",
                height=Size.VERY_BIG.value,
                weight=Size.VERY_BIG.value,
                alt="logo de la pagina"
        ),
        
        rx.link(f"© {datetime.date.today().year} - Mauricio Franco Salazar",
                href="https://maufranzar.com",
                font_size=Size.DEFAULT.value,
                color=TextColor.FOOTER.value,
        ),
        
        rx.text("Gracias por tu visita 🐸",
                font_size=Size.DEFAULT.value,
                color=TextColor.FOOTER.value,
        ),
                
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,        
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
        
    )