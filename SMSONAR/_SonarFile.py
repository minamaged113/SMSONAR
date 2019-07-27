VALUE_ERROR_MSG = 'Unexpected type of input for {}. Expected {}, but {} \
was given.'


class SonarFile:
    def __init__(self, filePath: str = None):
        if not isinstance(filePath, str) and filePath is not None:
            # check if the passed path is a string
            # if not, raise a ValueError
            raise ValueError(VALUE_ERROR_MSG.format('filePath',
                                                    'string',
                                                    'integer'))
        return
