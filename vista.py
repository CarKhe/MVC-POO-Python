from controller import Controller as Ctrl


class Main:
    def __init__(self):
        obj = Ctrl()
        obj.buscar_valores()
        del obj
        
    
    
Main()