import aiohttp
import asyncio
import os
import sys
import traceback

from aiohttp import web


from . import tasks


async def main(request):
    try:
        tasks.task_two.delay()
        tasks.task_one.delay()
        # chain()
        print("tasks delayed")
        return web.Response(text="Hello", status=200)
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        return web.Response(status=500)


if __name__ == "__main__":  # pragma: no cover
    app = web.Application()
    app.router.add_get("/", main)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)
