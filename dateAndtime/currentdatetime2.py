# using time.strftime()

from time import gmtime, strftime

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))