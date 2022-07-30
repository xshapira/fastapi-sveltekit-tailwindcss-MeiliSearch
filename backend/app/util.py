import asyncio
from functools import wraps
from typing import Generator
from typing import Tuple


def chunkify(lst: list, size: int) -> Tuple[Generator[list, None, None], int]:
    """Chunks lst into unique subsets of length chunk_size"""
    chunks = sum(not i % size for i in range(len(lst)))
    return (lst[i::chunks] for i in range(chunks)), chunks


def coroutine(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


def unique_list(flatrate: list, free: list) -> list:
    return [provider for provider in free if provider not in flatrate] + flatrate
