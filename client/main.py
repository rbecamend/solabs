from nicegui import ui
from client.auth import login_page, register_page
from client.home import home_page

def setup_pages():
    @ui.page('/')
    def redirect_to_login():
        ui.navigate.to('/login')

    ui.page('/login')(login_page)
    ui.page('/register')(register_page)
    ui.page('/home')(home_page)

if __name__ == "__main__":
    setup_pages()
    ui.run(
        title="SOLABS",
        port=8000,
        host="0.0.0.0",
        reload=False,
        show=False,
    )

#MAS QUE MERDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
