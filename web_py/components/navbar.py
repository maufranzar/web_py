import reflex as rx
import web_py.styles.styles as styles
from web_py.styles.styles import Size as Size
from web_py.styles.colors import Color as Color



def navbar() -> rx.Component:
    return rx.hstack(

                rx.box(
                    rx.span("mau",color=Color.PRIMARY.value),
                    rx.span("fran",color=Color.SECONDARY.value),
                    rx.span("zar",color=Color.PRIMARY.value),
                    style=styles.navbar_title_style,
                ),

            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=Size.MEDIUM.value,
            padding_y=Size.MEDIUM.value,
            z_index="999",
            top="0"
            )