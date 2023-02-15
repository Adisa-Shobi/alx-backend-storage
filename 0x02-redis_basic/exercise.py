#!/usr/bin/env python3
'''
A Cache class that interfaces with redis
'''
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(mthd: Callable) -> Callable:
    '''
    wraps decorated function and stores the number
    of time method has been stored
    '''
    @wraps(mthd)
    def wrapped(self, *args, **kwargs):
        self._redis.incrby(mthd.__qualname__, 1)
        return mthd(self, *args, **kwargs)
    return wrapped


class Cache:
    '''
    Interface class for redis
    '''
    def __init__(self) -> None:
        '''
        class construction
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        takes a data argument and returns a string
        '''
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str,
            fn: Union[Callable, None] = None) -> Union[int, str, float]:
        '''
        Ensures get format is correct
        '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        '''
        Ensures get format is correct for strings
        '''
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        '''
        Ensures get format is correct for integers
        '''
        return self.get(key, int)
