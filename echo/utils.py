import functools


def logger_factory(logger):
    """ Импорт функции происходит раньше чем загрузка конфига логирования.
        Поэтому нужно явно указать в какой логгер мы хотим записывать.
    """
    def debug_requests(f):

        @functools.wraps(f)
        def inner(*args, **kwargs):

            try:
                logger.debug('Обращение в функцию `{}`'.format(f.__name__))
                return f(*args, **kwargs)
            except Exception as e:
                logger.exception('Ошибка в функции `{}`'.format(f.__name__))
                raise

        return inner

    return debug_requests
