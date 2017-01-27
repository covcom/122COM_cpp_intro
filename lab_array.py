import sys

def main():
    userinputs = []

    while len(userinputs) < 5:                    # read in the 5 integers
        try:
            ui = int(input('Enter integer:'))
            userinputs.append(ui)
        except ValueError:                        # handle any non-integers
            print('Not an integer')
        
    for i in range(len(userinputs)-1, -1, -1):    # print them back out in reverse order
        print( 'number {} is {}'.format( i+1, userinputs[i] ) )

if __name__ == '__main__':
    sys.exit(main())