@dataclass
class Node:
    val: str
    children: dict[str, Node]
    leaf: bool = False

    def get_child(self, k: str) -> Optional[Node]:
        return self.children.get(k)

    def get_or_add_child(self, k: str, is_word: bool) -> Node:
        n = self.children.setdefault(k, Node(k, {}, leaf=is_word))
        # Potentially update leaf status if child wasn't before but is are now
        # Probably shouldn't happen since our words are sorted, but who knows?
        if is_word:
            n.leaf = True
        return n


class Trie:
    root: Node

    def __init__(self):
        self.root = Node("", {}, leaf=False)

    @classmethod
    def from_file(cls, file_name: str) -> Trie:
        t = Trie()
        with open(file_name) as f:
            for line in f:
                t.add(line.strip())
        return t

    def add(self, word: str):
        cur_node = self.root
        for i, c in enumerate(word):
            cur_node = cur_node.get_or_add_child(c, i == len(word) - 1)

    def _child_node(self, word: str) -> Optional[Node]:
        cur_node = self.root
        for c in word:
            cur_node = cur_node.get_child(c)
            if cur_node is None:
                return None
        return cur_node

    def is_prefix_or_word(self, word: str) -> tuple[bool, bool]:
        n = self._child_node(word)
        if n is None:
            return (False, False)
        return (len(n.children) > 0, n.leaf)
