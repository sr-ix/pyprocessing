import math
import pyglet.gl as gl

#************************
#  CONSTANTS
#************************

version = "0.1.3.10" # This version of pyprocessing

#keycodes
F1 = 65470
F2 = 65471
F3 = 65472
F4 = 65473
F5 = 65474
F6 = 65475
F7 = 65476
F8 = 65477
F9 = 65478
F10 = 65479
F11 = 65480
F12 = 65481
F13 = 65482
F14 = 65483
F15 = 65484
F16 = 65485
LSHIFT = SHIFT = 65505
RSHIFT = 65506
LCTRL = CTRL = 65507
RCTRL = 65508
CAPSLOCK = 65509
LMETA = META = 65511
RMETA = 65512
LALT = ALT = 65513
RALT = 65514
LWINDOWS = WINDOWS = 65515
RWINDOWS = 65516
LCOMMAND = COMMAND = 65517
RCOMMAND = 65518
LOPTION = 65488
ROPTION = 65489
BACKSPACE = 65288
TAB = 65289
LINEFEED = 65290
CLEAR = 65291
RETURN = 65293
ENTER = 65293
PAUSE = 65299
SCROLLLOCK = 65300
SYSREQ = 65301
ESCAPE = 65307
HOME = 65360
LEFT = 65361
UP = 65362
RIGHT = 65363
DOWN = 65364
PAGEUP = 65365
PAGEDOWN = 65366
END = 65367
BEGIN = 65368
DELETE = 65535
SELECT = 65376
PRINT = 65377
EXECUTE = 65378
INSERT = 65379
UNDO = 65381
REDO = 65382
MENU = 65383
FIND = 65384
CANCEL = 65385
HELP = 65386
BREAK = 65387

CODED = '\0'

#rectmode/ellipsemode/mousebutton
CORNER = 1
CORNERS = 2
CENTER = 3
RADIUS = 4

#textalign
TOP = 7
BOTTOM = 8
BASELINE = 9

# this maps Processing constants to strings used by pyglet's text
# rendering subsystem
textAlignConst = {LEFT:'left', RIGHT:'right',
                  CENTER:'center', TOP:'top',
                  BOTTOM:'bottom', BASELINE:'baseline'}

# colorMode
RGB=0
HSB=1

# math
PI = math.pi
TWO_PI = PI*2
HALF_PI = PI/2

# hints
ENABLE_DEPTH_TEST = 'ENABLE_DEPTH_TEST'
DISABLE_DEPTH_TEST = 'DISABLE_DEPTH_TEST'
DISABLE_POLYGON_SMOOTH = 'DISABLE_POLYGON_SMOOTH'
DOUBLE_FLIP_POLICY = 'DOUBLE_FLIP_POLICY'
SINGLE_FLIP_POLICY = 'SINGLE_FLIP_POLICY'
FBO_FLIP_POLICY = 'FBO_FLIP_POLICY'
ACCUM_FLIP_POLICY = 'ACCUM_FLIP_POLICY'
BACKUP_FLIP_POLICY = 'BACKUP_FLIP_POLICY'

#filter modes
THRESHOLD = 'THRESOLD'
GRAY = 'GRAY'
INVERT = 'INVERT'
POSTERIZE = 'POSTERIZE'
BLUR = 'BLUR'
OPAQUE = 'OPAQUE'
ERODE = 'ERODE'
DILATE = 'DILATE'

# shapes 
POINTS = gl.GL_POINTS
LINES = gl.GL_LINES
TRIANGLES = gl.GL_TRIANGLES
TRIANGLE_FAN = gl.GL_TRIANGLE_FAN
TRIANGLE_STRIP = gl.GL_TRIANGLE_STRIP
QUADS = gl.GL_QUADS 
QUAD_STRIP = gl.GL_QUAD_STRIP
CLOSE = 1

#blend modes
BLEND, ADD, SUBTRACT, DARKEST, LIGHTEST, DIFFERENCE, EXCLUSION, \
MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN = range(14)

#texture modes
NORMALIZED = 'NORMALIZED'
IMAGE = 'IMAGE'

# image formats
RGB = 'RGB'
ARGB = 'RGBA'
ALPHA = 'A'

# cursor types
ARROW = None
CROSS = 'crosshair'
HAND = 'hand'
MOVE = 'size'
TEXT = 'text'
WAIT = 'wait'

#perlin noise table
perlin = (
151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,
30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,
62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,
125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,
83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,
143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,
196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,
250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,
58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,
221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,
224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,
12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,
199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,
205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180,
151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,
30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,
62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,
125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,
83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,
143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,
196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,
250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,
58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,
221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,
224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,
12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,
199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,
205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180)
