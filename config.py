# config written by alpha (Alphanet#0001 on discord)

import collections
import functools

global parsedict
from json import loads as parsedict

global addItemName, formatCoordinates, translateItemId, ALL_ITEMS

ALL_ITEMS = {
    "minecraft:air": "Air",
    "minecraft:stone": "Stone",
    "minecraft:grass": "Grass",
    "minecraft:dirt": "Dirt",
    "minecraft:cobblestone": "Cobblestone",
    "minecraft:planks": "Planks",
    "minecraft:sapling": "Sapling",
    "minecraft:bedrock": "Bedrock",
    "minecraft:flowing_water": "Flowing Water",
    "minecraft:water": "Water",
    "minecraft:flowing_lava": "Flowing Lava",
    "minecraft:lava": "Lava",
    "minecraft:sand": "Sand",
    "minecraft:gravel": "Gravel",
    "minecraft:gold_ore": "Gold Ore",
    "minecraft:iron_ore": "Iron Ore",
    "minecraft:coal_ore": "Coal Ore",
    "minecraft:log": "Log",
    "minecraft:leaves": "Leaves",
    "minecraft:sponge": "Sponge",
    "minecraft:glass": "Glass",
    "minecraft:lapis_ore": "Lapis Ore",
    "minecraft:lapis_block": "Lapis Block",
    "minecraft:dispenser": "Dispenser",
    "minecraft:sandstone": "Sandstone",
    "minecraft:noteblock": "Noteblock",
    "minecraft:bed": "Bed",
    "minecraft:golden_rail": "Golden Rail",
    "minecraft:detector_rail": "Detector Rail",
    "minecraft:sticky_piston": "Sticky Piston",
    "minecraft:web": "Web",
    "minecraft:tallgrass": "Tallgrass",
    "minecraft:deadbush": "Deadbush",
    "minecraft:piston": "Piston",
    "minecraft:piston_head": "Piston Head",
    "minecraft:wool": "Wool",
    "minecraft:piston_extension": "Piston Extension",
    "minecraft:yellow_flower": "Yellow Flower",
    "minecraft:red_flower": "Red Flower",
    "minecraft:brown_mushroom": "Brown Mushroom",
    "minecraft:red_mushroom": "Red Mushroom",
    "minecraft:gold_block": "Gold Block",
    "minecraft:iron_block": "Iron Block",
    "minecraft:double_stone_slab": "Double Stone Slab",
    "minecraft:stone_slab": "Stone Slab",
    "minecraft:brick_block": "Brick Block",
    "minecraft:tnt": "Tnt",
    "minecraft:bookshelf": "Bookshelf",
    "minecraft:mossy_cobblestone": "Mossy Cobblestone",
    "minecraft:obsidian": "Obsidian",
    "minecraft:torch": "Torch",
    "minecraft:fire": "Fire",
    "minecraft:mob_spawner": "Mob Spawner",
    "minecraft:oak_stairs": "Oak Stairs",
    "minecraft:chest": "Chest",
    "minecraft:redstone_wire": "Redstone Wire",
    "minecraft:diamond_ore": "Diamond Ore",
    "minecraft:diamond_block": "Diamond Block",
    "minecraft:crafting_table": "Crafting Table",
    "minecraft:wheat": "Wheat",
    "minecraft:farmland": "Farmland",
    "minecraft:furnace": "Furnace",
    "minecraft:furnace": "Furnace",
    "minecraft:sign": "Sign",
    "minecraft:wooden_door": "Wooden Door",
    "minecraft:ladder": "Ladder",
    "minecraft:rail": "Rail",
    "minecraft:stone_stairs": "Stone Stairs",
    "minecraft:wall_sign": "Wall Sign",
    "minecraft:lever": "Lever",
    "minecraft:stone_pressure_plate": "Stone Pressure Plate",
    "minecraft:iron_door": "Iron Door",
    "minecraft:wooden_pressure_plate": "Wooden Pressure Plate",
    "minecraft:redstone_ore": "Redstone Ore",
    "minecraft:lit_redstone_ore": "Lit Redstone Ore",
    "minecraft:unlit_redstone_torch": "Unlit Redstone Torch",
    "minecraft:redstone_torch": "Redstone Torch",
    "minecraft:stone_button": "Stone Button",
    "minecraft:snow_layer": "Snow Layer",
    "minecraft:ice": "Ice",
    "minecraft:snow": "Snow",
    "minecraft:cactus": "Cactus",
    "minecraft:clay": "Clay",
    "minecraft:reeds": "Reeds",
    "minecraft:jukebox": "Jukebox",
    "minecraft:fence": "Fence",
    "minecraft:pumpkin": "Pumpkin",
    "minecraft:netherrack": "Netherrack",
    "minecraft:soul_sand": "Soul Sand",
    "minecraft:glowstone": "Glowstone",
    "minecraft:portal": "Portal",
    "minecraft:lit_pumpkin": "Lit Pumpkin",
    "minecraft:cake": "Cake",
    "minecraft:repeater": "Repeater",
    "minecraft:powered_repeater": "Powered Repeater",
    "minecraft:stained_glass": "Stained Glass",
    "minecraft:trapdoor": "Trapdoor",
    "minecraft:monster_egg": "Monster Egg",
    "minecraft:stonebrick": "Stonebrick",
    "minecraft:brown_mushroom_block": "Brown Mushroom Block",
    "minecraft:red_mushroom_block": "Red Mushroom Block",
    "minecraft:iron_bars": "Iron Bars",
    "minecraft:glass_pane": "Glass Pane",
    "minecraft:melon_block": "Melon Block",
    "minecraft:pumpkin_stem": "Pumpkin Stem",
    "minecraft:melon_stem": "Melon Stem",
    "minecraft:vine": "Vine",
    "minecraft:fence_gate": "Fence Gate",
    "minecraft:brick_stairs": "Brick Stairs",
    "minecraft:stone_brick_stairs": "Stone Brick Stairs",
    "minecraft:mycelium": "Mycelium",
    "minecraft:waterlily": "Waterlily",
    "minecraft:nether_brick": "Nether Brick",
    "minecraft:nether_brick_fence": "Nether Brick Fence",
    "minecraft:nether_brick_stairs": "Nether Brick Stairs",
    "minecraft:nether_wart": "Nether Wart",
    "minecraft:enchanting_table": "Enchanting Table",
    "minecraft:brewing_stand": "Brewing Stand",
    "minecraft:cauldron": "Cauldron",
    "minecraft:end_portal": "End Portal",
    "minecraft:end_portal_frame": "End Portal Frame",
    "minecraft:end_stone": "End Stone",
    "minecraft:dragon_egg": "Dragon Egg",
    "minecraft:redstone_lamp": "Redstone Lamp",
    "minecraft:lit_redstone_lamp": "Lit Redstone Lamp",
    "minecraft:double_wooden_slab": "Double Wooden Slab",
    "minecraft:wooden_slab": "Wooden Slab",
    "minecraft:cocoa": "Cocoa",
    "minecraft:sandstone_stairs": "Sandstone Stairs",
    "minecraft:emerald_ore": "Emerald Ore",
    "minecraft:ender_chest": "Ender Chest",
    "minecraft:tripwire_hook": "Tripwire Hook",
    "minecraft:tripwire": "Tripwire",
    "minecraft:emerald_block": "Emerald Block",
    "minecraft:spruce_stairs": "Spruce Stairs",
    "minecraft:birch_stairs": "Birch Stairs",
    "minecraft:jungle_stairs": "Jungle Stairs",
    "minecraft:command_block": "Command Block",
    "minecraft:beacon": "Beacon",
    "minecraft:cobblestone_wall": "Cobblestone Wall",
    "minecraft:flower_pot": "Flower Pot",
    "minecraft:carrots": "Carrots",
    "minecraft:potatoes": "Potatoes",
    "minecraft:wooden_button": "Wooden Button",
    "minecraft:skull": "Skull",
    "minecraft:anvil": "Anvil",
    "minecraft:trapped_chest": "Trapped Chest",
    "minecraft:light_weighted_pressure_plate": "Light Weighted Pressure Plate",
    "minecraft:heavy_weighted_pressure_plate": "Heavy Weighted Pressure Plate",
    "minecraft:comparator": "Comparator",
    "minecraft:powered_redstone_comparator": "Powered Redstone Comparator",
    "minecraft:daylight_detector": "Daylight Detector",
    "minecraft:redstone_block": "Redstone Block",
    "minecraft:quartz_ore": "Quartz Ore",
    "minecraft:hopper": "Hopper",
    "minecraft:quartz_block": "Quartz Block",
    "minecraft:quartz_stairs": "Quartz Stairs",
    "minecraft:activator_rail": "Activator Rail",
    "minecraft:dropper": "Dropper",
    "minecraft:stained_hardened_clay": "Stained Hardened Clay",
    "minecraft:stained_glass_pane": "Stained Glass Pane",
    "minecraft:leaves2": "Leaves2",
    "minecraft:log2": "Log2",
    "minecraft:acacia_stairs": "Acacia Stairs",
    "minecraft:dark_oak_stairs": "Dark Oak Stairs",
    "minecraft:slime": "Slime",
    "minecraft:barrier": "Barrier",
    "minecraft:iron_trapdoor": "Iron Trapdoor",
    "minecraft:prismarine": "Prismarine",
    "minecraft:sea_lantern": "Sea Lantern",
    "minecraft:hay_block": "Hay Block",
    "minecraft:carpet": "Carpet",
    "minecraft:hardened_clay": "Hardened Clay",
    "minecraft:coal_block": "Coal Block",
    "minecraft:packed_ice": "Packed Ice",
    "minecraft:double_plant": "Double Plant",
    "minecraft:banner": "Banner",
    "minecraft:wall_banner": "Wall Banner",
    "minecraft:daylight_detector_inverted": "Daylight Detector Inverted",
    "minecraft:red_sandstone": "Red Sandstone",
    "minecraft:red_sandstone_stairs": "Red Sandstone Stairs",
    "minecraft:double_stone_slab2": "Double Stone Slab2",
    "minecraft:stone_slab2": "Stone Slab2",
    "minecraft:spruce_fence_gate": "Spruce Fence Gate",
    "minecraft:birch_fence_gate": "Birch Fence Gate",
    "minecraft:jungle_fence_gate": "Jungle Fence Gate",
    "minecraft:dark_oak_fence_gate": "Dark Oak Fence Gate",
    "minecraft:acacia_fence_gate": "Acacia Fence Gate",
    "minecraft:spruce_fence": "Spruce Fence",
    "minecraft:birch_fence": "Birch Fence",
    "minecraft:jungle_fence": "Jungle Fence",
    "minecraft:dark_oak_fence": "Dark Oak Fence",
    "minecraft:acacia_fence": "Acacia Fence",
    "minecraft:spruce_door": "Spruce Door",
    "minecraft:birch_door": "Birch Door",
    "minecraft:jungle_door": "Jungle Door",
    "minecraft:acacia_door": "Acacia Door",
    "minecraft:dark_oak_door": "Dark Oak Door",
    "minecraft:end_rod": "End Rod",
    "minecraft:chorus_plant": "Chorus Plant",
    "minecraft:chorus_flower": "Chorus Flower",
    "minecraft:purpur_block": "Purpur Block",
    "minecraft:purpur_pillar": "Purpur Pillar",
    "minecraft:purpur_stairs": "Purpur Stairs",
    "minecraft:purpur_double_slab": "Purpur Double Slab",
    "minecraft:purpur_slab": "Purpur Slab",
    "minecraft:end_bricks": "End Bricks",
    "minecraft:beetroots": "Beetroots",
    "minecraft:grass_path": "Grass Path",
    "minecraft:end_gateway": "End Gateway",
    "minecraft:repeating_command_block": "Repeating Command Block",
    "minecraft:chain_command_block": "Chain Command Block",
    "minecraft:frosted_ice": "Frosted Ice",
    "minecraft:magma": "Magma",
    "minecraft:nether_wart_block": "Nether Wart Block",
    "minecraft:red_nether_brick": "Red Nether Brick",
    "minecraft:bone_block": "Bone Block",
    "minecraft:structure_void": "Structure Void",
    "minecraft:observer": "Observer",
    "minecraft:white_shulker_box": "White Shulker Box",
    "minecraft:orange_shulker_box": "Orange Shulker Box",
    "minecraft:magenta_shulker_box": "Magenta Shulker Box",
    "minecraft:light_blue_shulker_box": "Light Blue Shulker Box",
    "minecraft:yellow_shulker_box": "Yellow Shulker Box",
    "minecraft:lime_shulker_box": "Lime Shulker Box",
    "minecraft:pink_shulker_box": "Pink Shulker Box",
    "minecraft:gray_shulker_box": "Gray Shulker Box",
    "minecraft:silver_shulker_box": "Silver Shulker Box",
    "minecraft:cyan_shulker_box": "Cyan Shulker Box",
    "minecraft:purple_shulker_box": "Purple Shulker Box",
    "minecraft:blue_shulker_box": "Blue Shulker Box",
    "minecraft:brown_shulker_box": "Brown Shulker Box",
    "minecraft:green_shulker_box": "Green Shulker Box",
    "minecraft:red_shulker_box": "Red Shulker Box",
    "minecraft:black_shulker_box": "Black Shulker Box",
    "minecraft:white_glazed_terracotta": "White Glazed Terracotta",
    "minecraft:orange_glazed_terracotta": "Orange Glazed Terracotta",
    "minecraft:magenta_glazed_terracotta": "Magenta Glazed Terracotta",
    "minecraft:light_blue_glazed_terracotta": "Light Blue Glazed Terracotta",
    "minecraft:yellow_glazed_terracotta": "Yellow Glazed Terracotta",
    "minecraft:lime_glazed_terracotta": "Lime Glazed Terracotta",
    "minecraft:pink_glazed_terracotta": "Pink Glazed Terracotta",
    "minecraft:gray_glazed_terracotta": "Gray Glazed Terracotta",
    "minecraft:silver_glazed_terracotta": "Silver Glazed Terracotta",
    "minecraft:cyan_glazed_terracotta": "Cyan Glazed Terracotta",
    "minecraft:purple_glazed_terracotta": "Purple Glazed Terracotta",
    "minecraft:blue_glazed_terracotta": "Blue Glazed Terracotta",
    "minecraft:brown_glazed_terracotta": "Brown Glazed Terracotta",
    "minecraft:green_glazed_terracotta": "Green Glazed Terracotta",
    "minecraft:red_glazed_terracotta": "Red Glazed Terracotta",
    "minecraft:black_glazed_terracotta": "Black Glazed Terracotta",
    "minecraft:concrete": "Concrete",
    "minecraft:concrete_powder": "Concrete Powder",
    "minecraft:structure_block": "Structure Block",
    "minecraft:iron_shovel": "Iron Shovel",
    "minecraft:iron_pickaxe": "Iron Pickaxe",
    "minecraft:iron_axe": "Iron Axe",
    "minecraft:flint_and_steel": "Flint And Steel",
    "minecraft:apple": "Apple",
    "minecraft:bow": "Bow",
    "minecraft:arrow": "Arrow",
    "minecraft:coal": "Coal",
    "minecraft:diamond": "Diamond",
    "minecraft:iron_ingot": "Iron Ingot",
    "minecraft:gold_ingot": "Gold Ingot",
    "minecraft:iron_sword": "Iron Sword",
    "minecraft:wooden_sword": "Wooden Sword",
    "minecraft:wooden_shovel": "Wooden Shovel",
    "minecraft:wooden_pickaxe": "Wooden Pickaxe",
    "minecraft:wooden_axe": "Wooden Axe",
    "minecraft:stone_sword": "Stone Sword",
    "minecraft:stone_shovel": "Stone Shovel",
    "minecraft:stone_pickaxe": "Stone Pickaxe",
    "minecraft:stone_axe": "Stone Axe",
    "minecraft:diamond_sword": "Diamond Sword",
    "minecraft:diamond_shovel": "Diamond Shovel",
    "minecraft:diamond_pickaxe": "Diamond Pickaxe",
    "minecraft:diamond_axe": "Diamond Axe",
    "minecraft:stick": "Stick",
    "minecraft:bowl": "Bowl",
    "minecraft:mushroom_stew": "Mushroom Stew",
    "minecraft:golden_sword": "Golden Sword",
    "minecraft:golden_shovel": "Golden Shovel",
    "minecraft:golden_pickaxe": "Golden Pickaxe",
    "minecraft:golden_axe": "Golden Axe",
    "minecraft:string": "String",
    "minecraft:feather": "Feather",
    "minecraft:gunpowder": "Gunpowder",
    "minecraft:wooden_hoe": "Wooden Hoe",
    "minecraft:stone_hoe": "Stone Hoe",
    "minecraft:iron_hoe": "Iron Hoe",
    "minecraft:diamond_hoe": "Diamond Hoe",
    "minecraft:golden_hoe": "Golden Hoe",
    "minecraft:wheat_seeds": "Wheat Seeds",
    "minecraft:wheat": "Wheat",
    "minecraft:bread": "Bread",
    "minecraft:leather_helmet": "Leather Helmet",
    "minecraft:leather_chestplate": "Leather Chestplate",
    "minecraft:leather_leggings": "Leather Leggings",
    "minecraft:leather_boots": "Leather Boots",
    "minecraft:chainmail_helmet": "Chainmail Helmet",
    "minecraft:chainmail_chestplate": "Chainmail Chestplate",
    "minecraft:chainmail_leggings": "Chainmail Leggings",
    "minecraft:chainmail_boots": "Chainmail Boots",
    "minecraft:iron_helmet": "Iron Helmet",
    "minecraft:iron_chestplate": "Iron Chestplate",
    "minecraft:iron_leggings": "Iron Leggings",
    "minecraft:iron_boots": "Iron Boots",
    "minecraft:diamond_helmet": "Diamond Helmet",
    "minecraft:diamond_chestplate": "Diamond Chestplate",
    "minecraft:diamond_leggings": "Diamond Leggings",
    "minecraft:diamond_boots": "Diamond Boots",
    "minecraft:golden_helmet": "Golden Helmet",
    "minecraft:golden_chestplate": "Golden Chestplate",
    "minecraft:golden_leggings": "Golden Leggings",
    "minecraft:golden_boots": "Golden Boots",
    "minecraft:flint": "Flint",
    "minecraft:porkchop": "Porkchop",
    "minecraft:cooked_porkchop": "Cooked Porkchop",
    "minecraft:painting": "Painting",
    "minecraft:golden_apple": "Golden Apple",
    "minecraft:sign": "Sign",
    "minecraft:wooden_door": "Wooden Door",
    "minecraft:bucket": "Bucket",
    "minecraft:water_bucket": "Water Bucket",
    "minecraft:lava_bucket": "Lava Bucket",
    "minecraft:minecart": "Minecart",
    "minecraft:saddle": "Saddle",
    "minecraft:iron_door": "Iron Door",
    "minecraft:redstone": "Redstone",
    "minecraft:snowball": "Snowball",
    "minecraft:boat": "Boat",
    "minecraft:leather": "Leather",
    "minecraft:milk_bucket": "Milk Bucket",
    "minecraft:brick": "Brick",
    "minecraft:clay_ball": "Clay Ball",
    "minecraft:reeds": "Reeds",
    "minecraft:paper": "Paper",
    "minecraft:book": "Book",
    "minecraft:slime_ball": "Slime Ball",
    "minecraft:chest_minecart": "Chest Minecart",
    "minecraft:furnace_minecart": "Furnace Minecart",
    "minecraft:egg": "Egg",
    "minecraft:compass": "Compass",
    "minecraft:fishing_rod": "Fishing Rod",
    "minecraft:clock": "Clock",
    "minecraft:glowstone_dust": "Glowstone Dust",
    "minecraft:fish": "Fish",
    "minecraft:cooked_fish": "Cooked Fish",
    "minecraft:dye": "Dye",
    "minecraft:bone": "Bone",
    "minecraft:sugar": "Sugar",
    "minecraft:cake": "Cake",
    "minecraft:bed": "Bed",
    "minecraft:repeater": "Repeater",
    "minecraft:cookie": "Cookie",
    "minecraft:filled_map": "Filled Map",
    "minecraft:shears": "Shears",
    "minecraft:melon": "Melon",
    "minecraft:pumpkin_seeds": "Pumpkin Seeds",
    "minecraft:melon_seeds": "Melon Seeds",
    "minecraft:beef": "Beef",
    "minecraft:cooked_beef": "Cooked Beef",
    "minecraft:chicken": "Chicken",
    "minecraft:cooked_chicken": "Cooked Chicken",
    "minecraft:rotten_flesh": "Rotten Flesh",
    "minecraft:ender_pearl": "Ender Pearl",
    "minecraft:blaze_rod": "Blaze Rod",
    "minecraft:ghast_tear": "Ghast Tear",
    "minecraft:gold_nugget": "Gold Nugget",
    "minecraft:nether_wart": "Nether Wart",
    "minecraft:potion": "Potion",
    "minecraft:glass_bottle": "Glass Bottle",
    "minecraft:spider_eye": "Spider Eye",
    "minecraft:fermented_spider_eye": "Fermented Spider Eye",
    "minecraft:blaze_powder": "Blaze Powder",
    "minecraft:magma_cream": "Magma Cream",
    "minecraft:brewing_stand": "Brewing Stand",
    "minecraft:cauldron": "Cauldron",
    "minecraft:ender_eye": "Ender Eye",
    "minecraft:speckled_melon": "Speckled Melon",
    "minecraft:potion": "Potion",
    "minecraft:experience_bottle": "Experience Bottle",
    "minecraft:fire_charge": "Fire Charge",
    "minecraft:writable_book": "Writable Book",
    "minecraft:written_book": "Written Book",
    "minecraft:emerald": "Emerald",
    "minecraft:item_frame": "Item Frame",
    "minecraft:flower_pot": "Flower Pot",
    "minecraft:carrot": "Carrot",
    "minecraft:potato": "Potato",
    "minecraft:baked_potato": "Baked Potato",
    "minecraft:poisonous_potato": "Poisonous Potato",
    "minecraft:map": "Map",
    "minecraft:golden_carrot": "Golden Carrot",
    "minecraft:skull": "Skull",
    "minecraft:carrot_on_a_stick": "Carrot On A Stick",
    "minecraft:nether_star": "Nether Star",
    "minecraft:pumpkin_pie": "Pumpkin Pie",
    "minecraft:fireworks": "Fireworks",
    "minecraft:firework_charge": "Firework Charge",
    "minecraft:enchanted_book": "Enchanted Book",
    "minecraft:comparator": "Comparator",
    "minecraft:netherbrick": "Netherbrick",
    "minecraft:quartz": "Quartz",
    "minecraft:tnt_minecart": "Tnt Minecart",
    "minecraft:hopper_minecart": "Hopper Minecart",
    "minecraft:prismarine_shard": "Prismarine Shard",
    "minecraft:prismarine_crystals": "Prismarine Crystals",
    "minecraft:rabbit": "Rabbit",
    "minecraft:cooked_rabbit": "Cooked Rabbit",
    "minecraft:rabbit_stew": "Rabbit Stew",
    "minecraft:rabbit_foot": "Rabbit Foot",
    "minecraft:rabbit_hide": "Rabbit Hide",
    "minecraft:armor_stand": "Armor Stand",
    "minecraft:iron_horse_armor": "Iron Horse Armor",
    "minecraft:golden_horse_armor": "Golden Horse Armor",
    "minecraft:diamond_horse_armor": "Diamond Horse Armor",
    "minecraft:lead": "Lead",
    "minecraft:name_tag": "Name Tag",
    "minecraft:command_block_minecart": "Command Block Minecart",
    "minecraft:mutton": "Mutton",
    "minecraft:cooked_mutton": "Cooked Mutton",
    "minecraft:banner": "Banner",
    "minecraft:end_crystal": "End Crystal",
    "minecraft:spruce_door": "Spruce Door",
    "minecraft:birch_door": "Birch Door",
    "minecraft:jungle_door": "Jungle Door",
    "minecraft:acacia_door": "Acacia Door",
    "minecraft:dark_oak_door": "Dark Oak Door",
    "minecraft:chorus_fruit": "Chorus Fruit",
    "minecraft:chorus_fruit_popped": "Chorus Fruit Popped",
    "minecraft:beetroot": "Beetroot",
    "minecraft:beetroot_seeds": "Beetroot Seeds",
    "minecraft:beetroot_soup": "Beetroot Soup",
    "minecraft:dragon_breath": "Dragon Breath",
    "minecraft:splash_potion": "Splash Potion",
    "minecraft:spectral_arrow": "Spectral Arrow",
    "minecraft:tipped_arrow": "Tipped Arrow",
    "minecraft:lingering_potion": "Lingering Potion",
    "minecraft:shield": "Shield",
    "minecraft:elytra": "Elytra",
    "minecraft:spruce_boat": "Spruce Boat",
    "minecraft:birch_boat": "Birch Boat",
    "minecraft:jungle_boat": "Jungle Boat",
    "minecraft:acacia_boat": "Acacia Boat",
    "minecraft:dark_oak_boat": "Dark Oak Boat",
    "minecraft:totem_of_undying": "Totem Of Undying",
    "minecraft:shulker_shell": "Shulker Shell",
    "minecraft:iron_nugget": "Iron Nugget",
    "minecraft:knowledge_book": "Knowledge Book",
    "minecraft:record_13": "Record 13",
    "minecraft:record_cat": "Record Cat",
    "minecraft:record_blocks": "Record Blocks",
    "minecraft:record_chirp": "Record Chirp",
    "minecraft:record_far": "Record Far",
    "minecraft:record_mall": "Record Mall",
    "minecraft:record_mellohi": "Record Mellohi",
    "minecraft:record_stal": "Record Stal",
    "minecraft:record_strad": "Record Strad",
    "minecraft:record_ward": "Record Ward",
    "minecraft:record_11": "Record 11",
    "minecraft:record_wait": "Record Wait",
    }

worlds["Hypnos SMP"] = "C:/Users/benme/Desktop/Hypnos SMP"  # PATH TO YOUR WORLD
world = "Hypnos SMP"
customwebassets = "C:/Users/benme/Desktop/overviewer-tweaks-main"  # PATH TO YOUR WEB ASSETS
outputdir = "C:/Users/benme/Desktop/hypnos-output"  # PATH TO YOUR OUTPUT DIR

custom_overlay_rendermode = [HeatmapOverlay(
  t_invisible=int((datetime.now() - timedelta(days=60)).timestamp()),
  t_full=int(datetime.now().timestamp())
)]

def addItemName(itemdict):
    if 'tag' in itemdict:
        if 'display' in itemdict['tag']:
            if 'Name' in itemdict['tag']['display']:
                if itemdict['tag']['display']['Name'] is not None and itemdict['tag']['display']['Name'] != "":
                        return " (<i>" + itemdict['tag']['display']['Name'] + "</i>)"
    return ""

def formatCoordinates(x, y, z):
    return "{:.1f}, {:.1f}, {:.1f}".format(x, y, z)

def translateItemId(itemid, iconsuffix=False, iconprefix=True):
    if itemid in ALL_ITEMS:
        istr = ""
        if iconprefix:
            istr += '<img src="poi_icons/icons/{0}.png" alt="{1}" width="16" height="16"> '.format(itemid.split(':')[1], ALL_ITEMS[itemid])
        istr += ALL_ITEMS[itemid]
        if iconsuffix:
            istr += ' <img src="poi_icons/{0}.png" alt="{1}" width="16" height="16">'.format(itemid.split(':')[1], ALL_ITEMS[itemid])
        return istr
    else:
        return itemid

def location_filter(poi):
	if poi['id'] == 'tlocation' or poi['id'] == 'plocation':
		poi['icon'] = "%s.png" % poi['id']
		return "<b>%s</b><br>located at %s, %s, %s" % (poi['name'], poi['x'], poi['y'], poi['z'])


def chest_filter(poi):
    if poi['id'] == "Chest" or poi['id'] == 'minecraft:chest' or poi['id'] == "Trapped Chest" or poi['id'] == 'minecraft:trapped_chest':
        if "LootTable" in poi:
            return None
        else:
            if len(poi.get('Items', [])) > 0:
                items = poi.get('Items', [])
                itemstring = ["<b>Chest with {0} items at {1}: </b>".format(len(items), formatCoordinates(poi['x'], poi['y'], poi['z']))]
                for item in items:
                    istring = "{0}x {1}".format(item['Count'], translateItemId(item['id']))
                    istring = istring + addItemName(item)
                    itemstring.append(istring)
                return ("Chest", "<br>".join(itemstring))
            else:
                return None


def sign_filter(poi):
	if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
		return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])


def shulker_filter(poi):
    if poi['id'].lower().find("shulker_box") != -1:
        if "LootTable" in poi:
            return None
        else:
            if len(poi.get('Items', [])) > 0:
                items = poi.get('Items', [])
                itemstring = ["<b>Shulker Box with {0} items at {1}: </b>".format(len(items), formatCoordinates(poi['x'], poi['y'], poi['z']))]
                for item in items:
                    istring = "{0}x {1}".format(item['Count'], translateItemId(item['id']))
                    istring = istring + addItemName(item)
                    itemstring.append(istring)
                return ("Shulker Box", "<br>".join(itemstring))
            else:
                return None


def player_icons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s/head" % poi['EntityId']
        if len(poi.get('Inventory', [])) > 0:
            items = poi.get('Inventory', [])
            itemstring = ["<b>%s</b><br>Located at %s, %s, %s<br>Inventory:" % (poi['EntityId'], poi['x'], poi['y'], poi['z'])]
            for item in items:
                istring = "{0}x {1}".format(item['Count'], translateItemId(item['id']))
                istring = istring + addItemName(item)
                itemstring.append(istring)
            return ("Player", "<br>".join(itemstring))
        else:
            return None


def books_filter(poi):
    if 'Items' in poi:
        if "LootTable" in poi:
            return None
        else:
            items = poi.get('Items', [])
            if len(items) > 0:
                itemsFilter = ['minecraft:written_book', 'minecraft:writable_book']
                try:
                    itemstring = f"Book located at {poi['x']}, {poi['y']}, {poi['z']}"
                except:
                    print('except1')
                for item in items:
                    if item['id'] in itemsFilter:
                        if item['id'] == itemsFilter[0]:
                            try:
                                itemstring += f"<br>Entitled: {poi['Items'][0]['tag']['title']}"
                                itemstring += f"<br>Author: {poi['Items'][0]['tag']['author']}"
                                pages = poi['Items'][0]['tag']['pages']
                                for i in pages:
                                    itemstring += f"<br><br>{parsedict(i)['text']}"
                            except:
                                print('except2')
                        if item['id'] == itemsFilter[1]:
                            try:
                                pages = poi['Items'][0]['tag']['pages']
                                for i in pages:
                                    itemstring += f"<br><br>{i}"
                            except:
                                print('except3')
                        return itemstring
            else:
                return None


renders['Overworld'] = {
    "world": "Hypnos SMP",
	"title": "3D Overworld",
	"rendermode": "smooth_lighting",
	"dimension": "overworld",
	"defaultzoom": 15,
	'manualpois': [
		{'id': 'tlocation', 'name': 'Coming Soon tm', 'x': 0, 'y': 90, 'z': 0},
	],
}

renders["OverworldHM"] = {
    "world": "Hypnos SMP",
    "dimension": "overworld",
    "title": "Activity Heatmap",
    "rendermode": custom_overlay_rendermode,
    "overlay": ["Overworld"],
}

renders['Nether'] = {
    "world": "Hypnos SMP",
    "title": "3D Nether",
    "rendermode": "normal",
    "dimension": "nether",
    "defaultzoom": 15,
    'manualpois': [
		{'id': 'tlocation', 'name': 'Coming Soon tm', 'x': 0, 'y': 90, 'z': 0},
    ],
}

renders["NetherHM"] = {
    "world": "Hypnos SMP",
    "dimension": "nether",
    "title": "Activity Heatmap",
    "rendermode": custom_overlay_rendermode,
    "overlay": ["Nether"],
}

renders["Nether2"] = {
    "world": "Hypnos SMP",
    "dimension": "nether",
    "title": "No Roof",
    "rendermode": "nether",
}

renders['End'] = {
    "world": "Hypnos SMP",
    "title": "3D End",
    "dimension": "end",
    "defaultzoom": 15,
    'manualpois': [
		{'id': 'tlocation', 'name': 'Coming Soon tm', 'x': 0, 'y': 90, 'z': 0},
    ],
}

renders["EndHM"] = {
    "world": "Hypnos SMP",
    "dimension": "end",
    "title": "Activity Heatmap",
    "rendermode": custom_overlay_rendermode,
    "overlay": ["End"],
}

ids = [
"acacia_boat",
"acacia_door",
"acacia_door",
"acacia_fence",
"acacia_fence_gate",
"acacia_stairs",
"activator_rail",
"anvil",
"apple",
"armor_stand",
"arrow",
"baked_potato",
"banner",
"barrier",
"beacon",
"bed",
"beef",
"beetroot",
"beetroot_seeds",
"beetroot_soup",
"beetroots",
"birch_boat",
"birch_door",
"birch_door",
"birch_fence",
"birch_fence_gate",
"birch_stairs",
"black_shulker_box",
"blaze_powder",
"blaze_rod",
"blue_shulker_box",
"boat",
"bone",
"bone_block",
"book",
"bookshelf",
"bow",
"bowl",
"bread",
"brewing_stand",
"brewing_stand",
"brick",
"brick_block",
"brick_stairs",
"brown_mushroom",
"brown_shulker_box",
"bucket",
"cactus",
"cake",
"carpet",
"carrot",
"carrot_on_a_stick",
"carrots",
"cauldron",
"cauldron",
"chainmail_boots",
"chainmail_chestplate",
"chainmail_helmet",
"chainmail_leggings",
"chest",
"chest_minecart",
"chicken",
"chorus_flower",
"chorus_fruit",
"chorus_fruit_popped",
"chorus_plant",
"clay",
"clay_ball",
"clock",
"coal",
"coal_block",
"coal_ore",
"cobblestone",
"cobblestone_wall",
"cocoa",
"command_block",
"comparator",
"compass",
"concrete",
"concrete_powder",
"cooked_beef",
"cooked_chicken",
"cooked_fish",
"cooked_mutton",
"cooked_porkchop",
"cooked_rabbit",
"cookie",
"crafting_table",
"cyan_shulker_box",
"dark_oak_boat",
"dark_oak_door",
"dark_oak_door",
"dark_oak_fence",
"dark_oak_fence_gate",
"dark_oak_stairs",
"daylight_detector",
"deadbush",
"detector_rail",
"diamond",
"diamond_axe",
"diamond_block",
"diamond_boots",
"diamond_chestplate",
"diamond_helmet",
"diamond_hoe",
"diamond_horse_armor",
"diamond_leggings",
"diamond_ore",
"diamond_pickaxe",
"diamond_shovel",
"diamond_sword",
"dirt",
"dispenser",
"double_plant",
"dragon_breath",
"dragon_egg",
"dropper",
"dye",
"egg",
"elytra",
"emerald",
"emerald_block",
"emerald_ore",
"enchanted_book",
"enchanting_table",
"end_bricks",
"end_crystal",
"end_rod",
"end_stone",
"ender_chest",
"ender_eye",
"ender_pearl",
"experience_bottle",
"farmland",
"feather",
"fence",
"fence_gate",
"fermented_spider_eye",
"filled_map",
"fire_charge",
"firework_charge",
"fireworks",
"fish",
"fishing_rod",
"flint",
"flint_and_steel",
"flower_pot",
"flower_pot",
"frosted_ice",
"furnace",
"furnace",
"ghast_tear",
"glass",
"glass_bottle",
"glass_pane",
"glowstone",
"glowstone_dust",
"gold_block",
"gold_ingot",
"gold_nugget",
"gold_ore",
"golden_apple",
"golden_axe",
"golden_boots",
"golden_carrot",
"golden_chestplate",
"golden_helmet",
"golden_hoe",
"golden_horse_armor",
"golden_leggings",
"golden_pickaxe",
"golden_rail",
"golden_shovel",
"golden_sword",
"grass",
"grass_path",
"gravel",
"gray_shulker_box",
"green_shulker_box",
"gunpowder",
"hardened_clay",
"hay_block",
"hopper",
"hopper_minecart",
"ice",
"iron_axe",
"iron_bars",
"iron_block",
"iron_boots",
"iron_chestplate",
"iron_door",
"iron_door",
"iron_helmet",
"iron_hoe",
"iron_horse_armor",
"iron_ingot",
"iron_leggings",
"iron_nugget",
"iron_ore",
"iron_pickaxe",
"iron_shovel",
"iron_sword",
"iron_trapdoor",
"item_frame",
"jukebox",
"jungle_boat",
"jungle_door",
"jungle_door",
"jungle_fence",
"jungle_fence_gate",
"jungle_stairs",
"ladder",
"lapis_block",
"lapis_ore",
"lava_bucket",
"lead",
"leather",
"leather_boots",
"leather_chestplate",
"leather_helmet",
"leather_leggings",
"leaves",
"lever",
"light_blue_shulker_box",
"lime_shulker_box",
"lit_pumpkin",
"lit_redstone_ore",
"log",
"magenta_shulker_box",
"magma",
"magma_cream",
"map",
"melon",
"melon_block",
"melon_seeds",
"melon_stem",
"milk_bucket",
"minecart",
"mob_spawner",
"monster_egg",
"mossy_cobblestone",
"mushroom_stew",
"mutton",
"mycelium",
"name_tag",
"nether_brick",
"nether_brick_fence",
"nether_brick_stairs",
"nether_star",
"nether_wart",
"nether_wart",
"nether_wart_block",
"netherbrick",
"netherrack",
"noteblock",
"oak_stairs",
"observer",
"obsidian",
"orange_shulker_box",
"packed_ice",
"painting",
"paper",
"pink_shulker_box",
"piston",
"piston_head",
"planks",
"poisonous_potato",
"porkchop",
"portal",
"potato",
"potatoes",
"potion",
"potion",
"prismarine",
"prismarine_crystals",
"prismarine_shard",
"pumpkin",
"pumpkin_pie",
"pumpkin_seeds",
"pumpkin_stem",
"purple_shulker_box",
"purpur_block",
"purpur_double_slab",
"purpur_pillar",
"purpur_slab",
"purpur_stairs",
"quartz",
"quartz_block",
"quartz_ore",
"quartz_stairs",
"rabbit",
"rabbit_foot",
"rabbit_hide",
"rabbit_stew",
"rail",
"red_flower",
"red_mushroom",
"red_mushroom_block",
"red_nether_brick",
"red_sandstone",
"red_sandstone_stairs",
"red_shulker_box",
"redstone",
"redstone_block",
"redstone_lamp",
"redstone_ore",
"redstone_torch",
"redstone_wire",
"reeds",
"reeds",
"repeater",
"repeater",
"rotten_flesh",
"saddle",
"sand",
"sandstone",
"sandstone_stairs",
"sapling",
"sea_lantern",
"shears",
"shulker_shell",
"sign",
"sign",
"silver_shulker_box",
"skull",
"slime",
"slime_ball",
"snow",
"snow_layer",
"snowball",
"soul_sand",
"speckled_melon",
"spider_eye",
"sponge",
"spruce_boat",
"spruce_door",
"spruce_door",
"spruce_fence",
"spruce_fence_gate",
"spruce_stairs",
"stained_glass",
"stained_glass_pane",
"stick",
"sticky_piston",
"stone",
"stone_axe",
"stone_brick_stairs",
"stone_button",
"stone_hoe",
"stone_pickaxe",
"stone_pressure_plate",
"stone_shovel",
"stone_slab",
"stone_stairs",
"stone_sword",
"stonebrick",
"string",
"structure_block",
"structure_void",
"sugar",
"tallgrass",
"tnt",
"tnt_minecart",
"torch",
"totem_of_undying",
"trapdoor",
"trapped_chest",
"tripwire",
"tripwire_hook",
"unlit_redstone_torch",
"vine",
"wall_sign",
"water_bucket",
"waterlily",
"web",
"wheat",
"wheat",
"wheat_seeds",
"white_shulker_box",
"wooden_axe",
"wooden_button",
"wooden_door",
"wooden_door",
"wooden_hoe",
"wooden_pickaxe",
"wooden_shovel",
"wooden_slab",
"wooden_sword",
"wool",
"writable_book",
"written_book",
"yellow_flower",
"yellow_shulker_box",
]

weird_names = {
	"minecraft:dragon_breath": "Dragon's Breath",
	"minecraft:map": "Empty Map"
}


# noinspection PyShadowingNames
def item_filter(poi, partial_id, name, full_id):
	def flatten(array) -> list:
		return [g for n in array for g in (flatten(n) if isinstance(n, list) else [n])]

	def flat_item_list(item) -> list:
		return [
			item_f for item_f in (
				[item] if "tag" not in item or
									"BlockEntityTag" not in item['tag'] or
									'Items' not in item['tag']['BlockEntityTag']
				else flat_item_list(item['tag']['BlockEntityTag']['Items']) + [item]
			)
		]

	def recursive_id_search(item):
		nonlocal full_id
		return item["id"] == full_id or "shulker_box" in item["id"] and "tag" in item and "BlockEntityTag" in item[
			'tag'] and "Items" in item['tag']["BlockEntityTag"] and list(
			filter(recursive_id_search, item['tag']["BlockEntityTag"]["Items"]))
	items = poi.get('Items', []) or poi.get('Inventory')
	if items:
		if "LootTable" not in poi:
			items = flatten(map(flat_item_list, items))
			count = sum(
				map(
					lambda a: a["Count"] if a['id'] == full_id else 0,
					# [print(item) or item for _list in
					items
					# for item in _list]
				)
			)  # list(filter(recursive_id_search, poi["Items"]))))
			if count:
				return f"{'' if 'EntityId' not in poi else poi['EntityId'] + ': '}{name}", f"Found <b>{count}</b> {name}<br>Located at {'?x?' if 'x' not in poi else poi['x']}, {'?x?' if 'y' not in poi else poi['y']}, {'?x?' if 'z' not in poi else poi['z']}"
		else:
			return None


for render in renders.keys():

	render: dict = renders[render]
	markers = render.setdefault(
		'markers', [
			dict(name="<b><u>Locations", filterFunction=location_filter, showIconInLegend=True, icon="marker_icons/mlocation.png"),
			dict(name="Players", filterFunction=player_icons, showIconInLegend=True, icon="marker_icons/playerhead.png"),
            dict(name="Chests", filterFunction=chest_filter, icon="marker_icons/chest.png", showIconInLegend=True),
			dict(name="Shulkers", filterFunction=shulker_filter, icon="marker_icons/shulker.png", showIconInLegend=True),
			dict(name="Signs", filterFunction=sign_filter, showIconInLegend=True),
			dict(name="Books", filterFunction=books_filter, icon="marker_icons/book.png", showIconInLegend=True),
		]
	)

	for partial_id in ids:
		full_id = (f"minecraft:{partial_id}" if not partial_id.startswith("minecraft:") else partial_id[:])
		partial_id = full_id[10:]
		name = weird_names[full_id] if full_id in weird_names else " ".join(
			map(str.capitalize, partial_id.replace("_", " ").split()))
		filter_function = functools.partial(item_filter, partial_id=partial_id[:], name=name[:], full_id=full_id[:])
		filter_function.__name__ = partial_id + "_item_filter"
		# noinspection PyTypeChecker
		markers.append(
			{
				'name': name,
				'filterFunction': filter_function,
				'icon': 'marker_icons/mlocation.png',
				'showInLegend': False
			}
		)
