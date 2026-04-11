from typing import Any
import AiLangType
from grammar.AiLangParser import AiLangParser as ap
from utils import getTerminalSymbol, Singleton


class AiLangObj:

    def __init__(self, id, val=None, parent=None):
        self.id = id
        self.val: AiLangType.AiLangType | None = val
        self.parent: AiLangObj | None = parent
        self.members: dict[str, AiLangObj] = {}

    def killMembers(self) -> None:
        self.members = {}

    def get(self) -> AiLangType.AiLangType:
        if self.val is None:
            raise ValueError("No Type to get")
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

    def setMember(self, member):
        self.members[member.id] = member

    def getMember(self, id) -> None | AiLangObj:
        if id in self.members:
            return self.members[id]
        else:
            return None

    def getLast(self) -> AiLangObj:
        if len(self.members) == 0:
            return self
        memb = list(self.members.values())

        return memb[0].getLast()

    def getDFItemByID(self, id):
        items = filter(
            lambda v: isinstance(v.val, AiLangType.DfItem), list(self.members.values())
        )
        for item in items:
            if item.id == id:
                return item

    @staticmethod
    def make(node: ap.AssignableContext) -> AiLangObj:
        if isinstance(node, ap.SimpleTargetContext):
            id = getTerminalSymbol(node)
            return AiLangObj(id)
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
        return f"{self.id}({str(type(self.val))}) -> {repr(self.members)}"


class NoneObj(AiLangObj, metaclass=Singleton):
    def __init__(self):
        super().__init__("None", AiLangType.NoneType(), None)


def evalMember(node, parent):
    if isinstance(node, (ap.BasicIDMemberContext, ap.IntIDMemberContext)):
        return AiLangObj(getTerminalSymbol(node), parent=parent)
    if isinstance(node, ap.ListIDMemberContext):
        raise NotImplementedError()
