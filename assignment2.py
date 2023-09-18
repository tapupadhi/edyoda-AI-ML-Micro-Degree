class Dog:
    def __init__(self, name, age, coat_color):
        self.__name = name
        self.__age = age
        self.__coat_color = coat_color

    def description(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")

    def get_info(self):
        print(f"Coat Color: {self.__coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        self.__life_expectancy = '13 – 16 years'
        self.__temperament = ['Clownish', 'Intelligent', 'Athletic', 'Stubborn', 'Energetic', 'Fearless', 'Vocal']
        self.__mass = '6 – 8 kg(Adult)'
        self.__height = '25 – 38 cm(Adult, At the withers)'

    def get_info(self):
        print("About:")
        print("------")
        super().get_info()
        print(f"Life Expectancy: {self.__life_expectancy}")
        print(f"Temperament: {self.__temperament}")
        print(f"Mass: {self.__mass}")
        print(f"Height: {self.__height}")
        print()

    def description(self):
        print("Description:")
        print("------------")
        super().description()
        print("Due to their working nature, Jack Russell terriers remain much as they were some 200 years ago.\nThey "
              "are sturdy, tough, and tenacious, measuring between 25–38 cm (10–15 in) at the withers, and weigh 6–8 "
              "kg (14–18 lb).\n[citation needed] The body length must be in proportion to the height, and the dog "
              "should present a compact, balanced image.\nPredominantly white in coloration (more than 51%) with black "
              "and/or brown and/or tan markings, they exhibit either a smooth, rough or a combination of both which "
              "is known as a broken coat.\nA broken-coated dog may have longer hair on the tail or face than that "
              "which is seen on a smooth-coated dog.\n\n"


              "An example of a rough-coated Jack Russell terrier The head should be of moderate width at the ears, "
              "narrowing to the eyes, and slightly flat between the ears.\nThere should be a defined but not "
              "over-pronounced stop at the end of the muzzle where it meets the head, and a black nose.\nThe jaw "
              "should be powerful and well boned with a scissor bite and straight teeth.\nThe eyes are almond shaped "
              "and dark coloured and should be full of life and intelligence.\nSmall V-shaped ears of moderate "
              "thickness are carried forward on the head.\n[citation needed] When the dog is alert, the tip of the V "
              "should not extend past the outer corner of the eyes.\nThe tail is set high and in the past was docked "
              "to approximately 10 cm (5 in) in order to provide a sufficient hand-hold for gripping the terrier.\n\n"

              "The Jack Russell should always appear balanced and alert.\nThe red fox is the traditional quarry of "
              "the Jack Russell terrier, so the working Jack Russell must be small enough to pursue it.\nRed foxes "
              "vary in size, but across the world, they average from 6–8 kg (13–17 lb) in weight and have an average "
              "chest size of 30–36 cm (12–14 in) at the widest part")
        print()


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        self.__life_expectancy = '8 – 10 years'
        self.__temperament = ['Gregarious', 'Docile', 'Willful', 'Friendly']
        self.__mass = 'Female: 18–23 kg, Male: 23–25 kg'
        self.__height = 'Female: 31–40 cm, Male: 31–40 cm'

    def get_info(self):
        print("About:")
        print("------")
        super().get_info()
        print(f"Life Expectancy: {self.__life_expectancy}")
        print(f"Temperament: {self.__temperament}")
        print(f"Mass: {self.__mass}")
        print(f"Height: {self.__height}")
        print()

    def description(self):
        print("Description:")
        print("------------")
        super().description()
        print("Bulldogs have characteristically wide heads and shoulders along with a pronounced mandibular "
              "prognathism.\nThere are generally thick folds of skin on the brow; round, black, wide-set eyes; a short "
              "muzzle with characteristic folds called a rope or nose roll above the nose; hanging skin under the "
              "neck; drooping lips and pointed teeth, and an under-bite with an upturned jaw.\nThe coat is short, flat,"
              "and sleek with colours of red, fawn, white, brindle, and piebald.\nThey have short tails that can "
              "either hang down straight or be tucked in a coiled \"corkscrew\" into a tail pocket.\nIn the United "
              "Kingdom, the breed standards are 55 lb (25 kg) for a male and 50 lb (23 kg) for a female.\nIn the "
              "United States, the standard calls for a smaller dog — a typical mature male weighs 50 lb (23 kg), "
              "while mature females weigh about 40 lb (18 kg).")


print("***************************************************************************************")
print("                                Jack-Russell-Terrier                                   ")
print("***************************************************************************************")
jrt = JackRussellTerrier("JackRussellTerrier", 5, "Predominantly White")
jrt.get_info()
jrt.description()

print()

print("***************************************************************************************")
print("                                     Bull Dog                                          ")
print("***************************************************************************************")
bd = Bulldog("BullDog", 4, "Black")
bd.get_info()
bd.description()
