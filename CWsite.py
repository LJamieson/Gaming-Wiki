from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   categories = ['Genre', 'Platform', 'Publisher', 'Year', 'All']
   return render_template('base.html', categories=categories)

@app.route('/All')
def games():
   entries = ['Alien:_Isolation', 'Doom', 'Doom_2', 'Doom_(2016)', 'Halo:_Combat_Evolved', 'Halo_2', 'Halo_3', 'Sonic_The_Hedgehog', 'Sonic_&_Knuckles'] 

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
    entries = ['X-Com_UFO_Defence', 'Doom_2', 'Sonic_&_Knuckles']
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
    entries = []
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/NES')
def NES():
    entries =[]
    nextdirect='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/SNES')
def SNES():
    entries = []
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/MegaDrive')
def Megadrive():
    entries = []
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Windows')
def Windows():
    entries = []
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Linux')
def Linux():
    entries = []
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/MacOS')
def MacOS():
    entries = []
    nextdirect ='/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Xbox')
def Xbox():
    entries = []
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/Xbox360')
def Xbox360():
    entries = []
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/PS1')
def PS1():
    entries = []
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/PS3')
def PS4():
    entries = []
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/GB')
def GB():
    entries = []
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

@app.route('/Platform/GBA')
def GBA():
    entries = []
    nextdirect = '/Games/'
    return render_template('base.html', categories=entries, direct=nextdirect)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
