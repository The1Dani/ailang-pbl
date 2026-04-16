import pandas as pd

import AiLangType
from grammar.AiLangParser import AiLangParser as ap
from utils import getTerminalSymbol, Singleton


class AiLangObj:
    """AiLang Object Implementation, This class wraps AiLang, This is used to assosiate objects"""

    def __init__(self, ident, val: AiLangType.AiLangType | None = None, parent=None):
        self.ident: str = ident
        self.val: AiLangType.AiLangType | None = val
        self.parent: AiLangObj | None = parent
        self.members: dict[str, AiLangObj] = {}

    def killMembers(self) -> None:
        self.members = {}

    def get(self) -> AiLangType.AiLangType:
        if self.val is None:
            return AiLangType.NoneType()
        return self.val

    def getParent(self) -> AiLangObj:
        if self.parent:
            return self.parent
        raise ValueError("No parent")

    def getRoot(self) -> AiLangObj:
        if self.parent:
            return self.parent.getRoot()
        return self

    def set(self, val: AiLangType.AiLangType | None) -> None:
        self.val = val

    def setMember(self, member: AiLangObj):
        self.members[member.ident] = member

    def getMember(self, ident) -> None | AiLangObj:
        if ident in self.members:
            return self.members[ident]
        return None

    def getLast(self) -> AiLangObj:
        if len(self.members) == 0:
            return self
        memb = list(self.members.values())

        return memb[0].getLast()

    def getDFItemByID(self, ident) -> AiLangObj | None:
        items = filter(
            lambda v: isinstance(v.val, AiLangType.DfItem), list(self.members.values())
        )
        for item in items:
            if item.ident == ident:
                return item
        return None

    @staticmethod
    def make(node: ap.AssignableContext) -> AiLangObj:
        if isinstance(node, ap.SimpleTargetContext):
            ident = getTerminalSymbol(node)
            return AiLangObj(ident)
        if isinstance(node, ap.MemberTargetContext):
            ctx = node.getTypedRuleContext(ap.AssignableContext, 0)
            if ctx is None:
                raise ValueError()
            assignable_obj = AiLangObj.make(ctx)
            member_obj = evalMember(
                node.getTypedRuleContext(ap.MemberContext, 0), assignable_obj
            )
            assignable_obj.setMember(member_obj)
            return assignable_obj
        raise ValueError()

    def __repr__(self) -> str:
        return f"{self.ident}({str(type(self.val))}) {f"-> {repr(self.members)}" if len(self.members) > 0 else ""}"  # pylint: disable=line-too-long

    def update(self, other: AiLangObj) -> None:
        self.__dict__ = other.__dict__


class NoneObj(AiLangObj, metaclass=Singleton):
    """Object that is None in AiLang"""

    def __init__(self):
        super().__init__("None", AiLangType.NoneType(), None)


def evalMember(node, parent):
    if isinstance(node, (ap.BasicIDMemberContext, ap.IntIDMemberContext)):
        return AiLangObj(getTerminalSymbol(node), parent=parent)
    if isinstance(node, ap.ListIDMemberContext):
        raise NotImplementedError()
    raise ValueError()


def fromDFtoObj(ident: str, df: pd.DataFrame) -> AiLangObj:
    obj = AiLangObj(ident, AiLangType.DfType(df))
    for col, ser in df.items():
        column_obj = AiLangObj(col, AiLangType.DfItem(ser))
        obj.setMember(column_obj)
    return obj
