import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)



def render(game, current):
        '''Display the current room, moves and points'''
        r = game['rooms']
        c= r[current]


def check_input():
    '''Check Player Input'''
    response = input ('What would the mighty nerd (You.) like to do?')
    return response

def update(selectiom, game, current):
    '''Update our location, if possible etc.'''
    return True

def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'


    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()