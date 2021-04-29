

import pygame
from data import *
from features import *
from mapClasses import *
from TileMap import *
from keyboards import *
from random import randrange

def init_game(gd, gc):
    '''
    :type gc: GameController
    :type gd: GameData
    :return:
    '''
    pygame.init()
    pygame.display.set_caption('NPC')


    # load all keyboard managers
    # TODO: add other possible Keyboard_managers
    gc.add_keyboard_manager(InGameKeyboardManager.ID, InGameKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InMenuKeyboardManager.ID, InMenuKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InStartMenuKeyboardManager.ID, InStartMenuKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InTextKeyboardManager.ID, InTextKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InTalkingMenuKeyboardManager.ID, InTalkingMenuKeyboardManager(gc, gd))
    gc.set_keyboard_manager(InGameKeyboardManager.ID)

    #load menus
    gd.add_overlay("testing_menu", Overlay(gc, gd, "testing_menu", 700, 500, Spritesheet("assets/menu_images/testing_menu.png", 200, 100)))
    gd.add_menu("testing_menu", Menu(gc, gd, "testing_menu", ["hi", "hello", "yo"], True, "testing_menu"))

    gd.add_overlay("menu2", Overlay(gc, gd, "menu2", 200, 500, Spritesheet("assets/menu_images/testing_menu.png", 200, 100)))
    gd.add_menu("menu2", Menu(gc, gd, "menu2", ["Clayton", "Adam", "Jim"], True, "menu2"))

    gd.add_overlay("start_menu", Overlay(gc, gd, "start_menu", 600, 200, Spritesheet("assets/menu_images/start_menu.png", 150, 400)))
    gd.add_menu("start_menu", Menu(gc, gd, "start_menu", ["Pokedex", "Pokemon", "Bag", "PokeNav", "Profile", "Save", "Options" ], True, "start_menu"))

    gd.add_overlay("top_bar", Overlay(gc, gd, "top_bar", 100, 100, Spritesheet("assets/menu_images/top_bar.png", 700, 100)))

    gd.add_overlay("text_box", Overlay(gc, gd, "text_box", 250, 550, Spritesheet("assets/menu_images/text_box.png", 500, 150)))

    gd.add_menu("character_interact_menu", Menu(gc, gd, "character_interact_menu", ["Talk", "Give Gift"], True, "text_box", offset_x=150))

    # add the player to the game
    gd.add_player("Player", Player(2, 3, 2, 3, 32, 40, Spritesheet("assets/player/player_sheet.png", 32, 40), "Bug", gc, gd))
    gd.player["Player"].activate_timer()

    # run functions that initiate all rooms
    init_room_1(gc, gd)
    init_room_2(gc, gd)
    init_room_3(gc, gd)
    init_room_4(gc, gd)

def init_room_1(gc, gd):
    # room #1

    # add the room #1, generate the grid, and add the background and doors
    gd.add_room("room1", Room2("room1", 1, 2, 6, 6, 1, 1, 6, 6, gc, gd))
    gd.room_list["room1"].add_room_plot("room1_1_1", Plot("room4", 1, 1, pygame.image.load("assets/backgrounds/room_1_background.png"), gc, gd))
    gd.room_list["room1"].activate_plot("room1_1_1")

    gd.room_list["room1"].generate_room_grid()

    gd.room_list["room1"].add_room_door("room1_door1", Door("room1", "room2", 2, 2, 1, 14, "room1_door1"))
    gd.room_list["room1"].add_room_door("room1_door2", Door("room1", "room4", 5, 1, 2, 4, "room1_door2"))

    # add the NPC characters to the game
    gd.add_character("Shuma", Pixie(2, 3, 2, 3, 32, 40, Spritesheet("assets/NPC_sprites/sprite_sheet.png", 32, 40), "Shuma", gc, gd, "Hi!"))

    gd.add_character("Julia", Pixie(5, 5, 5, 5, 32, 40, Spritesheet("assets/NPC_sprites/sprite_sheet.png", 32, 40), "Julia", gc, gd, "Hi!"))

    gd.add_character("Laurie", Pixie(4, 3, 4, 3, 32, 40, Spritesheet("assets/NPC_sprites/Laurie.png", 32, 40), "Laurie", gc, gd, "Have you seen my drink anywhere?"))

    #add props to the game
    gd.add_prop("trunk", Prop(3, 3, 3, 3, 32, 40, Spritesheet("assets/prop_sprites/trunk.png", 32, 40), "trunk", gc, gd, 1, 1))
    gd.add_prop("lamp", Prop(2, 5, 2, 5, 32, 40, Spritesheet("assets/prop_sprites/lamp.png", 32, 40), "lamp", gc, gd, 1, 1))

    #add all the features to the current room
    gd.room_list["room1"].add_room_character("Shuma")
    gd.room_list["room1"].add_room_character("Julia")
    gd.room_list["room1"].add_room_character("Laurie")
    gd.room_list["room1"].add_room_prop("trunk")
    gd.room_list["room1"].add_room_prop("lamp")

    # add position manager to it's room and make it tell the tile array what it's filled with
    gd.add_positioner("room1", Position_Manager("room1", gc, gd))
    gd.positioner["room1"].fill_tiles("room1")
    gd.positioner["room1"].fill_doors("room1")

    # activate the timers for animation and actions for the NPCs (make this apply to all that are in room)
    for character in gd.room_list["room1"].character_list:
        gd.character_list[character].activate_timers()

def init_room_2(gc, gd):
    # room#2

    # add the room #2, generate the grid, and add the background and doors
    gd.add_room("room2", Room2("room2", 1, 1, 15, 15, 1, 1, 15, 15, gc, gd, map_style="csv"))
    gd.room_list["room2"].add_room_plot("room2_1_1", Plot("room2", 1, 1,
                                                          pygame.image.load("assets/backgrounds/room_2_background.png"),
                                                          gc, gd))
    gd.room_list["room2"].activate_plot("room2_1_1")
    gd.room_list["room2"].generate_room_grid()



    room2_map = TileMap("assets/csv_maps/room2.csv", "grass", "water")

    gd.room_list["room2"].add_room_door("room2_door1", Door("room2", "room1", 1, 15, 2, 3, "room2_door1"))
    gd.room_list["room2"].add_room_door("room2_door2", Door("room2", "room3", 8, 12, 2, 4, "room2_door2"))

    # add features for room 2
    gd.add_prop("lamp4", Prop(1, 1, 1, 1, 32, 40, Spritesheet("assets/prop_sprites/lamp.png", 32, 40), "lamp4", gc, gd, 1, 1))
    gd.add_prop("lamp2", Prop(10, 5, 10, 5, 32, 40, Spritesheet("assets/prop_sprites/lamp.png", 32, 40), "lamp2", gc, gd, 1, 1))
    gd.add_prop("lamp3", Prop(8, 7, 8, 7, 32, 40, Spritesheet("assets/prop_sprites/lamp.png", 32, 40), "lamp3", gc, gd, 1, 1))
    gd.add_prop("house", Prop(4, 9, 4, 9, 192, 128, Spritesheet("assets/prop_sprites/House.png", 192, 128), "house", gc, gd, 6, 4, offset_y=0))

    gd.add_decoration("Grass1", Decoration(2, 13, 2, 13, 32, 32, Spritesheet("assets/decoration_sprites/grass.png", 32, 32), "Grass1", gc, gd, 1, 1, [[2, 13], [2, 14], [3, 13], [3, 14]]))

    # attach all features to room
    gd.room_list["room2"].add_room_prop("lamp2")
    gd.room_list["room2"].add_room_prop("lamp3")
    gd.room_list["room2"].add_room_prop("lamp4")
    gd.room_list["room2"].add_room_prop("house")



    gd.room_list["room2"].add_room_decoration("Grass1")

    # add position manager to it's room and make it tell the tile array what it's filled with, then populate doors
    gd.add_positioner("room2", Position_Manager("room2", gc, gd))
    gd.positioner["room2"].fill_obstacles("assets/csv_maps/room2.csv", "room2")
    gd.positioner["room2"].fill_tiles("room2")
    gd.positioner["room2"].fill_doors("room2")

def init_room_3(gc, gd):
    gd.add_room("room3", Room2("room3", 1, 2, 3, 3, 1, 1, 3, 3, gc, gd))
    gd.room_list["room3"].generate_room_grid()
    gd.room_list["room3"].add_room_plot("room3_1_1", Plot("room3", 1, 1, pygame.image.load("assets/backgrounds/room_3_background.png"), gc, gd))
    gd.room_list["room3"].add_room_door("room3_door1", Door("room3", "room2", 2, 5, 8, 13, "room3_door1"))

    gd.room_list["room3"].activate_plot("room3_1_1")

    gd.add_character("Pixie", Pixie(2, 2, 2, 2, 32, 40, Spritesheet("assets/NPC_sprites/sprite_sheet.png", 32, 40), "Pixie", gc, gd, "Hi!"))

    gd.add_character("Pixie_b", Pixie(3, 4, 3, 4, 32, 40, Spritesheet("assets/NPC_sprites/sprite2_sheet.png", 32, 40), "Pixie_b", gc, gd, "Hi!"))

    gd.add_character("Ian", Pixie(3, 2, 3, 2, 32, 40, Spritesheet("assets/NPC_sprites/Ian.png", 32, 40), "Ian", gc, gd, "Damnit, the cows got out again..."))

    gd.room_list["room3"].add_room_character("Pixie")
    gd.room_list["room3"].add_room_character("Pixie_b")
    gd.room_list["room3"].add_room_character("Ian")


    gd.add_positioner("room3", Position_Manager("room3", gc, gd))
    gd.positioner["room3"].fill_tiles("room3")
    gd.positioner["room3"].fill_doors("room3")

    for character in gd.room_list["room3"].character_list:
        gd.character_list[character].activate_timers()




def init_room_4(gc, gd):

    # add room #4
    gd.add_room("room4", Room2("room4", 1, 1, 100, 50, 2, 1, 50, 50, gc, gd))

    big_map = TileMap("assets/csv_maps/big_map.csv", "grass", "water")
    gd.room_list["room4"].add_room_plot("room4_1_1", Plot("room4", 1, 1, big_map.return_map(), gc, gd))
    gd.room_list["room4"].add_room_plot("room4_1_2", Plot("room4", 2, 1, big_map.return_map(), gc, gd))
    gd.room_list["room4"].activate_plot("room4_1_1")
    gd.room_list["room4"].activate_plot("room4_1_2")

    gd.room_list["room4"].generate_room_grid()




    for name in range(50):
        rand_x = randrange(1, 100)
        rand_y = randrange(1, 50)
        gd.add_character(("Sheep" + str(name)), Pixie(rand_x, rand_y, rand_x, rand_y, 32, 40, Spritesheet("assets/NPC_sprites/sheep.png", 32, 40), ("Sheep" + str(name)), gc, gd, "Baaaahhhh"))
        gd.room_list["room4"].add_room_character(("Sheep" + str(name)))
        gd.character_list["Sheep" + str(name)].activate_timers()

    gd.add_positioner("room4", Position_Manager("room4", gc, gd))

    # TODO: figure out how to use csv for rooms with multiple maps in them (Perhaps attach them to BG instead of Room)
    gd.positioner["room4"].fill_obstacles("assets/csv_maps/big_map.csv", "room4")
    gd.positioner["room4"].fill_tiles("room4")
    gd.positioner["room4"].fill_doors("room4")