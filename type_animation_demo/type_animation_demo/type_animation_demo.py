"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_type_animation import type_animation

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            type_animation(
                sequence=[
                    "Lewis Hamilton is the Greatest Driver of all time.",
                    1000
                ],
            ),

            type_animation(
                sequence=[
                    "Michael Schumacher",
                    1000,
                    "Max Ver",
                    1000,
                    "Lewis Hamilton is the Greatest Driver of all time.",
                    1000
                ],
                repeat=float("inf")
            ),
        ),

        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
