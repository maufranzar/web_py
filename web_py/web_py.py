...

import reflex as rx
...



from web_py.components.navbar import navbar
from web_py.components.footer import footer
from web_py.views.header.header import header
from web_py.views.links.links import links
import web_py.styles.styles as styles
from web_py.styles.styles import Size as Size


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
    title="",
    description="",
    image="",
)
app.compile()