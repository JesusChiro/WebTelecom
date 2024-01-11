"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import WebTelecom.styles.styles as styles
from WebTelecom.components.navbar import navbar
from WebTelecom.views.header.header import header


class State(rx.State):
    """The app state."""

    pass


@rx.page(route="/", title="NMT")
def index():
    return rx.fragment(
        navbar(),
        # rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            header(),
        ),
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
# app.add_page(index)
app.compile()
