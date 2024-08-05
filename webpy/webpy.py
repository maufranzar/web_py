...

import reflex as rx
...

from webpy.components.navbar import navbar
from webpy.components.footer import footer
from webpy.views.header.header import header
from webpy.views.links.links import links
import webpy.styles.styles as styles
from webpy.styles.styles import Size as Size

...


# class State(rx.State):
#     pass


...
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            )
        ),
        footer()
    )

    
...

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=["fonts/fonts.css"],
)


app.add_page(
    index,
    title="maufranzar",
    description="web personal hecha solo con python! :D | Gracias Reflex!",
    image="img/logo_.ico",
)
app.compile()