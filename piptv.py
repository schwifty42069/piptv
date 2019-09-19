import requests
from bs4 import BeautifulSoup as Soup
import vlc
import time
import os
from threading import Thread
import platform


class CableBox(Thread):
    def __init__(self):
        super().__init__()
        self.channel_dict = {'a&e': 'http://ustvgo.tv/ae-networks-live-streaming-free/',
                             'abc': 'http://ustvgo.tv/abc-live-streaming-free/',
                             'amc': 'http://ustvgo.tv/amc-live/',
                             'animal planet': 'http://ustvgo.tv/animal-planet-live/',
                             'bbc america': 'http://ustvgo.tv/bbc-america-live/',
                             'bet': 'http://ustvgo.tv/bet/',
                             'boomerang': 'http://ustvgo.tv/boomerang/',
                             'bravo': 'http://ustvgo.tv/bravo-channel-live-free/',
                             'cartoon network': 'http://ustvgo.tv/cartoon-network-live-streaming-free/',
                             'cbs': 'http://ustvgo.tv/cbs-live-streaming-free/',
                             'cmt': 'http://ustvgo.tv/cmt/',
                             'cnbc': 'http://ustvgo.tv/cnbc-live-streaming-free/',
                             'cnn': 'http://ustvgo.tv/cnn-live-streaming-free/',
                             'comedy central': 'http://ustvgo.tv/comedy-central-live-free/',
                             'destination america': 'http://ustvgo.tv/destination-america/',
                             'discovery channel': 'http://ustvgo.tv/discovery-channel-live/',
                             'disney channel': 'http://ustvgo.tv/disney-channel-live-streaming-free/',
                             'disneyjr': 'http://ustvgo.tv/disneyjr/',
                             'disneyxd': 'http://ustvgo.tv/disneyxd/',
                             'diy': 'http://ustvgo.tv/diy/',
                             'e!': 'http://ustvgo.tv/e/',
                             'espn': 'http://ustvgo.tv/espn-live/',
                             'espn2': 'http://ustvgo.tv/espn2/',
                             'food network': 'http://ustvgo.tv/food-network-live-free/',
                             'fox': 'http://ustvgo.tv/fox-hd-live-streaming/',
                             'fox business': 'http://ustvgo.tv/fox-business-live-streaming-free/',
                             'fox news': 'http://ustvgo.tv/fox-news-live-streaming-free/',
                             'fox sports 1': 'http://ustvgo.tv/fox-sports-1/',
                             'fox sports 2': 'http://ustvgo.tv/fox-sports-2/',
                             'freeform': 'http://ustvgo.tv/freeform-channel-live-free/',
                             'fx': 'http://ustvgo.tv/fx-channel-live/',
                             'fxm': 'http://ustvgo.tv/fxm/',
                             'fxx': 'http://ustvgo.tv/fxx/',
                             'golf channel': 'http://ustvgo.tv/golf-channel-live-free/',
                             'gsn': 'http://ustvgo.tv/gsn/',
                             'hallmark channel': 'http://ustvgo.tv/hallmark-channel-live-streaming-free/',
                             'hallmark movies & mysteries': 'http://ustvgo.tv/hallmark-movies-mysteries-live-streaming-free/',
                             'hbo': 'http://ustvgo.tv/hbo/',
                             'hgtv': 'http://ustvgo.tv/hgtv-live-streaming-free/',
                             'history channel': 'http://ustvgo.tv/history-channel-live/',
                             'hln': 'http://ustvgo.tv/hln/',
                             'investigation discovery': 'http://ustvgo.tv/investigation-discovery-live-streaming-free/',
                             'lifetime': 'http://ustvgo.tv/lifetime-channel-live/',
                             'lifetime movies': 'http://ustvgo.tv/lifetime-movies/',
                             'mlb network': 'http://ustvgo.tv/mlb-network/',
                             'motortrend': 'http://ustvgo.tv/motortrend/',
                             'msnbc live streaming free': 'http://ustvgo.tv/msnbc-live-streaming-free/',
                             'mtv': 'http://ustvgo.tv/mtv/',
                             'nat geo wild': 'http://ustvgo.tv/nat-geo-wild-live/',
                             'national geographic': 'http://ustvgo.tv/national-geographic-live/',
                             'nba tv': 'http://ustvgo.tv/nba-tv/',
                             'nbc': 'http://ustvgo.tv/nbc/',
                             'nbc sports': 'http://ustvgo.tv/nbc-sports/',
                             'nfl network': 'http://ustvgo.tv/nfl-network-live-free/',
                             'nickelodeon': 'http://ustvgo.tv/nickelodeon-live-streaming-free/',
                             'nicktoons': 'http://ustvgo.tv/nicktoons/',
                             'own': 'http://ustvgo.tv/own/',
                             'oxygen': 'http://ustvgo.tv/oxygen/',
                             'paramount network': 'http://ustvgo.tv/paramount-network/',
                             'pbs': 'http://ustvgo.tv/pbs-live/',
                             'pop': 'http://ustvgo.tv/pop/',
                             'science': 'http://ustvgo.tv/science/',
                             'showtime': 'http://ustvgo.tv/showtime/',
                             'starz': 'http://ustvgo.tv/starz-channel-live/',
                             'sundance tv': 'http://ustvgo.tv/sundance-tv/',
                             'syfy': 'http://ustvgo.tv/syfy-channel-live/',
                             'tbs': 'http://ustvgo.tv/tbs-channel-live-free/',
                             'tcm': 'http://ustvgo.tv/tcm/',
                             'telemundo': 'http://ustvgo.tv/telemundo/',
                             'tennis channel': 'http://ustvgo.tv/tennis-channel-live-free/',
                             'the cw': 'http://ustvgo.tv/the-cw-live-streaming-free/',
                             'the weather channel': 'http://ustvgo.tv/the-weather-channel-live-streaming-free/',
                             'tlc': 'http://ustvgo.tv/tlc-live-free/',
                             'tnt': 'http://ustvgo.tv/tnt/',
                             'travel': 'http://ustvgo.tv/travel-channel-live-free/',
                             'trutv': 'http://ustvgo.tv/trutv/',
                             'tv land': 'http://ustvgo.tv/tv-land-live-free/',
                             'univision': 'http://ustvgo.tv/univision/',
                             'usa network': 'http://ustvgo.tv/usa-network-live/',
                             'vh1': 'http://ustvgo.tv/vh1/',
                             'we tv': 'http://ustvgo.tv/we-tv/',
                             'wwe network': 'http://ustvgo.tv/wwe-network/'}
        instance_args = "--verbose=-1" + "--vout=opengl"
        if platform.system() == "Windows":
            instance_args += "--plugins-path=C:\Program Files\VideoLAN\VLC\plugins"
        self.instance = vlc.Instance(instance_args)
        self.player = vlc.MediaPlayer(self.instance)
        self.player.set_fullscreen(True)
        self.daemon = False

    def get_hls_hotlink(self, channel):
        try:
            bsoup = Soup(requests.get(self.channel_dict[channel.lower()]).text, 'html.parser')
            return bsoup.findAll("script")[15].next_element.split(" file: ")[1].split(',')[0].strip("\'")
        except KeyError:
            print("\n\033[1;31;49mInvalid channel name!\n")
            return 1

    def tune_to_channel(self, channel):
        hotlink = self.get_hls_hotlink(channel)
        if hotlink == 1:
            return
        self.player.set_mrl(hotlink)
        self.run()

    def run(self):
        self.player.play()
        while True:
            try:
                time.sleep(0.1)
                os.system('cls' if os.name == 'nt' else 'clear')
            except KeyboardInterrupt:
                print("\n\033[1;31;49mStopping..\n")
                self.player.stop()
                break


def main():
    while True:
        stb = CableBox()
        print("\n\033[1;36;49mTo list channels, type list.\n"
              "To tune to a channel, type its name.\n"
              "To stop playback, hit CTRL+C.\n"
              "To quit, type quit.\n\n")
        command = input("\033[1;37;49m>> ")
        if command == "stop":
            stb.player.stop()
        elif command == "list":
            print("\n\033[1;32;49mCHANNELS:\n")
            for key in stb.channel_dict.keys():
                print("\033[1;32;49m" + key)
        elif command == "quit":
            return
        elif command == "set hotlink":
            stb.player.set_mrl(input("\nhotlink: "))
            stb.run()
        else:
            print("\n\033[1;33;49mTrying to tune to {}...\n".format(command))
            stb.tune_to_channel(command)


if __name__ == "__main__":
    main()
