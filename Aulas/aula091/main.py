def master():
    def slave():
        print('Oi')

    return slave


var = master()

var