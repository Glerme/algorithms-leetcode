class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value
      
      
dll = DoublyLinkedList()

# Teste 1: Adicionar elementos no início
print("Adicionando ao início:")
dll.add_to_front(10)
dll.add_to_front(20)
dll.add_to_front(30)
print("Lista após adicionar ao início: 30 -> 20 -> 10")

# Teste 2: Adicionar elementos no final
print("\nAdicionando ao final:")
dll.add_to_end(40)
dll.add_to_end(50)
print("Lista após adicionar ao final: 30 -> 20 -> 10 -> 40 -> 50")

# Teste 3: Remover do início
print("\nRemovendo do início:")
print("Removido:", dll.remove_from_front())
print("Lista após remover do início: 20 -> 10 -> 40 -> 50")

# Teste 4: Remover do final
print("\nRemovendo do final:")
print("Removido:", dll.remove_from_end())
print("Lista após remover do final: 20 -> 10 -> 40")

# Teste 5: Lista vazia
print("\nRemovendo de uma lista vazia:")
dll = DoublyLinkedList()  # Criando uma nova lista vazia
print("Removido do início:", dll.remove_from_front())
print("Removido do final:", dll.remove_from_end())