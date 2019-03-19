__version__ = "3.0.1"

# Autor: Douglas
from pygame import mixer


# lista de códigos
def lista():
    print('Zelda´s lulabby: awdawd')
    print('Epona´s song: wadwad')
    print('Lost Woods: sdasda')
    print('Sun´s Song: dswdsw')
    print('Song of time: dxsdxs')
    print('Song of storms: xswxsw')
    print('Minuet of forest: xwadad')
    print('Bolero of fire: sxsxdsds')
    print('Serenade of water: xsdda')
    print('Requiem of spirit: xsxsdsx')
    print('Nocturne of Shadow: addxads')
    print('Prelude of light: wdwdaw')
    print(menu())


def menu():
    a = input('Press ENTER to write a sequence ')
    while a == '':
        print(musicas())
    else:
        print(menu())


def musicas():
    print('=' * 70)
    print('Zelda Ocarina of Time Ocarina Songs')
    m = input('Make a sequence using  w,a,s,d e x to play one song or help to open the song list: ')

    if m == 'help':
        print(lista())

    elif m == 'awdawd':
        print('Zelda´s lullaby')
        mixer.init()
        mixer.music.load('Zeldas lullaby.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'wadwad':
        print('Eponas Song')
        mixer.init()
        mixer.music.load('Eponas song.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'sdasda':
        print('Lost Woods')
        mixer.init()
        mixer.music.load('Lost Woods.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'dswdsw':
        print('Sun´s Song')
        mixer.init()
        mixer.music.load('Suns Song.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'dxsdxs':
        print('Song of Time')
        mixer.init()
        mixer.music.load('Song of Time.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'xswxsw':
        print('Song of storms')
        mixer.init()
        mixer.music.load('Song of Storms.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'xwadad':
        print('Minuet of Forest')
        mixer.init()
        mixer.music.load('Minuet of Forest.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'sxsxdsds':
        print('Bolero of Fire')
        mixer.init()
        mixer.music.load('Bolero of fire.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'xsdda':
        print('Serenade of Water')
        mixer.init()
        mixer.music.load('Serenade of Water.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'xsxsdsx':
        print('Requiem of Spirit')
        mixer.init()
        mixer.music.load('Requiem of Spirit.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'addxads':
        print('Nocturne of Shadow')
        mixer.init()
        mixer.music.load('Nocturne of Shadow.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    elif m == 'wdwdaw':
        print('Prelude of light')
        mixer.init()
        mixer.music.load('Prelude of Light.mp3')
        mixer.music.play()
        print('When the music ends press ENTER to continue')
        input()

    else:
        print('type another sequence, press ENTER to continue')


def reboot():
    v = input('Type 1 to play another music or 2 to exit: ')
    while v == '1':
        print(musicas())
        print(reboot())
    else:
        exit(0)


print(musicas())
print(reboot())
