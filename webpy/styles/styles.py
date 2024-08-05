# Desc: Styles for the web app
import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font


# Constatns
MAX_WIDTH = "580px"


# 1 em = tamano de fuente 

#Sizes
class Size(Enum):
    
    ZERO = "0px !important"
    SMALL = "0.6em"
    MEDIUM = "0.9em"
    DEFAULT = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "12em"
    

# Styles

BASE_STYLE = {
    
    "font_family":Font.DEFAULT.value,
    "background_color":Color.BACKGROUND.value,
    
    rx.Button: {
        
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background_color":Color.CONTENT.value,
        "white_space": "nowrap",
        "text_align": "left",
        "color":TextColor.HEADER.value,
        "_hover":{"background_color":Color.PRIMARY.value},
    },
    rx.Link: {
        
        "text_decoration": "none",
        "_hover": {},
        
    }
}

title_style = dict(
    font_family=Font.TITLE.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_size=Size.DEFAULT.value,
)

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.BIG.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.HEADER.value,
    
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
    
)