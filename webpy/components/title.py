import reflex as rx
import webpy.styles.styles as styles


def title(text:str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        size="md",
        )