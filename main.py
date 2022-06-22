from os import makedirs, listdir
from os.path import isdir
from shutil import move
from sys import exit


class PerkOrganizer():
    def __init__(self, image_dir, output_dir):
        self.image_dir = image_dir
        self.output_dir = output_dir
        self.prefix = "iconPerks_"
        self.suffix = ".png"

        self.perk_list = {
            "Ash": ["buckleUp", "flipFlop", "mettleOfMan"],
            "Aurora": ["appraisal", "coupDeGrace", "deception", "Hoarder", "Oppression", "powerStruggle"],
            "Cannibal": ["BBQAndChili", "franklinsLoss", "knockOut"],
            "Comet": ["FastTrack", "HexCrowdControl", "NoWayOut", "Self-Preservation", "SmashHit", "Starstruck"],
            "DLC2": ["decisiveStrike", "dyingLight", "objectOfObsession", "playWithYourFood", "saveTheBestForLast", "soleSurvivor"],
            "DLC3": ["aceInTheHole", "devourHope", "openHanded", "ruin", "theThirdSeal", "thrillOfTheHunt", "upTheAnte"],
            "DLC4": ["alert", "generatorOvercharge", "lithe", "monitorAndAbuse", "overwhelmingPresence", "technician"],
            "DLC5": ["BeastOfPrey", "DeadHard", "HuntressLullaby", "NoMither", "TerritorialImperative", "WereGonnaLiveForever"],
            "Eclipse": ["BiteTheBullet", "blastMine", "Counterforce", "eruption", "Flashbang", "hysteria", "lethalPursuer", "Resurgence", "RookieSpirit"],
            "England": ["bloodWarden", "fireUp", "pharmacy", "rememberMe", "vigil", "wakeUp"],
            "Finland": ["detectivesHunch", "hangmansTrick", "makeYourChoice", "stakeOut", "surveillance", "tenacity"],
            "Gemini": ["Deadlock", "HexPlaything", "ScourgeHookGiftOfPain"],
            "Guam": ["bamboozle", "coulrophobia", "popGoesTheWeasel"],
            "Haiti": ["autodidact", "deliverance", "diversion", "hatred", "hauntedGround", "spiritFury"],
            "Hubble": ["BoonCircleOfHealing", "BoonShadowStep", "Clairvoyance"],
            "Kate": ["boilOver", "danceWithMe", "windowsOfOpportunity"],
            "Kenya": ["aftercare", "breakdown", "discordance", "distortion", "ironMaiden", "madGrit"],
            "Kepler": ["callOfBrine", "darkTheory", "empathicConnection", "floodOfRage", "mercilessStorm", "parentalGuidance"],
            "L4D": ["borrowedTime", "leftBehind", "unbreakable"],
            "Mali": ["corruptIntervention", "darkDevotion", "headOn", "infectiousFright", "poised", "solidarity"],
            "Meteor": ["BoonDestroyer", "DarknessRevelated", "Dissolution", "InnerFocus", "Overzealous", "ResidualManifest", "SepticTouch"],
            "Oman": ["furtiveChase", "imAllEars", "thrillingTremors"],
            "Qatar": ["babySitter", "betterTogether", "camaraderie", "cruelConfinement", "fixated", "guardian", "innerStrength", "mindBreaker", "pushThroughIt", "secondWind", "situationalAwareness", "surge", "survivalInstincts"],
            "Sweden": ["anyMeansNecessary", "bloodEcho", "breakout", "luckyBreak", "nemesis", "zanshinTactics"],
            "Ukraine": ["deadManSwitch", "forThePeople", "gearHead", "hexRetribution", "offTheRecord", "redHerring"],
            "Wales": ["bloodPact", "deathbound", "forcedPenance", "repressedAlliance", "soulGuard", "trailOfTorment"],
            "Yemen": ["builtToLast", "desperateMeasures", "dragonsGrip", "hexBloodFavor", "hexUndying", "visionary"]
        }

        self.perk_list_2 = {
            "Ion": ["BoonExponential", "CorrectiveAction", "grimEmbrace", "hexPentimento", "Overcome", "painResonance"]
        }


    def generateDirs(self):
        for dir in self.perk_list.keys():
            if not isdir(dir):
                try:
                    makedirs(f"./{self.output_dir}/{dir}")
                except Exception as e:
                    pass

        for dir in self.perk_list_2.keys():
            if not isdir(dir):
                try:
                    makedirs(f"./{self.output_dir}/{dir}")
                except Exception as e:
                    pass


    def moveImages(self):
        for dir, perks in self.perk_list.items():
            for index in range(len(perks)):
                try:
                    move(f"{self.image_dir + self.prefix + perks[index]}.png", f"{self.output_dir + dir}/{self.prefix + perks[index]}.png")
                except Exception as e:
                    pass

        for dir, perks in self.perk_list_2.items():
            for index in range(len(perks)):
                try:
                    move(f"{self.image_dir + 'T_iconPerks_' + perks[index]}.png", f"{self.output_dir + dir}/{'T_iconPerks_' + perks[index]}.png")
                except Exception as e:
                    pass

        file_names = listdir(self.image_dir)

        for file_name in file_names:
            move(self.image_dir + file_name, self.output_dir)


    def main(self):
        self.generateDirs()
        self.moveImages()


if __name__ == "__main__":
    PerkOrganizer("./images/", "./output/").main()
else:
    input("Error!\nPress ENTER to continue...")
    exit()