import reflex as rx
from WebTelecom.styles.fonts import Font
from WebTelecom.styles.styles import Size
from WebTelecom.styles.colors import Color, TextColor


def navbar():
    return rx.center(
        rx.hstack(
            rx.image(
                src="logo.png",
                width=Size.VERY_BIG.value,
                height=Size.BIG.value,
            ),
            rx.spacer(),
            rx.hstack(
                rx.menu(
                    rx.menu_button("Nosotros"),
                    rx.spacer(),
                    rx.menu_button("Proyectos"),
                    rx.spacer(),
                    rx.menu_button("Principales Clientes"),
                    rx.spacer(),
                    rx.menu_button("Contactenos"),
                    color=TextColor.NAVBAR.value,
                    margin_x=Size.VERY_BIG.value,
                ),
            ),
        ),
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        background_color=Color.CONTENT.value,
        position="fixed",
        top="0px",
        z_index="999",
        width="100%",
    )
