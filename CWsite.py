from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   categories = ['Genre', 'Platform', 'Publisher', 'Year', 'Games']
   return render_template('base.html', categories=categories)

@app.route('/Games')
def games():
   entries = ['Alien:_Isolation', 'Doom', 'Doom_2', 'Doom_(2016)', 'Halo:_Combat_Evolved', 'Halo_2', 'Halo_3','Halo_Wars','Hearts_Of_Iron_IV','Pokemon_Blue','Pokemon_Emerald','Pokemon_Red','Stellaris', 'Sonic_The_Hedgehog', 'Sonic_&_Knuckles', 'Super_Mario_Bros.', 'Super_Mario_World','The_Elder_Scrolls_III:_Morrowind','The_Elder_Scrolls_V:_Skyrim','X-Com:_UFO_Defence','XCOM:_Enemy_Unknown'] 
   currentdirect='/Games/'
   return render_template('base.html', categories=entries, direct=currentdirect)

@app.route('/Games/Alien:_Isolation')
def alien():
   game = 'Alien: Isolation'
   details = []
   dict_details = dict(genre="FPS", year="2012", pub="Sega", plat="Windows, PS3, Xbox360, Linux, MacOS")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Doom')
def doom():
   game = 'Doom'
   details = []
   dict_details = dict(genre="FPS", year="1993", pub="id Software", plat="Windows, MS-DOS, Xbox360, Xbox, SNES, PS1, PS3, GBA")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Doom_2')
def doom2():
   game = 'Doom II'
   details = []
   dict_details = dict(genre="FPS", year="1993", pub="id Software", plat="Windows, MS-DOS, Xbox360, Xbox, MacOS, PS1, PS3, GBA")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Doom_(2016)')
def doom2016():
   game = 'Doom'
   details = []
   dict_details = dict(genre="FPS", year="2016", pub="Bethesda Softworks", plat="Windows")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Halo:_Combat_Evolved')
def halo():
   game = 'Halo: Combat Evolved'
   details = []
   dict_details = dict(genre="FPS", year="2001", pub="Microsoft Game Studios", plat="Xbox, Windows, MacOS, Xbox360")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Halo_2')
def halo2():
   game = 'Halo 2'
   details = []
   dict_details = dict(genre="FPS", year="2004", pub="Microsoft Game Studios", plat="Xbox, Windows, Xbox360")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Halo_3')
def halo3():
   game = 'Halo 3'
   details = []
   dict_details = dict(genre="FPS", year="2007", pub="Microsoft Game Studios", plat="Xbox360")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Halo_Wars')
def halowars():
   game = 'Halo Wars'
   details = []
   dict_details = dict(genre="Strategy", year="2009", pub="Microsoft Game Studios", plat="Windows, Xbox360")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Hearts_Of_Iron_IV')
def hoi4():
   game = 'Hearts Of Iron IV'
   details = []
   dict_details = dict(genre="Strategy", year="2016", pub="Paradox Interactive", plat="Windows, MacOS, Linux")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Pokemon_Blue')
def pokemonb():
   game = 'Pokemon Blue'
   details = []
   dict_details = dict(genre="RPG", year="1996", pub="Nintendo", plat="GB")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Pokemon_Red')
def pokemonr():
   game = 'Pokemon Red'
   details = []
   dict_details = dict(genre="RPG", year="1996", pub="Nintendo", plat="GB")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Pokemon_Emerald')
def pokemone():
   game = 'Pokemon Emerald'
   details = []
   dict_details = dict(genre="RPG", year="2004", pub="Nintendo", plat="GBA")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Stellaris')
def stellaris():
   game = 'Stellaris'
   details = []
   dict_details = dict(genre="Strategy", year="2016", pub="Paradox Interactive", plat="Windows, MacOS, Linux")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Sonic_The_Hedgehog')
def sonic():
   game = 'Sonic The Hedgehog'
   details = []
   dict_details = dict(genre="Platformer", year="1991", pub="Sega", plat="Megadrive, Windows, GBA")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Sonic_&_Knuckles')
def knuckles():
   game = 'Sonic & Knuckles'
   details = []
   dict_details = dict(genre="Platformer", year="1994", pub="Sega", plat="Megadrive, Windows")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Super_Mario_Bros.')
def smb():
   game = 'Super Mario Bros.'
   details = []
   dict_details = dict(genre="Platformer", year="1985", pub="Nintendo", plat="NES, SNES")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/Super_Mario_World')
def smw():
   game = 'Super Mario World'
   details = []
   dict_details = dict(genre="Platformer", year="1990", pub="Nintendo", plat="SNES, GBA")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/The_Elder_Scrolls_III:_Morrowind')
def morrowind():
   game = 'The Elder Scrolls III: Morrowind'
   details = []
   dict_details = dict(genre="RPG", year="2002", pub="Bethesda Softworks", plat="Xbox, Windows")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/The_Elder_Scrolls_V:_Skyrim')
def skyrim():
   game = 'The Elder Scrolls V: Skyrim'
   details = []
   dict_details = dict(genre="RPG", year="2011", pub="Bethesda Softworks", plat="Xbox360, Windows, PS3")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/X-Com:_UFO_Defence')
def ufo():
   game = 'X-Com: UFO Defence'
   details = []
   dict_details = dict(genre="Strategy", year="1994", pub="MircoProse", plat="MS-DOS, Windows, PS1")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Games/XCOM:_Enemy_Unknown')
def xcom():
   game = 'XCOM: Enemy Unknown'
   details = []
   dict_details = dict(genre="Strategy", year="2012", pub="2K Games", plat="MS-DOS, Windows, PS1")
   details.append(dict_details)
   return render_template('entry.html', game=game, details=details)

@app.route('/Genre')
def genre():
   categories = ['FPS', 'Platformer', 'Strategy', 'RPG']
   currentdirect='/Genre/'
   return render_template('base.html', categories=categories, direct=currentdirect)

@app.route('/Genre/FPS')
def fps():
   entries = ['Alien:_Isolation', 'Doom', 'Doom_2', 'Doom_(2016)','Halo:_Combat_Evolved', 'Halo_2', 'Halo_3']
   nextdirect='/Games/'
   return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Genre/Platformer')
def platformer():
    entries = ['Sonic_The_Hedgehog', 'Sonic_&_Knuckles', 'Super_Mario_Bros.', 'Super_Mario_World']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Genre/Strategy')
def strategy():
    entries = ['Halo_Wars','Hearts_Of_Iron_IV', 'Stellaris', 'X-Com_UFO_Defense', 'XCOM:_Enemy_Unknown']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Genre/RPG')
def rpg():
    entries = ['Pokemon_Red', 'Pokemon_Blue', 'Pokemon_Emerald', 'The_Elder_Scrolls_III:_Morrowind', 'The_Elder_Scrolls_V:_Skyrim']
    nextdirect='/Games/'
    return render_template('base.html', categories= entries, direct=nextdirect)

@app.route('/Year')
def year():
    categories = ['1985','1990','1991','1993','1994','1996','2001','2002','2004','2007','2009','2011','2012','2014','2016']
    currentdirect='/Year/'
    return render_template('base.html', categories=categories, direct=currentdirect)

@app.route('/Year/1985')
def y1985():
    entries = ['Super_Mario_Bros.']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/1990')
def y1990():
    entries = ['Super_Mario_World']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/1991')
def y1991():
    entries = ['Sonic_The_Hedgehog']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/1993')
def y1993():
    entries = ['Doom']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/1994')
def y1994():
    entries = ['X-Com:_UFO_Defence', 'Doom_2', 'Sonic_&_Knuckles']
    nextdirect='/Games/'
    return render_template('base.html', categories= entries, direct=nextdirect)

@app.route('/Year/1996')
def y1996():
    entries = ['Pokemon_Red, Pokemon_Blue']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2001')
def y2001():
   entries = ['Halo:_Combat_Evolved']
   nextdirect='/Games/'
   return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2002')
def y2002():
   entries = ['The_Elder_Scrolls_III:_Morrowind']
   nextdirect='/Games/'
   return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2004')
def y2004():
   entries = ['Pokemon_Emerald', 'Halo_2']
   nextdirect='/Games/'
   return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2007')
def y2007():
    entries = ['Halo_3']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2009')
def y2009():
    entries = ['Halo_Wars']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2011')
def y2011():
    entries = ['The_Elder_Scrolls_V:_Skyrim']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2012')
def y2012():
    entries = ['XCOM:_Enemy_Unknown']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2014')
def y2014():
    entries = ['Alien:_Isolation']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Year/2016')
def y2016():
    entries = ['Stellaris', 'Doom_(2016)', 'Hearts_Of_Iron_IV']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher')
def publisher():
    entries = ['2K_Games', 'Bethesda_Softworks', 'id_Software', 'MircoProse', 'Microsoft_Game_Studios', 'Nintendo', 'Paradox_Interactive', 'Sega']
    currentdirect='/Publisher/'
    return render_template('base.html', categories=entries, direct=currentdirect)

@app.route('/Publisher/2K_Games')
def TwoKGames():
    entries = ['XCOM: Enemy Unknown']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/Bethesda_Softworks')
def Bethesda():
    entries = ['The Elder Scrolls III: Morrowind', 'The Elder Scrolls V: Skyrim', 'Doom (2016)']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/id_Software')
def idSoftware():
    entries = ['Doom', 'Doom 2']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/MircoProse')
def mircoprose():
    entries = ['X-Com:_UFO_Defence']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/Mircosoft_Game_Studios')
def mircosoft():
    entries = ['Halo:_Combat_Evolved', 'Halo_2', 'Halo_3', 'Halo_Wars']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/Nintendo')
def nintendo():
    entries = ['Super_Mario_Bros.', 'Super_Mario_World', 'Pokemon_Red', 'Pokemon_Blue', 'Pokemon_Emerald']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/Paradox_Interactive')
def paradox():
    entries = ['Stellaris', 'Hearts_Of_Iron_IV']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Publisher/Sega')
def sega():
    entries = ['Sonic_The_Hedgehog', 'Sonic_&_Knuckles', 'Alien:_Isolation']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform')
def platform():
    entries = ['MS-DOS','NES','SNES','MegaDrive','Windows','Linux','MacOS','Xbox','Xbox360','PS1','PS3','GB','GBA']
    currentdirect='/Platform/'
    return render_template('base.html', categories=entries, direct=currentdirect)

@app.route('/Platform/MS-DOS')
def MSDOS():
    entries = ['Doom','Doom_2','X-Com:_UFO_Defence']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/NES')
def NES():
    entries =['Super_Mario_Bros.']
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/SNES')
def SNES():
    entries = ['Doom','Super_Mario_Bros.','Super_Mario_World']
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/MegaDrive')
def Megadrive():
    entries = ['Sonic_The_Hedgehog','Sonic_&_Knuckles']
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Windows')
def Windows():
    entries = ['Alien:_Isolation','Doom','Doom_2','Doom_(2016)','Halo:_Combat_Evolved','Halo_2','Halo_Wars','Hearts_Of_Iron_IV','Stellaris','Sonic_The_Hedgehog','Sonic_&_Knuckles','The_Elder_Scrolls_III:_Morrowind','The_Elder_Scrolls_V:_Skyrim','X-Com:_UFO_Defence','XCOM:_Enemy_Unknown']
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Linux')
def Linux():
    entries = ['Alien:_Isolation','Hearts_Of_Iron_IV','Stellaris','XCOM:_Enemy_Unknown']
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/MacOS')
def MacOS():
    entries = ['Alien:_Isolation','Doom_2','Halo:_Combat_Evolved','Hearts_Of_Iron_IV','Stellaris','XCOM:_Enemy_Unknown']
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Xbox')
def Xbox():
    entries = ['Doom','Doom_2','Halo:_Combat_Evolved','Halo_2','The_Elder_Scrolls_III:_Morrowind']
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Xbox360')
def Xbox360():
    entries = ['Alien:_Isolation','Doom','Doom_2','Halo:_Combat_Evolved','Halo_2','Halo_3','Halo_Wars','The_Elder_Scrolls_V:_Skyrim','XCOM:_Enemy_Unknown']
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/PS1')
def PS1():
    entries = ['Doom','Doom_2','X-Com:_UFO_Defence']
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/PS3')
def PS4():
    entries = ['Alien:_Isolation','Doom','Doom_2','The_Elder_Scrolls_V:_Skyrim','XCOM:_Enemy_Unknown']
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/GB')
def GB():
    entries = ['Pokemon_Blue','Pokemon_Red']
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/GBA')
def GBA():
    entries = ['Doom','Doom_2','Pokemon_Emerald','Sonic_The_Hedgehog','Super_Mario_World']
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
