import reflex as rx
from webpy.styles.styles import Size as Size
from webpy.styles.colors import Color as Color

def link_icon(image:str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            color=Color.ICON.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )