"""
This script is the entrypoint for the notes website.
"""

from nicegui import ui


title = "Notes"


@ui.page("/")
def main_page():
    """
    This function defines the content of the main landing page of the notes
    website.
    """
    ui.markdown(
        f"""
# {title}

I'm going to try to put some teaching notes for the B2 and B6 courses here.
I'll update this throughout term.
        """
    )

    # Add some options to the right drawer.
    with ui.right_drawer(fixed=False, bordered=False).props(
        "bordered"
    ) as right_drawer:
        ui.markdown("# :)")
        right_drawer.toggle()

    # Add the header.
    with ui.header(elevated=True).classes("items-center justify-between"):
        ui.markdown(f"##{title}")
        ui.button(on_click=right_drawer.toggle, icon="menu").props(
            "flat color=white"
        )

    # Make a left drawer that's the same width as we would have with material
    # mkdocs.
    with ui.left_drawer(bordered=False):
        ui.markdown(f"##### {title}")
        with ui.list():
            ui.item("B6").props("clickable")
            ui.item("PS1")
            ui.item("PS2")
            ui.item("PS3")
            ui.item("PS4")
            ui.item("PS5")
            with ui.item("B2").props("clickable"):
                ui.item_section("PS1")
                ui.item_section("PS2")
                ui.item_section("PS3")
                ui.item_section("PS4")
                ui.item_section("PS5")

    # Make a footer that links to the github issues page.
    with ui.footer():
        ui.label(
            "Spot any mistakes? Go to the",
        )
        ui.link(
            "github issues page", target="github.com/rbrearton/notes/issues"
        ).classes("text-white"),


def main():
    """
    Running this function spins up the website.
    """


ui.run()
