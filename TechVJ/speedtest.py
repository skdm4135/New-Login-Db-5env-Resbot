# plugins/speedtest.py
"""Telethon plugin: /speedtest
Place this file in your repo's plugins/ folder and import it in your bot startup
(e.g. `import plugins.speedtest`) so the handler is registered at import time.
"""

import asyncio
from time import time
import logging
from typing import Dict, Any

from speedtest import Speedtest
from telethon import events

logger = logging.getLogger(__name__)

# Adjust this import if your bot object is located elsewhere.
# Example: from .. import bot as Invix
try:
    from .. import bot as Invix
except Exception:
    # fallback if plugins is at project root (adjust if needed)
    try:
        from bot import bot as Invix  # common pattern
    except Exception:
        # As a last resort try to import top-level 'Invix' name
        from __main__ import Invix  # may fail; change to match your project
        # If none of these work, replace the import above with your project's bot object.

# If you have a global start time constant in main, adjust import path:
try:
    from main.__main__ import botStartTime
except Exception:
    # fallback default (0) if not available — this is optional
    botStartTime = time()

SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']


def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(int(seconds), 86400)
    if days:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    if hours:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    if minutes:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result


def get_readable_file_size(size_in_bytes) -> str:
    if size_in_bytes is None:
        return '0B'
    index = 0
    size = float(size_in_bytes)
    while size >= 1024 and index < len(SIZE_UNITS) - 1:
        size /= 1024
        index += 1
    return f'{round(size, 2)}{SIZE_UNITS[index]}'


def speed_convert(size: float, byte: bool = True) -> str:
    # speedtest gives bits/sec; if byte flag False we convert to bytes/sec
    if not byte:
        size = size / 8.0
    power = 2 ** 10
    zero = 0
    units = {0: "B/s", 1: "KB/s", 2: "MB/s", 3: "GB/s", 4: "TB/s"}
    while size > power and zero < max(units.keys()):
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


def run_speedtest_sync() -> Dict[str, Any]:
    """Blocking speedtest run; suitable for running in a thread executor."""
    st = Speedtest()
    st.get_best_server()
    st.download()
    # pre_allocate=False can help avoid memory issues on some hosts
    st.upload(pre_allocate=False)
    try:
        st.results.share()
    except Exception:
        # ignore share failures (some hosting blocks uploads)
        pass
    return st.results.dict()


# Optional: change this pattern to restrict usage (e.g. to SUDO_USERS).
# Example pattern matches "/speedtest" or "/speedtest <anything>"
@Invix.on(events.NewMessage(incoming=True, pattern=r'^/speedtest(?:\s|$)'))
async def speedtest_handler(event):
    # immediate acknowledgement
    progress = await event.reply("Running Speed Test — this can take 20–60 seconds...")

    loop = asyncio.get_running_loop()
    try:
        result = await loop.run_in_executor(None, run_speedtest_sync)
    except Exception as e:
        logger.exception("Speedtest failed")
        try:
            await progress.delete()
        except Exception:
            pass
        await event.reply(f"Speedtest failed: {e}")
        return

    # Parse results safely
    upload = speed_convert(result.get('upload', 0), False)
    download = speed_convert(result.get('download', 0), False)
    ping = result.get('ping', 'N/A')
    timestamp = result.get('timestamp', 'N/A')
    bytes_sent = int(result.get('bytes_sent', 0) or 0)
    bytes_received = int(result.get('bytes_received', 0) or 0)
    server = result.get('server', {}) or {}
    client = result.get('client', {}) or {}
    share_url = result.get('share')  # may be None or an image URL

    uptime_str = get_readable_time(time() - botStartTime) if botStartTime else "N/A"

    message = f'''
╭─《 🚀 SPEEDTEST INFO 》
├ <b>Upload:</b> <code>{upload}</code>
├ <b>Download:</b> <code>{download}</code>
├ <b>Ping:</b> <code>{ping} ms</code>
├ <b>Time:</b> <code>{timestamp}</code>
├ <b>Data Sent:</b> <code>{get_readable_file_size(bytes_sent)}</code>
╰ <b>Data Received:</b> <code>{get_readable_file_size(bytes_received)}</code>
╭─《 🌐 SPEEDTEST SERVER 》
├ <b>Name:</b> <code>{server.get('name','N/A')}</code>
├ <b>Country:</b> <code>{server.get('country','N/A')}, {server.get('cc','')}</code>
├ <b>Sponsor:</b> <code>{server.get('sponsor','N/A')}</code>
├ <b>Latency:</b> <code>{server.get('latency','N/A')}</code>
├ <b>Latitude:</b> <code>{server.get('lat','N/A')}</code>
╰ <b>Longitude:</b> <code>{server.get('lon','N/A')}</code>
╭─《 👤 CLIENT DETAILS 》
├ <b>IP Address:</b> <code>{client.get('ip','N/A')}</code>
├ <b>Latitude:</b> <code>{client.get('lat','N/A')}</code>
├ <b>Longitude:</b> <code>{client.get('lon','N/A')}</code>
├ <b>Country:</b> <code>{client.get('country','N/A')}</code>
├ <b>ISP:</b> <code>{client.get('isp','N/A')}</code>
╰ <b>ISP Rating:</b> <code>{client.get('isprating','N/A')}</code>
'''

    # Send reply (include share image if available)
    try:
        if share_url:
            await event.reply(message, file=share_url, parse_mode='html')
        else:
            await event.reply(message, parse_mode='html')
    except Exception:
        # fallback to plain text if something goes wrong with HTML/file
        await event.reply(message)
    finally:
        try:
            await progress.delete()
        except Exception:
            pass
