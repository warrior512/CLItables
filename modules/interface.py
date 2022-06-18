from colorama import init, Fore, Back, Style
import os

init(autoreset=True)

byl = Back.YELLOW
sra = Style.RESET_ALL
fbc = Fore.BLACK
fyl = Fore.YELLOW
sbr = Style.BRIGHT


def print_logo():
    os.system('clear')
    print(fyl + sbr + '''\n ____  ____  ____  ____  ____  ____ 
||t ||||a ||||b ||||l ||||e ||||s ||
||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\|

          --------------------------
          |  id  |  name  |  tel
          --------------------------
          |  01  |  Ivan  |  +7(915)

(c) 2022  nikolaysmirnov86@gmail.com
 ''')


def main_menu():
    new_t = byl + fbc + 'n' + sra + fyl + sbr + 'ew'
    open_t = byl + fbc + 'o' + sra + fyl + sbr + 'pen'
    exit_p = fyl + sbr + 'e' + sra + byl + fbc + 'x' + sra + fyl + sbr + 'it'
    list_t = byl + fbc + 'l' + sra + fyl + sbr + 'ist'
    delete_t = byl + fbc + 'd' + sra + fyl + sbr + 'el'
    print('\n' + new_t, open_t, list_t, exit_p, delete_t + Style.RESET_ALL + '\n')


def open_menu():
    add_row_t = byl + fbc + 'a' + sra + fyl + sbr + 'dd' + sra + byl + fbc + 'r' + sra + fyl + sbr + 'ow'
    add_col = byl + fbc + 'a' + sra + fyl + sbr + 'dd' + sra + byl + fbc + 'c' + sra + fyl + sbr + 'ol'
    save = byl + fbc + 's' + sra + fyl + sbr + 'ave'
    exit_t = fyl + sbr + 'e' + sra + byl + fbc + 'x' + sra + fyl + sbr + 'it'
    del_row = byl + fbc + 'd' + sra + fyl + sbr + 'el' + sra + byl + fbc + 'r' + sra + fyl + sbr + 'ow'
    del_col = byl + fbc + 'd' + sra + fyl + sbr + 'el' + sra + byl + fbc + 'c' + sra + fyl + sbr + 'ol'
    edit = byl + fbc + 'e' + sra + fyl + sbr + 'dit'
    search = byl + fbc + 's' + sra + fyl + sbr + 'earc' + sra + byl + fbc + 'h' + sra
    help_m = byl + fbc + 'h' + sra + fyl + sbr + 'elp' + sra
    print('\n' + add_row_t, add_col, edit, search,  help_m + '\n\n' + del_row, del_col, save, exit_t + '\n')


def search_menu():
    exit_s = fyl + sbr + 'e' + sra + byl + fbc + 'x' + sra + fyl + sbr + 'it'
    save_s = byl + fbc + 's' + sra + fyl + sbr + 'ave'
    search = byl + fbc + 's' + sra + fyl + sbr + 'earc' + sra + byl + fbc + 'h' + sra
    print('\n' + exit_s, save_s, search + '\n')

