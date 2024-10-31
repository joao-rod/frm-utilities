""" Application to run command for assets install to FRM Project """

import os
import flet as ft

from dotenv import load_dotenv


class App:
    """Main application class"""

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "FRM assets:install"
        self.page.window.width = 200
        self.page.window.height = 100
        self.page.window.minimizable = False
        self.page.window.maximizable = False
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE))

        self.progress_bar = ft.ProgressBar(color="amber", bgcolor=ft.colors.BLUE_GREY)

        self.page.add(
            ft.ElevatedButton("Run assets:install", on_click=self.assets_install)
        )

    def assets_install(self, e):
        """Run command for assets install"""
        load_dotenv()

        self.page.add(self.progress_bar)

        os.system(os.getenv("ASSETS_INSTALL_CMD"))

        self.page.remove(self.progress_bar)
        self.page.update()


def main(page: ft.Page):
    """Initialize the application"""
    App(page)


ft.app(target=main)
