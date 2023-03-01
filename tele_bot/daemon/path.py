from enum import Enum
from tele_bot.settings import conf


class ButtonXpath(Enum):
    BACK = "/html/body/div/div/div/header/div/div/div/a[4]"
    BUTTON = "/html/body/div/div[1]/div/section/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/div/i"
    BUTTON_PASSENGER = "/html/body/div/div[2]/div/div[1]"
    BUTTON_BUS = "/html/body/div/div[2]/div/div[2]"


class FilePath(Enum):
    BENIAKONI = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[1]",
        "cargo_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "beniakoni"
        / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "beniakoni"
        / "passenger.html",
        "bus_path": conf.BASE_DIR / "daemon" / "pages" / "beniakoni" / "bus.html",
    }
    BERESTOVICA = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[2]",
        "cargo_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "berestovitsa"
        / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "berestovitsa"
        / "passenger.html",
        "bus_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "berestovitsa"
        / "bus.html",
    }
    BREST = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[3]",
        "cargo_path": conf.BASE_DIR / "daemon" / "pages" / "brest" / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "brest"
        / "passenger.html",
        "bus_path": conf.BASE_DIR / "daemon" / "pages" / "brest" / "bus.html",
    }
    GRIGOROVSHCINA = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[4]",
        "cargo_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "grigorovshcina"
        / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "grigorovshcina"
        / "passenger.html",
        "bus_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "grigorovshcina"
        / "bus.html",
    }
    KAMENNY_LOG = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[5]",
        "cargo_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "kamenny_log"
        / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "kamenny_log"
        / "passenger.html",
        "bus_path": conf.BASE_DIR / "daemon" / "pages" / "kamenny_log" / "bus.html",
    }
    KOTLOVKA = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[6]",
        "cargo_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "kotlovka"
        / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "kotlovka"
        / "passenger.html",
        "bus_path": conf.BASE_DIR / "daemon" / "pages" / "kotlovka" / "bus.html",
    }
    URBANY = {
        "xpath": "/html/body/div/div/div/section/div/div[2]/div/div/table/tbody/tr[7]",
        "cargo_path": conf.BASE_DIR / "daemon" / "pages" / "urbany" / "cargo.html",
        "passenger_path": conf.BASE_DIR
        / "daemon"
        / "pages"
        / "urbany"
        / "passenger.html",
        "bus_path": conf.BASE_DIR / "daemon" / "pages" / "urbany" / "bus.html",
    }
