from sys import exit

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        self.map = scene_map
        self.play()
    
    def play(self):
        nxt = self.map.currSceneName
        while True:
            print()
            print('-'*70)
            print('*'*25, nxt, '*'*25)
            nxt = self.map.currScene.enter()
            if nxt == 'win_scene':
                print('You won...')
                exit(0)
            self.map.nextScene(nxt)
            print('-'*70)
        

    
class DeathScene(Scene):
    def enter(self):
        print("You're Dead! Gothons mother ship is headed to Earth!")
        exit(0)

class CentralCorridorScene(Scene):
    def enter(self):
        print("Look, a scary Gothon in the central corridor of the space ship!")
        print("Fear is not an option, but you can choose to:")
        print("1. Scream at Gothon")
        print("2. Attack from behind")
        print("3. Do nothing")
        print("4. Tell a joke")
        choice = input(">")
        if choice != '4':
            print("Really? That's what you though to do!?... Gothon pounces on you with full wrath")
            return 'death_scene'
        else:
            print("Gothon never heard that before and ROFL! He passed out. Good Job!")
            print("Next stop: Laser Weapon Armory")
            return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("The Armory has a Neutron Bomb for the worst case")
        print("Choose your next step:")
        print("1. Bomb is scary, go back")
        print("2. Activate here")
        print("3. Take the bomb to next room")
        choice = input(">")
        if choice =='1':
            print("Gothon in the corridor is awake and attacks you")
            return 'death_scene'
        elif choice == '2':
            print("Bomb explodes killing you and the ship. Gothon mother ship survives")
            return 'death_scene'
        else:
            print("Good choice. Find a place to set the bomb ticking and excape")
            return 'bridge_scene'
        

class TheBridge(Scene):
    def enter(self):
        print("You reached the ship's central bridge. Choose what to do")
        print("1. Activate bomb and wait for firewors display")
        print("2. Go back and return the bomb")
        print("3. Activate and search for escape pods")
        choice = input(">")
        if choice == '1':
            print("Neutron bomb is not 4th of July. You melt")
            return 'death_scene'
        elif choice == '2':
            print("Armory is crawling with Gothons and they attack you")
            return 'death_scene'
        else:
            print("Enter the 4 key combination to activate the bomb")
            combo = input('>>>>')
            while combo != '5432':
                print("Incorrect. Try again. Fast!")
                combo = input('>>>>')
            print('Neutron bomb active! Qucikly go find escape pods')
            return 'escape_pod_scene'

class EscapePod(Scene):
    def enter(self):
        print("You have almost made it! There are two pods:")
        print("1. PodA has an abandoned suit in it")
        print("2. PodB seems to be older and unused")
        print("Enter one pod, qucikly!")
        choice = input(">")
        if choice == '1':
            print("Someone abandoned it for a reason. Its controls are haywire. Too late. Neutron Implosion!")
            return 'death_scene'
        else:
            print("Shown some courage to enter the 'Pod Not Taken'. Though old, it works and you hyper-jump near to earth")
            print("You reach earth and inform of Gothons' attack. Earth attacks with full force")
            return 'win_scene'

class Map(object):
    def __init__(self,start_scene):
        self.currSceneName = start_scene
        self.DeathScene = DeathScene()
        self.CentralCorridorScene = CentralCorridorScene()
        self.LaserWeaponArmory = LaserWeaponArmory()
        self.TheBridge = TheBridge()
        self.EscapePod = EscapePod()
        self.currScene = None
        self.openingScene()
    
    def nextScene(self, scene_name):
        if scene_name == 'death_scene':
            self.currScene = self.DeathScene
        elif scene_name == 'laser_weapon_armory':
            self.currScene = self.LaserWeaponArmory
        elif scene_name == 'bridge_scene':
            self.currScene = self.TheBridge
        elif scene_name == 'escape_pod_scene':
            self.currScene = self.EscapePod
        elif scene_name == 'central_corridor_scene':
            self.currScene = self.CentralCorridorScene
        elif scene_name == 'win_scene':
            self.currScene == self.winScene

    
    def openingScene(self):
        self.currScene = self.CentralCorridorScene


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()