import reflex as rx
from webpy.styles.styles import Size as Size
from webpy.styles.colors import TextColor as TextColor
from webpy.styles.colors import Color as Color


def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.span(title, 
                color=Color.ICON.value,
        ),
        f" {body}", 
        font_size=Size.DEFAULT.value,
        color = TextColor.BODY.value,
    )