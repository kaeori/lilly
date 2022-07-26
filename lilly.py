from typing import Any, Callable


class App:
    """
    Implements composable functions.
    """
    
    def __init__(self, callable: Callable):
        """
        Creates a composable from a given callable.
        """

        self.callable = callable

    
    def __call__(self, x: Any) -> Any:  
        """
        Calls the composable (i.e. the internal callable).
        """

        return self.callable(x)

    
    def __or__(self, other: App) -> App:
        """
        Implements the composition/pipe operator, and 
        returns a new composable.
        """

        return App(
            lambda x: other.callable(self.callable(x))
        )


Composable = App
