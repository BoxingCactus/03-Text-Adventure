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

        print('n\n\ You are in the {name}' .format(name=c ['name']))
        print(c['desc'])


def check_input():
    '''Check Player Input'''
    response = input ('What would the mighty nerd (You.) like to do?')
    return response

def update(selection, game, current):
    '''Update our location, if possible etc.'''
    for e in game['rooms'][current]['exits']:
        if e['verb'] == response:
            current = e['target']
    return True

def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'
    quit = False
    while not quit:
        #render
        render()
        #check player input
        check_input()
        #update
        update()

    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()