from glob import glob
import random
import tkinter as tk
import tkinter.ttk as ttk
import os


class SplashScreen:
    def __init__(self) -> None:
        self.__root = tk.Tk()
        image = self.__get_splash_image()
        if image is not None:
            self.splash = tk.PhotoImage(file=image)
            tk.Label(self.__root, image=self.splash).grid(row=0, column=0)

        self.__status = tk.Label(self.__root, text="Loading... 0%")
        self.__status.grid(row=1, column=0)

        self.__pbar = ttk.Progressbar(self.__root, mode='determinate')
        self.__pbar.grid(row=2, column=0, sticky="ew")

        self.__root.update()

    @staticmethod
    def __get_splash_image() -> str | None:
        """
        It gets a random image from the splash folder and returns it
        :return: The path to the splash image.
        """
        if not os.path.exists(os.path.join(".", "splash")):
            return None

        path = os.path.join(".", "splash")

        # Getting a random file from the splash folder and setting it as the splash screen.
        files = glob("*", root_dir=path)
        file = random.choice(files)

        return os.path.join(path, file)

    def set_progress(self, progress, update_status=False) -> None:
        """
        `set_progress` is a function that takes in two arguments, `progress` and `update_status`,
        and returns `None`

        :param progress: The progress value (0-100)
        :param update_status: This is a function that will be called to update the
        status of the progress bar, defaults to False (optional)
        """
        self.__pbar['value'] = int(progress)
        if update_status:
            self.update_status(f"Loading... {int(progress)}%")

        self.__root.update()

    def increment_progress(self, increment, update_status=False) -> None:
        """
        > The function takes in a progress value and an optional boolean value to update the status
        bar. If the boolean value is set to True, the status bar will be updated with the progress
        value

        :param increment: Increment the progress of the task
        :param update_status: If True, the status bar will be updated with the progress, defaults
        to False (optional)
        """
        progress = self.__pbar['value'] + int(increment)
        self.__pbar['value'] += progress
        if update_status:
            self.update_status(f"Loading... {progress}%")

        self.__root.update()

    def update_status(self, status) -> None:
        """
        It updates the status bar with the given text

        :param status: The status to be displayed
        """
        self.__status['text'] = status

        self.__root.update()
