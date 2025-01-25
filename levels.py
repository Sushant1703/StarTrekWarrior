class Levels:
    def __init__(self):
        self.level_data = self.define_levels()

    def define_levels(self):
        return {
            1: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},  
                    {'rect': (150, 450, 100, 20)},
                    {'rect': (300, 350, 100, 20)},
                    {'rect': (450, 250, 100, 20)},
                    {'rect': (600, 150, 100, 20)},
                ],
                'enemies': [
                    {'x': 150, 'y': 410, 'type': 'patrol'},
                    {'x': 300, 'y': 310, 'type': 'patrol'},
                    {'x': 450, 'y': 210, 'type': 'chaser'},
                ],
                'coins': [
                    (180, 420),
                    (330, 320),
                    (480, 220),
                    (630, 120),
                ],
                'background': r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png",
            },
            2: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},  
                    {'rect': (100, 450, 100, 20)},
                    {'rect': (250, 350, 100, 20)},
                    {'rect': (400, 250, 100, 20)},
                    {'rect': (550, 150, 100, 20)},
                    {'rect': (700, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 100, 'y': 410, 'type': 'chaser'},
                    {'x': 250, 'y': 310, 'type': 'patrol'},
                    {'x': 400, 'y': 210, 'type': 'patrol'},
                    {'x': 550, 'y': 110, 'type': 'chaser'},
                ],
                'coins': [
                    (130, 420),
                    (280, 320),
                    (430, 220),
                    (580, 120),
                    (730, 20),
                ],
                'background': r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png",
            },
            3: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},  
                    {'rect': (200, 450, 100, 20)},
                    {'rect': (350, 350, 100, 20)},
                    {'rect': (500, 250, 100, 20)},
                    {'rect': (650, 150, 100, 20)},
                    {'rect': (300, 150, 100, 20)},
                ],
                'enemies': [
                    {'x': 200, 'y': 410, 'type': 'patrol'},
                    {'x': 350, 'y': 310, 'type': 'chaser'},
                    {'x': 500, 'y': 210, 'type': 'patrol'},
                    {'x': 650, 'y': 110, 'type': 'chaser'},
                ],
                'coins': [
                    (230, 420),
                    (380, 320),
                    (530, 220),
                    (680, 120),
                    (330, 140),
                ],
                'background': r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png",
            },
           
            4: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (150, 450, 100, 20)},
                    {'rect': (300, 350, 100, 20)},
                    {'rect': (450, 250, 100, 20)},
                    {'rect': (600, 350, 100, 20)},
                    {'rect': (750, 250, 100, 20)},
                ],
                'enemies': [
                    {'x': 150, 'y': 410, 'type': 'patrol'},
                    {'x': 300, 'y': 310, 'type': 'chaser'},
                    {'x': 450, 'y': 210, 'type': 'patrol'},
                    {'x': 600, 'y': 310, 'type': 'chaser'},
                    {'x': 750, 'y': 210, 'type': 'patrol'},
                ],
                'coins': [
                    (180, 420),
                    (330, 320),
                    (480, 220),
                    (630, 320),
                    (780, 220),
                ],
                'background': r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png",
            },
            5: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},  
                    {'rect': (100, 450, 100, 20)},
                    {'rect': (250, 350, 100, 20)},
                    {'rect': (400, 250, 100, 20)},
                    {'rect': (550, 350, 100, 20)},
                    {'rect': (700, 250, 100, 20)},
                ],
                'enemies': [
                    {'x': 100, 'y': 410, 'type': 'chaser'},
                    {'x': 250, 'y': 310, 'type': 'patrol'},
                    {'x': 400, 'y': 210, 'type': 'chaser'},
                    {'x': 550, 'y': 310, 'type': 'patrol'},
                    {'x': 700, 'y': 210, 'type': 'chaser'},
                ],
                'coins': [
                    (130, 420),
                    (280, 320),
                    (430, 220),
                    (580, 320),
                    (730, 220),
                ],
                'background': r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png",
            },

            6: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},  
                    {'rect': (150, 450, 100, 20)},
                    {'rect': (300, 350, 100, 20)},
                    {'rect': (450, 250, 100, 20)},
                    {'rect': (600, 350, 100, 20)},
                    {'rect': (750, 250, 100, 20)},
                    {'rect': (300, 150, 100, 20)},
                ],
                'enemies': [
                    {'x': 150, 'y': 410, 'type': 'patrol'},
                    {'x': 300, 'y': 310, 'type': 'chaser'},
                    {'x': 450, 'y': 210, 'type': 'patrol'},
                    {'x': 600, 'y': 310, 'type': 'chaser'},
                    {'x': 750, 'y': 210, 'type': 'patrol'},
                    {'x': 300, 'y': 110, 'type': 'chaser'},
                ],
                'coins': [
                    (180, 420),
                    (330, 320),
                    (480, 220),
                    (630, 320),
                    (780, 220),
                    (330, 140),
                ],
                'background': r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png",
            },
            
        }

    def get_level(self, level_num):
        return self.level_data.get(level_num, None)
