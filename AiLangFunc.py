from AiLangObj import AiLangObj
import AiLangType
from grammar.AiLangParser import AiLangParser as ap
from utils import getTerminalSymbol

class AiLangFunc:
    def __init__(self, func, args):
        self.func = func
        self.args:list[AiLangObj] = args
    
    def call(self, args):
        self.func(*args)

    def make(self, node):
        raise NotImplementedError()