# TechVJ/speedtest.py

from telethon import events
import asyncio
from time import time
from speedtest import Speedtest
from bot import Bot             # import your bot client


def speed_convert(size, byte=True):
    if not byte:
        size = size / 8
    power = 2 ** 10
    zero = 0
    units = {0: "B/s", 1: "KB/s", 2: "MB/s", 3: "GB/s", 4: "TB/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


def get_readable_file_size(size_in_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    index = 0
    size = float(size_in_bytes)
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{round(size,2)}{units[index]}"


async def run_speedtest():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, run_speedtest_sync)


def run_speedtest_sync():
    st = Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    try:
        st.results.share()
    except:
        pass
    return st.results.dict()


@Bot.on(events.NewMessage(pattern="/speedtest"))
async def speedtest_handler(event):

    msg = await event.reply("Running speedtest... please wait 30–60 seconds.")

    result = await run_speedtest()

    upload = speed_convert(result['upload'], False)
    download = speed_convert(result['download'], False)
    ping = result['ping']
    bytes_sent = get_readable_file_size(int(result['bytes_sent']))
    bytes_received = get_readable_file_size(int(result['bytes_received']))

    server = result['server']
    client = result['client']

    share_url = result.get("share")

    text = f"""
<b>🚀 SPEEDTEST RESULT</b>

<b>Download:</b> <code>{download}</code>
<b>Upload:</b> <code>{upload}</code>
<b>Ping:</b> <code>{ping} ms</code>

<b>Server:</b> {server['name']} ({server['country']})
<b>Sponsor:</b> {server['sponsor']}

<b>Client ISP:</b> {client['isp']}
<b>IP:</b> {client['ip']}
"""

    if share_url:
        await event.reply(text, file=share_url, parse_mode="html")
    else:
        await event.reply(text, parse_mode="html")

    await msg.delete()
