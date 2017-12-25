import sys
import os


"""
Colors text in console mode application (win32).
Uses ctypes and Win32 methods SetConsoleTextAttribute and
GetConsoleScreenBufferInfo.

$Id: color_console.py 534 2009-05-10 04:00:59Z andre $
"""

from ctypes import windll, Structure, c_short, c_ushort, byref

SHORT = c_short
WORD = c_ushort

class COORD(Structure):
  """struct in wincon.h."""
  _fields_ = [
    ("X", SHORT),
    ("Y", SHORT)]

class SMALL_RECT(Structure):
  """struct in wincon.h."""
  _fields_ = [
    ("Left", SHORT),
    ("Top", SHORT),
    ("Right", SHORT),
    ("Bottom", SHORT)]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
  """struct in wincon.h."""
  _fields_ = [
    ("dwSize", COORD),
    ("dwCursorPosition", COORD),
    ("wAttributes", WORD),
    ("srWindow", SMALL_RECT),
    ("dwMaximumWindowSize", COORD)]

# winbase.h
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# wincon.h
FOREGROUND_BLACK     = 0x0000
FOREGROUND_BLUE      = 0x0001
FOREGROUND_GREEN     = 0x0002
FOREGROUND_CYAN      = 0x0003
FOREGROUND_RED       = 0x0004
FOREGROUND_MAGENTA   = 0x0005
FOREGROUND_YELLOW    = 0x0006
FOREGROUND_GREY      = 0x0007
FOREGROUND_INTENSITY = 0x0008 # foreground color is intensified.

BACKGROUND_BLACK     = 0x0000
BACKGROUND_BLUE      = 0x0010
BACKGROUND_GREEN     = 0x0020
BACKGROUND_CYAN      = 0x0030
BACKGROUND_RED       = 0x0040
BACKGROUND_MAGENTA   = 0x0050
BACKGROUND_YELLOW    = 0x0060
BACKGROUND_GREY      = 0x0070
BACKGROUND_INTENSITY = 0x0080 # background color is intensified.

stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo

def get_text_attr():
  """Returns the character attributes (colors) of the console screen
  buffer."""
  csbi = CONSOLE_SCREEN_BUFFER_INFO()
  GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
  return csbi.wAttributes

def set_text_attr(color):
  """Sets the character attributes (colors) of the console screen
  buffer. Color is a combination of foreground and background color,
  foreground and background intensity."""
  SetConsoleTextAttribute(stdout_handle, color)


def printRed(t, end=''):
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_RED | default_bg |
                     FOREGROUND_INTENSITY)
  print(t, end=end)
  sys.stdout.flush()
  set_text_attr(default_colors)

def printBlue(t, end=''):
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_BLUE | default_bg |
                     FOREGROUND_INTENSITY)
  print(t, end=end)
  sys.stdout.flush()
  set_text_attr(default_colors)

def printGreen(t, end=''):
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_GREEN | default_bg |
                     FOREGROUND_INTENSITY)
  print(t, end=end)
  sys.stdout.flush()
  set_text_attr(default_colors)

def printYellow(t, end=''):
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_YELLOW | default_bg |
                     FOREGROUND_INTENSITY)
  print(t, end=end)
  sys.stdout.flush()
  set_text_attr(default_colors)

def printCyan(t, end=''):
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_CYAN | default_bg |
                     FOREGROUND_INTENSITY)
  print(t, end=end)
  sys.stdout.flush()
  set_text_attr(default_colors)

def red():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_RED | default_bg |
                     FOREGROUND_INTENSITY)
def blue():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_BLUE | default_bg |
                     FOREGROUND_INTENSITY)

def yellow():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_YELLOW | default_bg |
                     FOREGROUND_INTENSITY)
def crit():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_GREY | BACKGROUND_RED |
                     FOREGROUND_INTENSITY)

def cyan():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_CYAN | default_bg |
                     FOREGROUND_INTENSITY)

def green():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_GREEN | default_bg |
                     FOREGROUND_INTENSITY)

def grey():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_GREY | default_bg |
                     FOREGROUND_INTENSITY)

def reset():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(FOREGROUND_GREY | BACKGROUND_BLACK)

def resete():
  default_colors = get_text_attr()
  default_bg = default_colors & 0x0070
  default_fg = default_colors & 0x0007
  set_text_attr(default_colors)
