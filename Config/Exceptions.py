from Config.Messages import Messages


class BkdError(Exception):
    def __init__(self, message='', title='', *args: object) -> None:
        self.__message = message
        self.__title = title
        super().__init__(*args)

    @property
    def message(self) -> str:
        return self.__message

    @property
    def title(self) -> str:
        return self.__title


class ImpossibleMove(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        message = Messages()
        if title == '':
            title = message.IMPOSSIBLE_MOVE
        super().__init__(message, title, *args)


class MusicUnavailable(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class YoutubeError(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class BadCommandUsage(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DownloadingError(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class SpotifyError(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DeezerError(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class UnknownError(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidInput(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class WrongLength(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorMoving(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorRemoving(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidIndex(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class NumberRequired(BkdError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)
