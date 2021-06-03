#!/usr/bin/env python

from blessed import Terminal

menu = [["login to system"], ["create account"], ["disconnect"]]


def display_screen(selection):
    term = Terminal()
    print (term.clear())

    for (idx, m) in enumerate(menu):
        if idx == selection:
            print('{t.bold_red_reverse}{title}'.format(t=term, title=m[0]))
        else:
            print('{t.normal}{title}'.format(t=term, title=m[0]))


def run_selection(selection):
    print (term.green_reverse('Running {}'.format(menu[selection][0])))


def main():
    term = Terminal()
    with term.fullscreen():
        selection = 0
        display_screen(selection)
        selection_inprogress = True
        with term.cbreak():
            while selection_inprogress:
                key = term.inkey()
                if key.is_sequence:
                    if key.name == 'KEY_TAB':
                        selection += 1
                    if key.name == 'KEY_DOWN':
                        selection += 1
                    if key.name == 'KEY_UP':
                        selection -= 1
                    if key.name == 'KEY_ENTER':
                        selection_inprogress = False
                elif key:
                    print("got {0}.".format(key))

                selection = selection % len(menu)

                display_screen(selection)

    run_selection(selection)

main()