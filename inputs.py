import argparse

parser = argparse.ArgumentParser(description='This work in progress is a Tinder bot which utilizes a neural network to rate the conventional beauty of Tinder photos and swipes accordingly.')
parser.add_argument("-p", "--profile", default=None, type=str, help="Selected profile")
parser.add_argument("-l", "--like", default=50, type=int, help="Number of likes allowed")
parser.add_argument("-b", "--batch", default=1, type=int, help="Number of request batches to swipe through")
parser.add_argument("-r", "--rating", default=3.5, type=int, help="Minimum beauty value (1-5) for the like. Default: 3.5. Set 0 to like all")
parser.add_argument("-m", "--model", default="model2.h5", type=str, help="Model selector Default: model2.h5")

args = parser.parse_args()