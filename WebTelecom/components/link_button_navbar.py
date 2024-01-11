import reflex as rx
import WebTelecom.styles.styles as styles
from WebTelecom.styles.styles import Size as Size


def link_button_navbar(txt: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.text(
                    txt,
                    # width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                ),
                width="100%",
            )
        ),
        is_external=False,
        width="100%",
    )
