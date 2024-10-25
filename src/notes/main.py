"""The entrypoint of the main notes website."""

from nicegui import ui

title = "Notes"


@ui.page("/", favicon="")
def main_page() -> None:
    """Define the content of the main landing page of the notes website."""
    ui.colors(primary="teal", secondary="orange")
    ui.page_title(title)

    ui.markdown(f"# {title}")
    ui.label(
        """
        I'm going to try to put some teaching notes for the B2 and B6 courses
        here.
        I'll update this throughout term.
        """,
    )

    # The right drawer.
    with ui.right_drawer(fixed=False):
        ui.markdown("This is another menu drawer.")

    # Add the header.
    with (
        ui.header(elevated=True, bordered=True)
        .props('height="h-1"')
        .classes("items-center justify-between")
    ):
        # These go on the left.
        with ui.row().classes("items-center"):
            ui.icon("description", size="md")
            ui.label("Notes").classes("text-2xl")

        # These go on the right.
        with ui.row().classes("items-center"):
            ui.input(placeholder="Search...").props(
                'input-style="color: white"',
            )
            ui.button(icon="menu").props("flat color=white")

    # The left drawer.
    with ui.left_drawer(fixed=False):
        ui.markdown(f"##### {title}")
        # The contents.
        with ui.column(align_items="stretch").style("gap: 0; padding: 0"):
            # Relativity dropdown.
            with (
                ui.expansion("B2: Symmetry and relativity")
                .props("dense items-start")
                .classes("non-selectable")
            ).style("gap: 0; padding: 0"):
                with ui.column().style("gap: 0; padding: 0"):
                    ui.label("PS1")
                    ui.label("PS2")

            with (
                ui.expansion("B6: Condensed matter physics")
                .props("dense")
                .classes("non-selectable")
            ):
                ui.label("PS1")
                ui.label("PS2")

    # The footer.
    with ui.footer(fixed=False):
        # Put a link to the github issues page.
        ui.label(
            "Spot any mistakes? Go to the",
        )
        (
            ui.link(
                "github issues page",
                target="github.com/rbrearton/notes/issues",
            ).classes("text-white"),
        )


def main() -> None:
    """Run to spin up the website."""


ui.run(favicon="icon.png")
