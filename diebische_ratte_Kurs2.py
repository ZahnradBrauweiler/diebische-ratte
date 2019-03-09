from time import sleep
import random


def cover():
    print('---------------------------------------------------------\n'
        '---------------------------------------------------------\n'
        '\n'
        'Diebische Ratte\n'
        '\n'
        '            ________________________________\n'
        '           /                                \\\n'
        '          /                                  \\\n'
        '         /      /\\                  /\\        \\\n'
        '        /       \\/                  \\/         \\\n'
        '       /                                        \\\n'
        '      /         ________________________         \\\n'
        '      \\       /                         \\        /\n'
        '       \\_____/                           \\______/\n'
        '\n'
        '\n'
        'Ein Text-Adventure in Python von\n'
        'Clemens, Jakob, Johannes, Julian\n'
        '---------------------------------------------------------\n'
        '---------------------------------------------------------\n\n')
    sleep(3)

def einfuehrung():
    print('\nEndlich Feierabend. Dein Raumgleiter fliegt wie geschmiert.\n'
        'Und nach dem letzten Duell mit den Außerirdischen hast du dir\n'
        'eine Partie FIFA3093 an deiner PS217 verdient.\n'
        'Was ein Glück dass du viel Zeit hattest zu trainieren.\n'
        'Damit hast du die Außerirdischen im entscheidenden Finale besiegt!\n'
        '\n'
        '\n'
        '\n'
        'Du greifst nach deinem Controller...\n'
        '...und siehst gerade noch wie dich Fred,\n'
        'die mutierte Weltraumratte, höhnisch angrinst\n'
        'und mit dem Controller in den Pfoten im nächsten Raum verschwindet!\n'
        'Er hat dir wohl die 17:0 Pleite immer noch nicht verziehen...\n')
    sleep(0.5)

def grundriss():
    print ('\nHier ein Grundriss deines Raumgleiters:\n')
    print("""
                ______
               |      |
               |Brücke|
               |      |
               |__  __|
                __||__
               |      |
               | Gang |
               |      |
               |__  __|
       ______   __||__   ______
      |      | |      | | Ret- |
      | Bad  |_|Kreu- |_|tungs-|
      |       _ zung   _ kapsel|
      |______| |__  __| |_ ____|
                __||__   //
               |      | //
               |Kajüte|//
               |       /
               |______|

    """)

def wuerfelspiel():
    farben = ('Blau', 'Grün', 'Schwarz', 'Weiß')
    farbe = random.choice(farben)
    print(f'\nDer Würfel zeigt die Farbe {farbe} an!\n')
    if 'Weiß' in farbe:
        print('\nDu siehst wie sich das Alien durch die Kajüte schwabbelt\n'
              'und dabei durchseitig wird. Sein Tentakel würgt Fred.\n'
              'Die Wand schmilzt und plötzlich tut sich ein Loch auf\n'
              'durch das das Alien ins Weltall entkommt.\n')
        antwort_wuerfelspiel = input('Was machst du? Folgen oder zum\n\n'
              'MediaMarktPlanet für einen neuen Controller?\n\n').lower()
        if 'mediamarktplanet' in antwort_wuerfelspiel:
            print('\nAlle PS-Controller sind ausverkauft und deswegen\n'
                  'kaufst du dir die XBOX3001 mit drei Ersatzcontrollern\n'
                  'und vielen aktuellen Spielen.\n')
            das_ende()
        elif 'folgen' in antwort_wuerfelspiel:
            print('\nDu folgst Fred, den du noch sehen kannst,\n'
                  'in dem frisch gedruckten Raumanzug mit Raketenrucksack.\n'
                  'Was ein Glück, dass in jedem Raum ein 3D-Drucker steht.\n'
                  'Du holst den Alien ein. Dieser lässt Fred los, damit\n'
                  'er schneller vor der Weltraumpolizei, die du schon hören\n'
                  'kannst, fliehen kann. Du fliegst mit Fred nach Hause.\n'
                  'Er sagt dir, dass der Controller in der Rettungskapsel\n'
                  'versteckt ist und gibt Johnny auch den Ölvorrat wieder.\n'
                  'Er sagt euch auch das Passwort "Fred_ist_cool".\n'
                  'Ihr geht in die Rettungskapsel.\n')
            raum6()
        else:
            print('\n&)(/=)()")()="/==§\n')
            wuerfelspiel()
    elif 'Blau' in farbe:
        print('\nDas Alien verwandelt sich in einen Kraken und das Schiff\n'
              'wird langsam geflutet und der Inhalt wird zu Korallen und\n'
              'bunten, tropischen Fischen transformiert. Die Wände werden\n'
              'zu Glas und du befindest dich in einem Aquarium.\n'
              'An den Scheiben drücken sich kleine Kinder die Nasen platt.\n'
              'Du hast dich in einen Clownfisch verwandelt.')
        sleep(5.73)
        das_ende()
    elif 'Grün' in farbe:
        print('\nDas Alien sieht ein, dass es verloren hat und schmilzt wie\n'
              'ein Eisberg in Afrikas Savanne. Aus Dankbarkeit sagt Fred dir\n'
              'wo er den Controller versteckt hat: In der Rettungskapsel\n'
              'gesichert mit dem Passwort "Fred_ist_cool".\n')
        raum6()
    elif 'Schwarz' in farbe:
        print('\nDas Alien fängt auf mysteriöse Art und Weise an zu\n'
              'verschwinden. Als der letzte Tropfen Schleim und der letzte\n'
              'verschwunden ist, verschwindet auf genauso mysteriöse Weise\n'
              'die schwarze Farbe auf dem Würfel und wird zu einer\n'
              'Bombenuhr. Sie zeigt 60 Sekunden an.')
        antwort_bombe = input('Was machst du?\n\n').lower()
        print('\n###########################################################\n'
              '\n'
              'Antwort1: Du lässt Johnny die Bombe entschärfen.\n'
              'Antwort2: Du rufst dein Oma an und fragst sie um Rat!\n'
              'Antwort3: Du zertrittst den Würfel.\n'
              'Antwort4: Du verschluckst den Würfel.\n'
              'Antwort5: Du läufst weg!\n'
              '\n##########################################################\n')
        if 'antwort1' in antwort_bome:
            print('\nJohnny hat keinen guten Tag und er durchtrennt das\n'
                  'falsche Kabel. Das Raumschiff explodiert!')
            das_ende()
        elif 'antwort2' in antwort_bombe:
            print('\nOmas wissen alles und du kannst mit ihrer Hilfe die\n'
                  'Bombe entschärfen und du bist gerettet. Zum Schluss lädt\n'
                  'sie dich zum Truthahn essen ein. Leider ist der immer\n'
                  'angebrannt. :( . Die schwarze Farbe auf dem Würfel\n'
                  'erscheint wieder und du kannst erneut würfeln.\n')
            wuerfelspiel()
        elif 'antwort3' in antwort_bombe:
            print('\nUnter dir erscheint ein schwarzes Loch.\n')
            das_ende()
        elif 'antwort4' in antwort_bombe:
            print('\nDu zerfällst in Pixel und landest in der Minecraftwelt.\n')
            das_ende()
        elif 'antwort5' in antwort_bombe:
            print('\nDu stolperst und verlierst das Bewusstsein.\n'
                  'Die Bombe explodiert und dadurch gibt es ein Riss im\n'
                  'Raum-Zeit-Kontinuum und du bist am Anfang der Geschichte\n'
                  'ohne dass du dich erinnern kannst.')
            sleep(3)
            main()
        else:
            print('\nMcDonalds - Ich liebe es: "/)/&(/=(/=")(=)"))"\n'
                  '\n'
                  '(@_@)\n')
            sleep(2)
            wuerfelspiel()
    else:
        print('\nBei Risiken und Nebenwirkungen fressen Sie die\n'
              'Packungsbeilage oder schlagen Sie Ihren Apotheker.\n')

def das_ende():
    print("""
        #######
        #       #    # #####  ######
        #       ##   # #    # #
        #####   # #  # #    # #####
        #       #  # # #    # #
        #       #   ## #    # #
        ####### #    # #####  ######
    """)
    sleep(5)

def raum6():
    print('\nDu stehst in der Rettungskapsel. Es ist klein und eng hier.\n')

    kapsel = input('Sprachassistent: "Wie lautet dein Befehl?"\n\n').lower()

    if 'fred_ist_cool' in kapsel:
        print('\nDer Tresor öffnet sich. Dein Controller liegt auf einem\n'
              'roten Samtkissen - mit Nachos übergossen. Du renigst ihn,\n'
              'isst die Nachos und gehst zur Brücke und zockst FIFA3093.\n')
        das_ende()
    else:
        print('\nDer Sprachassistent gibt unverständliche Knackgeräusche\n'
              'von sich. Der Assistent startet die Rettungskapsel und du\n'
              'fliegst an der Brücke vorbei. Dort siehst du Fred mit deinem\n'
               'Ersatzcontroller an der PS217 zocken. Danach kehrst du zur\n'
               'Station zurück. Du gehst in den Gang.\n')
        raum3()

def raum5():
    print('\nIhr geht in die Kajüte und dort steht das Bett mit den Gurten.\n'
          'Die Fenster sind mit Gardinen verhangen. Ein roter Schreibtisch\n'
          'mit Zeichnungen steht in einer Ecke. Davor seht ihr ein Alien.\n'
          'In der einen Tentakel hält es Fred gefangen.\n'
          'Es fordert dich heraus:"Wenn du Fred wiederhaben möchtest,"\n'
          'dann musst du gegen mich im Würfelspiel gewinnen!\n'
          'Du musst nur Grün würfeln!"\n')

    alien = input('Möchtest du annehmen oder kämpfen?\n\n').lower()
    if 'annehmen' in alien:
        wuerfelspiel()
    else:
        print('\nDas Alien lacht dich aus!\n'
              '\n'
              ':D\n')
        sleep(3)
        raum5()

def raum4():
    print('\nIhr steht im Badezimmer. Der Boden ist weiß gekachelt.\n'
          'Es hängt ein in Orange umrandeter Spiegel an der Wand.\n'
          'Die Anschnallgurte der Toilette flattern merkwürdig.\n'
          'Du spürst eine eisige Kälte und guckst zu der Luke.\n'
          'Du entdeckst ein kleines Loch in der Luke.\n')

    antwort_bad = input('Was tust du? Loch stopfen oder fliehen?\n\n').lower()

    if 'stopfen' in antwort_bad:
        print('\nDu stopfst gerade rechtzeitig die Watte vom Boden ins Loch\n'
             'und anschließend durchsuchst du das Bad nach dem Controller.\n'
             'Du findest keine Spur von Fred und deinem Controller.\n'
             'Du verlässt das Bad.\n')
        raum3()
    elif 'fliehen' in antwort_bad:
        print('\nDu probierst zu fliehen, doch die letzten Teile der Luke\n'
              'verschwinden im Weltall. Der Sog reißt dich ins Weltall\n'
              'und du landest mit Johnny auf einem nahe gelegenen Planeten.\n'
              'Gott sei dank kann sich Johnny in eine Rettungskapsel\n'
              'verwandeln. Du entdeckst eine fremde Zivilisation.\n')
        das_ende()
    else:
        print('\nIch verstehe die Antwort nicht - bitte nur ein Wort!\n')
        raum4()

def raum3():
    print('\nIhr steht in einem Raum, von dem drei weitere Räume abgehen.\n'
          'Von Fred keine Spur!\n'
          '\n'
          'Was macht ihr?\n'
          '\n##############################################################\n'
          '\n'
          'Antwort1: Yoga - das hilft immer!\n'
          'Antwort2: Wir gehen ins Badezimmer.\n'
          'Antwort3: Wir suchen die Kajüte auf.\n'
          'Antwort4: Bestimmt ist Fred bei der Rettungskapsel! Hinterher!\n'
          'Antwort5: Fred ist sicher zurück geschlichen! Auf zur Brücke!\n'
          '\n##############################################################\n')

    antwort_raum3 = input('> ').lower()

    if 'antwort1' in antwort_raum3:
        print('\nDein Roboter ist viel sportlicher als du!\n'
              'Du schämst dich.\n')
        raum3()
    elif 'antwort2' in antwort_raum3:
        raum4()
    elif 'antwort3' in antwort_raum3:
        raum5()
    elif 'antwort4' in antwort_raum3:
        raum6()
    elif 'antwort5' in antwort_raum3:
        print('\nDu denkst nochmal genauer darüber nach.\n'
              'Eigentlich bist du dir doch sicher, dass er woanders ist.\n')
        raum3()
    else:
        print('\nATEMLOS DURCH DIE NACHT,\n'
              'BIS EIN NEUER TAG ERWACHT...\n')
        sleep(3)
        print('\n(@_@)\n')
        sleep(2)
        raum3()

def raum2():
    print('\nDu rennst Fred hinterher und stehst in einem kurzen Korridor.\n'
        'Gegenüber gibt es einen Durchgang. Fred ist nicht hier.\n'
        'Dafür aber Journey2 genannt Johnny - dein Roboter.\n'
        'Es ist das neueste Modell. Er kann viele coole Tricks.\n'
        'Johnny spricht dich an:\n'
        '\n'
        '"Warum rennst du so?"\n'
        '\n################################################################\n'
        '\n'
        'Antwort1: "Fred hat meinen Controller geklaut!"\n'
        'Antwort2: "Dies ist mein Frühsport!"\n'
        '\n################################################################\n')

    antwort_raum2 = input('> ').lower()

    if 'antwort1' in antwort_raum2:
        print('\n"Das sieht ihm mal wieder ähnlich!\n'
              'Bestimmt hat er auch meinen Ölvorrat versteckt.\n'
              'Ich helfe dir natürlich, um es ihm heim zu zahlen!"\n'
              'Ihr geht den Korridor entlang in den nächsten Raum.\n')
        raum3()
    elif 'antwort2' in antwort_raum2:
        print('\n"Das ist sehr vernünftig.\n'
              'Vielleicht sollte ich auch mehr Sport treiben.\n'
              'Ich begleite dich."\n'
              'Ihr sprintet in den nächsten Raum.\n')
        raum3()
    else:
        print('\n???\n'
              'Bitte gib Antwort1 oder Antwort2 ein!\n')
        sleep(2)
        raum2()

def raum1():
    aktion = input('Was machst du? Stürzt du der Ratte nach?\n\n').lower()

    if 'ja' in aktion:
        raum2()
    elif 'nein' in aktion:
        print('\nDu schaust dich auf der Brücke kurz um,\n'
              'aber findest nichts, was dir weiterhilft.\n')
        raum1()
    else:
        print('\nIch bin leider nur ein dummes Computerprogramm.\n'
              'Ich brauche klare Anweisungen: "ja" oder "nein"!\n')
        raum1()

def main():
    cover()
    einfuehrung()
    grundriss()
    raum1()


main()
