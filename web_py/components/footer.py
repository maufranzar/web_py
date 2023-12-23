import reflex as rx
import datetime
from web_py.styles.styles import Size as Size
from web_py.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.image(
                src="img/logo_.png",
                height=Size.VERY_BIG.value,
                weight=Size.VERY_BIG.value,
                alt="logo de la pagina"
        ),
        
        rx.link(f"© {datetime.date.today().year}  Mauricio Franco Salazar",
                href="https://maufranzar.com",
                is_external=True,
                font_size=Size.DEFAULT.value,
                color=TextColor.FOOTER.value,
        ),
        
        rx.text("A hombros de gigantes",
                font_size=Size.DEFAULT.value,
                color=TextColor.FOOTER.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,        
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
        
    )