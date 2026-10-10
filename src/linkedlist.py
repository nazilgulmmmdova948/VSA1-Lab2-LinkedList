# Laboratoriya isi 1: Singly Linked List


# ---------- Tapshiriq 1: Node sinfi ----------
class Node:
    def __init__(self, data):
        self.data = data    # düyünün qiyməti
        self.next = None    # növbəti düyün (əvvəlcə yoxdur)


class LinkedList:
    def __init__(self):
        self.head = None    # siyahının başlanğıcı

    # ---------- Tapshiriq 2: sona elave et ----------
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:       # siyahı boşdursa
            self.head = new_node
            return
        current = self.head
        while current.next is not None:   # son düyünə qədər get
            current = current.next
        current.next = new_node

    # ---------- Tapshiriq 3: evvele elave et ----------
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ---------- Tapshiriq 4: verilmish elementden sonra elave et ----------
    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Element tapılmadı:", target)

    # ---------- Tapshiriq 5: element silme ----------
    def delete(self, value):
        if self.head is None:
            return
        # silinən element birinci düyündürsə
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next   # düyünü atlayırıq
                return
            current = current.next
        print("Silinəcək element tapılmadı:", value)

    # ---------- Tapshiriq 6: axtarish ----------
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False

    # ---------- Tapshiriq 7: uzunluq ----------
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # ---------- Tapshiriq 8: maksimum ve minimum ----------
    def find_max(self):
        if self.head is None:
            return None
        maximum = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            current = current.next
        return maximum

    def find_min(self):
        if self.head is None:
            return None
        minimum = self.head.data
        current = self.head.next
        while current is not None:
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return minimum

    # ---------- Tapshiriq 9: siyahini ters cevirmek ----------
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next    # növbətini yadda saxla
            current.next = previous     # oxu geri çevir
            previous = current
            current = next_node
        self.head = previous

    # siyahini ekrana cap etmek
    def display(self):
        current = self.head
        text = ""
        while current is not None:
            text += str(current.data) + " -> "
            current = current.next
        print(text + "None")


# ---------- Tapshiriq 10: telebe qeydiyyat sistemi ----------
class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, student_name, gpa):
        new_node = StudentNode(student_id, student_name, gpa)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_student(self, student_id):
        if self.head is None:
            return
        if self.head.student_id == student_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.student_id == student_id:
                current.next = current.next.next
                return
            current = current.next
        print("Tələbə tapılmadı:", student_id)

    def show_all(self):
        current = self.head
        while current is not None:
            print(current.student_id, current.student_name, current.gpa)
            current = current.next

    def show_high_gpa(self):
        current = self.head
        while current is not None:
            if current.gpa > 80:
                print(current.student_id, current.student_name, current.gpa)
            current = current.next

    def search_by_name(self, name):
        current = self.head
        while current is not None:
            if current.student_name == name:
                print("Tapıldı:", current.student_id, current.student_name, current.gpa)
                return
            current = current.next
        print("Tələbə tapılmadı:", name)

    def count(self):
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total


# ---------- Test hissesi ----------
def main():
    print("--- Tapşırıq 1 ---")
    test_node = Node(15)
    print("Node yaradıldı, data =", test_node.data, ", next =", test_node.next)

    print("\n--- Tapşırıq 2 ---")
    ll = LinkedList()
    for number in [10, 20, 30, 40]:
        ll.insert_at_end(number)
    ll.display()

    print("\n--- Tapşırıq 3 ---")
    ll = LinkedList()
    for number in [20, 30, 40]:
        ll.insert_at_end(number)
    ll.insert_at_beginning(10)
    ll.display()

    print("\n--- Tapşırıq 4 ---")
    ll = LinkedList()
    for number in [10, 20, 40]:
        ll.insert_at_end(number)
    ll.insert_after(20, 30)
    ll.display()

    print("\n--- Tapşırıq 5 ---")
    ll = LinkedList()
    for number in [10, 20, 30, 40, 50]:
        ll.insert_at_end(number)
    ll.delete(30)
    ll.display()

    print("\n--- Tapşırıq 6 ---")
    ll.search(40)
    ll.search(99)

    print("\n--- Tapşırıq 7 ---")
    ll = LinkedList()
    for number in [11, 22, 33, 44, 55]:
        ll.insert_at_end(number)
    print("List length =", ll.length())

    print("\n--- Tapşırıq 8 ---")
    ll = LinkedList()
    for number in [23, 8, 91, 15, 42]:
        ll.insert_at_end(number)
    ll.display()
    print("Maksimum:", ll.find_max())
    print("Minimum:", ll.find_min())

    print("\n--- Tapşırıq 9 ---")
    ll = LinkedList()
    for number in [10, 20, 30, 40, 50]:
        ll.insert_at_end(number)
    ll.display()
    ll.reverse()
    ll.display()

    print("\n--- Tapşırıq 10 ---")
    students = StudentList()
    students.add_student(1, "Ali", 85)
    students.add_student(2, "Leyla", 78)
    students.add_student(3, "Orxan", 92)
    students.add_student(4, "Aysel", 70)
    print("Bütün tələbələr:")
    students.show_all()
    print("GPA > 80 olanlar:")
    students.show_high_gpa()
    print("Ada görə axtarış:")
    students.search_by_name("Leyla")
    students.search_by_name("Vüqar")
    students.delete_student(2)
    print("Leyla silindikdən sonra:")
    students.show_all()
    print("Tələbələrin sayı:", students.count())


if __name__ == "__main__":
    main()
