class Config:
    APP_NAME = "GPX Time Offset"
    APP_DEFAULT_WIDTH = 1200
    APP_DEFAULT_HEIGHT = 600
    APP_MIN_WIDTH = 800
    APP_MIN_HEIGHT = 600
    APP_DEFAULT_GEOMETRY = f"{APP_DEFAULT_WIDTH}x{APP_DEFAULT_HEIGHT}"

    MESSAGE_BOX_DEFAULT_WIDTH = 400
    MESSAGE_BOX_DEFAULT_HEIGHT = 100

    DEFAULT_PADX = 10
    DEFAULT_PADY = 10
    DEFAULT_PADX_LEFT = (DEFAULT_PADX, 0.5 * DEFAULT_PADX)
    DEFAULT_PADX_MIDDLE = (0.5 * DEFAULT_PADX, 0.5 * DEFAULT_PADX)
    DEFAULT_PADX_RIGHT = (0.5 * DEFAULT_PADX, DEFAULT_PADX)
    DEFAULT_PADY_TOP = (DEFAULT_PADY, 0.5 * DEFAULT_PADY)
    DEFAULT_PADY_MIDDLE = (0.5 * DEFAULT_PADY, 0.5 * DEFAULT_PADY)
    DEFAULT_PADY_BOTTOM = (0.5 * DEFAULT_PADY, DEFAULT_PADY)
    DEFAULT_HEIGHT = 25