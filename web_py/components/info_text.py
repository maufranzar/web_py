import reflex as rx
from web_py.styles.styles import Size as Size
from web_py.styles.colors import TextColor as TextColor
from web_py.styles.colors import Color as Color


def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.span(title, 
                color=Color.ICON.value,
        ),
        f" {body}", 
        font_size=Size.DEFAULT.value,
        color = TextColor.BODY.value,
    )