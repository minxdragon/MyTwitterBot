import os
import argparse
import sys
import inspect
from friends import SakaFriends

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentparentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentparentdir)

from agent.Bot import Bot
from images.Header import RobotHeader

parser = argparse.ArgumentParser()

parser.add_argument("-t",
                    "--tweets",
                    type=int,
                    default=5,
                    help="number of tweets to write (default=5)")

parser.add_argument("-s",
                    "--show",
                    type=int,
                    default=10,
                    help="number of tweets to show to the user (default=10)")

parser.add_argument("-H",
                    "--hashtags",
                    type=int,
                    default=5,
                    help="number of hashtags (default=3)")
user_args = parser.parse_args()


print(RobotHeader)
SakaCorpus = os.path.join(parentparentdir, "data", "SakaCorpus.txt")
my_bot = Bot(corpus=SakaCorpus, friends=SakaFriends, commentary="SakaBot")
path = my_bot.curator_writer(num_tweets=user_args.tweets,
                             show_tweets=user_args.show,
                             num_hashtags=user_args.hashtags)

print("\n file can be found in {}".format(path))
