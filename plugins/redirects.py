from datasette import hookimpl, Response


@hookimpl
def register_routes():
    return (
        (
            r"^/conduct/?$",
            lambda request: Response.redirect(
                "https://github.com/simonw/datasette/blob/main/CODE_OF_CONDUCT.md",
                status=301,
            ),
        ),
        (
            r"^/discord/?$",
            lambda request: Response.redirect(
                "https://discord.gg/ktd74dm5mw", status=301
            ),
        ),
        (
            r"^/discord-llm/?$",
            lambda request: Response.redirect(
                "https://discord.gg/RKAH4b8TvE", status=301
            ),
        ),
        (
            r"^/discord-enrichments/?$",
            lambda request: Response.redirect(
                "https://discord.gg/tcTpMVQdRc", status=301
            ),
        ),
        # /help/X may be linked to from the datasette CLI - served with 302 because I may change
        # what they target in the future.
        (
            r"^/help/extensions/?$",
            lambda request: Response.redirect(
                "https://docs.datasette.io/en/stable/installation.html#a-note-about-extensions",
                status=302,
            ),
        ),
    )
