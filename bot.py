import os
import discord
from dotenv import load_dotenv
from data import (
    get_driver_standings,
    get_constructor_standings,
    get_race_season,
    get_race_schedule,
    get_race_results,
    get_teams,
    get_help,
)


class MyClient(discord.Client):
    # Terminal log in message.
    async def on_ready(self):
        print(f"Logged on as {self.user}.")

    # Commands
    async def on_message(self, message):
        # Prevents response to own message.
        if message.author == self.user:
            return

        # In response to "hello".
        if (message.content).lower().startswith("$hello"):
            await message.channel.send(
                "hello! I can help with F1 stats. Type '$help' for command specifications."
            )

        # Sends driver's championship.
        if (message.content).lower().startswith("$driver"):
            if "-" not in message.content:
                standings = get_driver_standings()
                await message.channel.send(standings)
            if "-" in message.content:
                try:
                    _, year = message.content.split("-")
                    standings = get_driver_standings(prev=year.strip())
                    await message.channel.send(standings)
                except:
                    await message.channel.send(
                        "Something went wrong! Check '$help' for command specifications."
                    )

        # Sends constructor's championship.
        if (message.content).lower().startswith("$constructor"):
            if "-" not in message.content:
                standings = get_constructor_standings()
                await message.channel.send(standings)
            if "-" in message.content:
                try:
                    _, year = message.content.split("-")
                    standings = get_constructor_standings(prev=year.strip())
                    await message.channel.send(standings)
                except:
                    await message.channel.send(
                        "Something went wrong! Check '$help' for command specifications."
                    )

        if (message.content).lower().startswith("$season"):
            if "-" not in message.content:
                season = get_race_season()
                await message.channel.send(season)
            if "-" in message.content:
                try:
                    _, year = message.content.split("-")
                    season = get_race_season(prev=year.strip())
                    await message.channel.send(season)
                except:
                    await message.channel.send(
                        "Something went wrong! Check '$help' for command specifications."
                    )

        if (message.content).lower().startswith("$schedule"):
            if "-" not in message.content:
                schedule = get_race_schedule()
                await message.channel.send(schedule)
            if "-" in message.content:
                try:
                    _, round = message.content.split("-")
                    schedule = get_race_schedule(round=round.strip())
                    await message.channel.send(schedule)
                except:
                    await message.channel.send(
                        "Something went wrong! Check '$help' for command specifications."
                    )

        if (message.content).lower().startswith("$result"):
            if "-" not in message.content:
                results = get_race_results()
                await message.channel.send(results)
            if "-" in message.content:
                try:
                    _, results = message.content.split("-")
                    results = get_race_results(prev=results.strip())
                    await message.channel.send(results)
                except:
                    await message.channel.send(
                        "Something went wrong! Check '$help' for command specifications."
                    )

        if (message.content).lower().startswith("$team"):
            teams = get_teams()
            await message.channel.send(teams)

        if (message.content).lower().startswith("$help"):
            help = get_help()
            await message.channel.send(help)


# System
load_dotenv()
intents = discord.Intents().all()
client = MyClient(intents=intents)
client.run(os.getenv("TOKEN"))
