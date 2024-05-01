from bot import main, ConsoleUserInterface, WebUserInterface


class Commander:

    @classmethod
    def run(cls, source):
        if source == "console":
            ui = ConsoleUserInterface()
        elif source == "web":
            ui = WebUserInterface()
        else:
            ui = None
            return f"Unknow {source}"
        main(ui)


if __name__ == "__main__":
    Commander.run("console")
