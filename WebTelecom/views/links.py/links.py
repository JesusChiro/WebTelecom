import reflex as rx
import WebTelecom.styles.styles as styles
from WebTelecom.styles.styles import Size
from WebTelecom.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("jesus", color=Color.PRIMARY.value),
            rx.span("chiroque", color=Color.SECONDARY.value),
            style=styles.navbar_title_style,
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
