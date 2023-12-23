import reflex as rx
from web_py.components.link_icon import link_icon
from web_py.components.info_text import info_text
from web_py.styles.styles import Size as Size
from web_py.styles.colors import TextColor as TextColor
from web_py.styles.colors import Color as Color
from web_py.styles.fonts import Font as Font
from web_py.components.title import title



def header() -> rx.Component:
    return rx.vstack(
        
        rx.hstack(
            rx.avatar(
                src="img/me_bg.png",
                size="xl",
                color=TextColor.BODY.value,
                bg=Color.BACKGROUND.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                title("Mauricio Franco Salazar"),
                rx.text("@maufranzar",
                    magin_top=Size.ZERO.value,
                    color=Color.ICON.value,
                    font_size=Size.MEDIUM.value
                ),
                rx.hstack(
                    link_icon("icon/github.svg",
                              "https://github.com/maufranzar",
                              "Github"
                    ),
                    link_icon("icon/twitter.svg",
                              "https://twitter.com/maufranzar",
                              "Twitter"
                    ),
                    link_icon("icon/spotify.svg",
                              "https://open.spotify.com/user/bmbpwp9beicgbbbaq0rmjwawm",
                              "Spotify"
                    ),
                    link_icon("icon/instagram.svg",
                              "https://www.instagram.com/maufranzar/",
                              "Instagram"
                    ),
                    spacing=Size.BIG.value,
                ),
                align_items="start",
            
            ),
            spacing=Size.MEDIUM.value,              
        ),
        
        rx.flex(
            info_text("+2","experiencia"),
            rx.Spacer(),
            info_text("+2","experiencia"),
            rx.Spacer(),
            info_text("+2","experiencia"),
            width="100%",
        ),
        
        
        rx.text("""
            Lorem ipsum dolor sit amet consectetur adipisicing elit.Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Lorem ipsum dolor sit amet consectetur adipisicing elit.Lorem ipsum dolor sit amet consectetur adipisicing elit.
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value,
            
        ),
        spacing=Size.BIG.value,
        align_items="start"

)