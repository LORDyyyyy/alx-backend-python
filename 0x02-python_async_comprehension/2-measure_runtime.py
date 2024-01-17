#!/usr/bin/env python3
""" Async Comprehension """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ doc """
    start = asyncio.get_event_loop().time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    return (asyncio.get_event_loop().time() - start)
