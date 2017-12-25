import colors as clr
import logging as lg

def debugLevel():
    lg.basicConfig(level=lg.DEBUG)

def critical(msg):
    clr.crit()
    lg.critical(msg)
    clr.reset()

def info(msg):
    clr.blue()
    lg.info(msg)
    clr.reset()

def warning(msg):
    clr.yellow()
    lg.warning(msg)
    clr.reset()

def error(msg):
    clr.red()
    lg.error(msg)
    clr.reset()

def debug(msg):
    clr.green()
    lg.debug(msg)
    clr.reset()
