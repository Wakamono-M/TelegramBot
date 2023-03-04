#как тестинг файл
class bot():
 
    def __init__(self, aura, level, time):
        
        self.kind = aura
        self.height = level
        self.legs = time
    

if __name__ == "__main__":
    wy = bot("чтото там", 5, 4)
    print(wy.kind)
    print(wy.height)
    print(wy.legs)
    
