import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType
from kmk.hid import HIDModes
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.digitalio import KeysScanner

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
 
layers_ext = Layers()
keyboard.modules.append(layers_ext)

# MATRIX
keyboard.matrix = MatrixScanner(
    column_pins=(board.D3, board.D6, board.D10),  # COL0, COL1, COL2
    row_pins=(board.D0, board.D1, board.D2),       # ROW0, ROW1, ROW2
    columns_to_anodes=True,                         # COL2ROW diode direction
)

# ENCODER CLICK
encoder_click = KeysScanner(
    pins=(board.D9,),  # EC11SWA on GP4 = D9 on XIAO
)
keyboard.matrix = [keyboard.matrix, encoder_click]

# ENCODER ROTATION
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D8, board.D7, None),)  # A=GP2, B=GP1, no push pin

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),  # Windows
    ((KC.VOLD, KC.VOLU),),  # Mac
]
keyboard.modules.append(encoder_handler)


# Shortcut to toggle between layers
TOGGLE_OS = KC.TG(1)

keyboard.keymap = [

    # Windows
    [
        KC.MPRV,           KC.MPLY,           KC.MNXT,   
        KC.LCTL(KC.Z),     KC.LCTL(KC.C),     KC.LCTL(KC.V), 
        KC.PSCR,           KC.SLEP,           KC.SCRL,   
        TOGGLE_OS,                                   
    ],

    #Mac
    [
        KC.MPRV,                    KC.MPLY,              KC.MNXT,   
        KC.LGUI(KC.Z),              KC.LGUI(KC.C),        KC.LGUI(KC.V), 
        KC.LGUI(KC.LSFT(KC.N4)),    KC.SLEP,              KC.SCRL,   
        TOGGLE_OS,                                                   
    ],
]

# OLED DISPLAY
oled_ext = Oled(
    OledDisplayMode.TXT,
    toDisplay="Command Node",
    flip=False,
)
keyboard.extensions.append(oled_ext)

# START
if __name__ == '__main__':
    keyboard.run()