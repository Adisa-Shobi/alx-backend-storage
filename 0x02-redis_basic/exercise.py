#!/usr/bin/env python3
'''
A Cache class that interfaces with redis
'''
import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        takes a data argument and returns a string
        '''
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
