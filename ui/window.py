import sdl2
sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
class Window:
    """
    window class, show window when create object
    """
    def __init__(self, title: str, closable: bool = False):
        """
        args:
        title(str)
        closable(bool)
        """
        self._title = title.encode("utf-8")
        self.closable = closable
        self.window = None
        self.running = False

    def show(self):
        """
        create and show window when called
        """
        self.running = True
        self.window = sdl2.SDL_CreateWindow(self._title, sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, 600, 400, sdl2.SDL_WINDOW_SHOWN)
        if not self.window:
            raise RuntimeError("Could not create SDL2 window")

    def set_closable(self, closable: bool):
        """
        set window closable
        args:
        closable(bool)
        """
        self.closable = closable

    def event_process(self):
        event = sdl2.SDL_Event()
        while sdl2.SDL_PollEvent(event):
            if event.type == sdl2.SDL_QUIT and self.closable:
                self.running = False

    def __del__(self):
        """
        destroy window when delete the object anyway
        """
        if hasattr(self, "window") and self.window:
            sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()
