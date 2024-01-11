import reflex as rx
import WebTelecom.styles.styles as styles
from WebTelecom.styles.styles import Size
from WebTelecom.styles.colors import Color
from WebTelecom.components.link_button_navbar import link_button_navbar


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(
                src="logo.png",
                width=Size.VERY_BIG.value,
                height=Size.BIG.value,
            ),
            style=styles.navbar_title_style,
            width="300px",
            bg="red",
        ),
        rx.hstack(
            link_button_navbar(
                "Nosotros",
            ),
            rx.spacer(),
            link_button_navbar(
                "Nuestros Servicios",
            ),
            link_button_navbar(
                "Nosotros",
            ),
            rx.spacer(),
            link_button_navbar(
                "Nuestros Servicios",
            ),
            bg="red",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
