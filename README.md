Name: Nazilə Gülməmmədova

Group: KOM25

Laboratory Work 2

Singly Linked List-in reallaşdırılması və tətbiqi

Teacher: Şamil Hümbətov

Implemented operations:

- Node class (Task 1)
- Insert at end (Task 2)
- Insert at beginning (Task 3)
- Insert after a given element (Task 4)
- Delete node (Task 5)
- Search node (Task 6)
- List length (Task 7)
- Find maximum and minimum (Task 8)
- Reverse list without creating a new list (Task 9)
- Student registry system (Task 10)

How the program works:

Siyahı Node obyektlərindən ibarətdir. Hər düyündə data (qiymət) və next
(növbəti düyünə istinad) var. LinkedList sinfi yalnız head (birinci düyün)
saxlayır. Bütün əməliyyatlar head-dən başlayaraq next istinadları ilə
siyahı boyunca gəzməklə icra olunur. Siyahının sonu None ilə göstərilir.
Reverse əməliyyatında yeni siyahı yaradılmır, yalnız düyünlərin next
istinadları geri çevrilir. Task 10-da eyni prinsip StudentNode və
StudentList siniflərində tələbə məlumatları üçün istifadə olunub.

Run:

python src/linkedlist.py