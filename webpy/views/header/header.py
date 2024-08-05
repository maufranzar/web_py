import reflex as rx
from webpy.components.link_icon import link_icon
from webpy.components.info_text import info_text
from webpy.styles.styles import Size as Size
from webpy.styles.colors import TextColor as TextColor
from webpy.styles.colors import Color as Color
from webpy.styles.fonts import Font as Font
from webpy.components.title import title



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
                    font_size=Size.DEFAULT.value
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
            info_text("Bienvenid@","👋🏼"),
            rx.Spacer(),
            info_text("🍃"," "),
            width="100%",
        ),
        
        rx.text("""
             En este espacio comparto informacion sobre mis proyectos e intereses. Me apaciona la tecnologia y el poder que tiene para mejorar la vida las personas, sin embargo el acceso a ella no es igual para todos. Me motiva la idea de poder contribuir a reducir tal brecha. 
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value,
            
        ),
        spacing=Size.BIG.value,
        align_items="start"

)