from functools import wraps
from inspect import getcallargs


class CustomException(Exception):
    """

    """
    # TODO: Implement Custom Exception
    pass


class Decorators:
    @staticmethod
    def force_type_hints(f):
        """Decorator wrapper function to ensure that type hints match actual parameters

        :param f: Function
        :return:
        """

        # TODO: Complete Documentation
        @wraps(f)
        def decorated(*args, **kwargs):
            """ Decorator function to ensure that type hints match actual parameters.

            first loop: will raise an exception if param_value does not match the type hint data type specified.
            second loop: execute the function and raise an exception if result data does not match the specified
            data type.
            :local_var: annotations: dict of param_name: param_type items Including the return element.
            :local_var: arguments: list of tuples (param_name, param_type) Including self parameter.
            :param args: Function arguments
            :param kwargs: Function Keyword arguments
            :return: The function value or raise an Exception
            :rtype: The function result data type
            """
            annotations = f.__annotations__
            arguments = getcallargs(f, *args, **kwargs).items()
            for param_name, param_value in arguments:
                if param_name != 'self':
                    data_type = annotations.get(param_name)
                    if not isinstance(param_value, data_type):
                        # TODO: Implement Custom Exceptions
                        # TODO: Validation against Defaults values
                        # TODO: Validate more complex Data Types like [string] or (float, int)
                        raise NotImplementedError

            # TODO: Implement Custom Exceptions
            try:
                # No need to use Try Except in specific functions just raise the specific exception
                return_value = f(*args, **kwargs)
            except CustomException as error:
                raise error
            except:
                raise NotImplementedError

            if 'return' in f.__annotations__:
                result_data_type = f.__annotations__['return']
                if not isinstance(return_value, result_data_type):
                    # TODO: Implement Custom Exceptions
                    raise NotImplementedError
            return return_value

        return decorated


class Testing:
    def __init__(self):
        pass

    @Decorators.force_type_hints
    def test(self, a: int, b: str, c: [float], d: dict, e: tuple = None, f: int = None) -> str:
        print(a, b, c, d, e, f)
        return 11


# test("33", {})
j = Testing()
j.test(123, "jj", ["kk"], {"ll": ""}, ("tt", "kk"), f=111)
