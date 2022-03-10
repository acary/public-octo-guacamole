# This Python3 script takes a musical key as user input
# and displays relevant information about the key.
#
# To run:
# - Save the file to a location on your computer
# - Using a terminal, run: `python3 dictionary_music.py`
#   (where `dictionary_music.py` is the file name)

def main():

    print("\n*********** MUSICAL KEY REFERENCE ***********")

    print("* At the prompt, enter the music key to look up.")
    print("* To view all, enter 'all'")
    print("* To exit program, enter 'quit'")

    music_keys = {
      'C':
        {
            'key'           : 'C',
            'scales'        : 'C',
            'major_minor'   : 'C',
            'neighbor'      : 'C',
            'voicings'      : 'C',
            'progressions'  : 'C',
        },
      'C#':
        {
            'key'           : 'C#',
            'scales'        : 'C#',
            'major_minor'   : 'C#',
            'neighbor'      : 'C#',
            'voicings'      : 'C#',
            'progressions'  : 'C#',
        },
      'D':
        {
            'key'           : 'D',
            'scales'        : 'D',
            'major_minor'   : 'D',
            'neighbor'      : 'D',
            'voicings'      : 'D',
            'progressions'  : 'D',
        },
      'Eb':
        {
            'key'           : 'Eb',
            'scales'        : 'Eb',
            'major_minor'   : 'Eb',
            'neighbor'      : 'Eb',
            'voicings'      : 'Eb',
            'progressions'  : 'Eb',
        },
      'E':
        {
            'key'           : 'E',
            'scales'        : 'E',
            'major_minor'   : 'E',
            'neighbor'      : 'E',
            'voicings'      : 'E',
            'progressions'  : 'E',
        },
      'F':
        {
            'key'           : 'F',
            'scales'        : 'F',
            'major_minor'   : 'F',
            'neighbor'      : 'F',
            'voicings'      : 'F',
            'progressions'  : 'F',
        },
      'F#':
        {
            'key'           : 'F#',
            'scales'        : 'F#',
            'major_minor'   : 'F#',
            'neighbor'      : 'F#',
            'voicings'      : 'F#',
            'progressions'  : 'F#',
        },
      'G':
        {
            'key'           : 'G',
            'scales'        : 'G',
            'major_minor'   : 'G',
            'neighbor'      : 'G',
            'voicings'      : 'G',
            'progressions'  : 'G',
        },
      'Ab':
        {
            'key'           : 'Ab',
            'scales'        : 'Ab',
            'major_minor'   : 'Ab',
            'neighbor'      : 'Ab',
            'voicings'      : 'Ab',
            'progressions'  : 'Ab',
        },
      'A':
        {
            'key'           : 'A',
            'scales'        : 'A',
            'major_minor'   : 'A',
            'neighbor'      : 'A',
            'voicings'      : 'A',
            'progressions'  : 'A',
        },
      'Bb':
        {
            'key'           : 'Bb',
            'scales'        : 'Bb',
            'major_minor'   : 'Bb',
            'neighbor'      : 'Bb',
            'voicings'      : 'Bb',
            'progressions'  : 'Bb',
        },
      'B':
        {
            'key'           : 'B',
            'scales'        : 'B',
            'major_minor'   : 'B',
            'neighbor'      : 'B',
            'voicings'      : 'B',
            'progressions'  : 'B',
        },
      }

    while True:
        user_input = input("\nEnter a musical key: ")
        if user_input == 'quit':
            quit()
        if user_input == 'all':
            print_all(music_keys)
        else:
            get_key_info(music_keys, user_input)



def get_key_info(music_keys, user_input):
    print(
        '\n* key: ' + music_keys[user_input]['key'] +
        '\n* scales: ' + music_keys[user_input]['scales'] +
        '\n* major_minor: ' + music_keys[user_input]['major_minor'] +
        '\n* neighbor: ' + music_keys[user_input]['neighbor'] +
        '\n* voicings: ' + music_keys[user_input]['voicings'] +
        '\n* progressions: ' + music_keys[user_input]['progressions'] + '\n'
    )

def print_all(music_keys):
    print()
    for k, v in music_keys.items():
        print(k + ':\n\t' +
                'key: ' + str(v['key']) + '\n\t'
                'scales: ' + str(v['scales']) + '\n\t'
                'major_minor: ' + str(v['major_minor']) + '\n\t'
                'neighbor: ' + str(v['neighbor']) + '\n\t'
                'voicings: ' + str(v['voicings']) + '\n\t'
                'progressions: ' + str(v['progressions']) + '\n\t'
            )

if __name__ == "__main__":
    main()
