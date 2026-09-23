# Week 3, Day 2 — Classwork: Attributes, Methods, and Magic Methods

## 1. Teacher Actions

**English**
Create a class `Teacher` with instance attributes `full_name`, `subject`, and `experience=0`. Add instance methods `teach()`, `set_experience(years)`, and `get_experience()`. Reject a negative experience value. Create one teacher, call every method, and print the results.

**Тоҷикӣ**
Class-и `Teacher` созед, ки instance attribute-ҳои `full_name`, `subject` ва `experience=0` дорад. Instance method-ҳои `teach()`, `set_experience(years)` ва `get_experience()`-ро илова кунед. Қимати манфии таҷрибаро рад намоед. Як омӯзгор сохта, ҳамаи method-ҳоро даъват кунед ва натиҷаҳоро чоп кунед.

**Русский**
Создайте класс `Teacher` с атрибутами экземпляра `full_name`, `subject` и `experience=0`. Добавьте методы экземпляра `teach()`, `set_experience(years)` и `get_experience()`. Отклоняйте отрицательное значение стажа. Создайте одного преподавателя, вызовите все методы и выведите результаты.

**Input**

    Nasiba Karimova Python
    6

**Output**

    Nasiba Karimova is teaching Python.
    Experience: 6 years

------------------------------------------------------------------------

## 2. Shared School Name

**English**
Create a class `Student` with the class attribute `school_name="School 21"` and the instance attributes `name` and `grade`. Create two students and print their school names. Then change the class attribute through `Student`, print both students again, and show that the new value is shared.

**Тоҷикӣ**
Class-и `Student` созед, ки class attribute-и `school_name="School 21"` ва instance attribute-ҳои `name` ва `grade` дорад. Ду донишҷӯ сохта, номи мактаби онҳоро чоп кунед. Баъд class attribute-ро тавассути `Student` тағйир дода, ҳар ду донишҷӯро аз нав чоп кунед ва умумӣ будани қимати навро нишон диҳед.

**Русский**
Создайте класс `Student` с атрибутом класса `school_name="School 21"` и атрибутами экземпляра `name` и `grade`. Создайте двух учеников и выведите названия их школы. Затем измените атрибут класса через `Student`, снова выведите обоих учеников и покажите, что новое значение общее.

**Input**

    Ali 10
    Sara 11
    Python Academy

**Output**

    Ali | 10 | School 21
    Sara | 11 | School 21
    Ali | 10 | Python Academy
    Sara | 11 | Python Academy

------------------------------------------------------------------------

## 3. Employee Counter

**English**
Create a class `Employee` with the class attribute `employees_count=0`. Every new object must increase this counter. Add the class method `get_count()` that returns the current number of employees and the instance method `show_info()`. Read employee names until `stop`, create the objects, print them, and print the total through the class method.

**Тоҷикӣ**
Class-и `Employee`-ро бо class attribute-и `employees_count=0` созед. Ҳар object-и нав бояд ин ҳисобкунакро зиёд кунад. Class method-и `get_count()`-ро барои баргардондани шумораи кормандон ва instance method-и `show_info()`-ро илова кунед. Номҳоро то `stop` хонда, object-ҳо созед, онҳоро чоп кунед ва шумораи умумиро тавассути class method нишон диҳед.

**Русский**
Создайте класс `Employee` с атрибутом класса `employees_count=0`. Каждый новый объект должен увеличивать счётчик. Добавьте метод класса `get_count()`, возвращающий текущее количество сотрудников, и метод экземпляра `show_info()`. Считывайте имена до `stop`, создайте объекты, выведите их и общее количество через метод класса.

**Input**

    Ali Developer
    Sara Designer
    Rustam Manager
    stop

**Output**

    Ali | Developer
    Sara | Designer
    Rustam | Manager
    Total employees: 3

------------------------------------------------------------------------

## 4. Static Calculator

**English**
Create a class `Calculator` with static methods `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, and `divide(a, b)`. Division by zero must return `Cannot divide by zero`. Call the methods through the class without creating an object.

**Тоҷикӣ**
Class-и `Calculator`-ро бо static method-ҳои `add(a, b)`, `subtract(a, b)`, `multiply(a, b)` ва `divide(a, b)` созед. Ҳангоми тақсим ба сифр `Cannot divide by zero` баргардонед. Method-ҳоро бе сохтани object тавассути class даъват кунед.

**Русский**
Создайте класс `Calculator` со статическими методами `add(a, b)`, `subtract(a, b)`, `multiply(a, b)` и `divide(a, b)`. При делении на ноль возвращайте `Cannot divide by zero`. Вызовите методы через класс, не создавая объект.

**Input**

    12 3

**Output**

    Add: 15
    Subtract: 9
    Multiply: 36
    Divide: 4.0

------------------------------------------------------------------------

## 5. Currency Exchange Rate

**English**
Create a class `Currency` with the class attribute `usd_rate=10.90`. Store a dollar amount in each object. Add the instance method `to_somoni()`, the class method `change_rate(new_rate)`, and the static method `valid_rate(value)`. Change the shared rate only when it is positive, then show how the same object gives a new result.

**Тоҷикӣ**
Class-и `Currency`-ро бо class attribute-и `usd_rate=10.90` созед. Дар ҳар object маблағи долларро нигоҳ доред. Instance method-и `to_somoni()`, class method-и `change_rate(new_rate)` ва static method-и `valid_rate(value)`-ро илова кунед. Қурби умумиро танҳо ҳангоми мусбат будан тағйир диҳед ва нишон диҳед, ки ҳамон object натиҷаи нав медиҳад.

**Русский**
Создайте класс `Currency` с атрибутом класса `usd_rate=10.90`. В каждом объекте храните сумму в долларах. Добавьте метод экземпляра `to_somoni()`, метод класса `change_rate(new_rate)` и статический метод `valid_rate(value)`. Изменяйте общий курс только при положительном значении и покажите, что тот же объект выдаёт новый результат.

**Input**

    100
    11.20

**Output**

    Before: 1090.00 TJS
    Rate changed: True
    After: 1120.00 TJS

------------------------------------------------------------------------

## 6. Bank Account String

**English**
Create a class `BankAccount` with `owner` and `balance=0`. Add instance methods `deposit(amount)` and `withdraw(amount)` with validation. Implement `__str__()` so `print(account)` returns `Owner: <name>, Balance: <balance>`. Perform the operations and print the account after each one.

**Тоҷикӣ**
Class-и `BankAccount`-ро бо `owner` ва `balance=0` созед. Instance method-ҳои `deposit(amount)` ва `withdraw(amount)`-ро бо санҷиши қиматҳо илова кунед. `__str__()`-ро тавре амалӣ кунед, ки `print(account)` сатри `Owner: <name>, Balance: <balance>`-ро диҳад. Амалиётҳоро иҷро карда, баъди ҳар кадом ҳисобро чоп кунед.

**Русский**
Создайте класс `BankAccount` с `owner` и `balance=0`. Добавьте методы экземпляра `deposit(amount)` и `withdraw(amount)` с проверкой значений. Реализуйте `__str__()`, чтобы `print(account)` возвращал строку `Owner: <name>, Balance: <balance>`. Выполните операции и выводите счёт после каждой.

**Input**

    Alice 1000
    deposit 500
    withdraw 2000
    withdraw 300

**Output**

    Owner: Alice, Balance: 1500
    Insufficient funds
    Owner: Alice, Balance: 1500
    Owner: Alice, Balance: 1200

------------------------------------------------------------------------

## 7. Product for Users and Developers

**English**
Create a class `Product` with `name`, `price`, and `quantity`. Implement `__str__()` for a user-friendly description and `__repr__()` for an unambiguous developer representation. Create one product and print `str(product)` and `repr(product)`.

**Тоҷикӣ**
Class-и `Product`-ро бо `name`, `price` ва `quantity` созед. Барои тавсифи фаҳмо ба корбар `__str__()` ва барои намоиши дақиқи object ба барномасоз `__repr__()`-ро амалӣ кунед. Як маҳсулот сохта, `str(product)` ва `repr(product)`-ро чоп кунед.

**Русский**
Создайте класс `Product` с `name`, `price` и `quantity`. Реализуйте `__str__()` для понятного пользователю описания и `__repr__()` для однозначного представления объекта разработчику. Создайте один товар и выведите `str(product)` и `repr(product)`.

**Input**

    Laptop 7500 3

**Output**

    Laptop — 7500 TJS, stock: 3
    Product(name='Laptop', price=7500, quantity=3)

------------------------------------------------------------------------

## 8. Books with the Same ISBN

**English**
Create a class `Book` with `title`, `author`, and `isbn`. Implement `__eq__()` so two book objects are equal when their ISBN values are equal. Implement `__repr__()` and compare three books. Comparing a book with an object of another type must return `False`.

**Тоҷикӣ**
Class-и `Book`-ро бо `title`, `author` ва `isbn` созед. `__eq__()`-ро тавре амалӣ кунед, ки ду book object ҳангоми баробар будани ISBN баробар ҳисоб шаванд. `__repr__()`-ро илова карда, се китобро муқоиса кунед. Муқоисаи китоб бо object-и навъи дигар бояд `False` диҳад.

**Русский**
Создайте класс `Book` с `title`, `author` и `isbn`. Реализуйте `__eq__()`, чтобы два объекта-книги считались равными при одинаковом ISBN. Добавьте `__repr__()` и сравните три книги. Сравнение книги с объектом другого типа должно возвращать `False`.

**Input**

    Python101 Ali 978-1
    PythonBasics Sara 978-1
    Django101 Rustam 978-2

**Output**

    Book 1 == Book 2: True
    Book 1 == Book 3: False
    Book 1 == '978-1': False

------------------------------------------------------------------------

## 9. Playlist Size and Search

**English**
Create a class `Playlist` that stores a title and a list of songs. Add the instance method `add_song(song)`. Implement `__len__()` to return the number of songs and `__contains__(song)` so the expression `song in playlist` works without case sensitivity. Add songs, print the size, and perform two searches.

**Тоҷикӣ**
Class-и `Playlist` созед, ки ном ва рӯйхати сурудҳоро нигоҳ медорад. Instance method-и `add_song(song)`-ро илова кунед. `__len__()` бояд шумораи сурудҳоро баргардонад ва `__contains__(song)` бояд expression-и `song in playlist`-ро бе фарқи ҳарфҳои калону хурд кор фармояд. Сурудҳо илова карда, андоза ва натиҷаи ду ҷустуҷӯро чоп кунед.

**Русский**
Создайте класс `Playlist`, хранящий название и список песен. Добавьте метод экземпляра `add_song(song)`. Реализуйте `__len__()` для количества песен и `__contains__(song)`, чтобы выражение `song in playlist` работало без учёта регистра. Добавьте песни, выведите размер и выполните два поиска.

**Input**

    Study
    Believer
    Numb
    Imagine
    numb
    Halo

**Output**

    Study: 3 songs
    numb found: True
    Halo found: False

------------------------------------------------------------------------

## 10. Adding Vectors

**English**
Create a class `Vector` with coordinates `x` and `y`. Implement `__add__()` so `vector1 + vector2` returns a new `Vector` containing the sums of matching coordinates. Implement `__str__()` as `(x, y)`. Add two vectors and prove that the original objects did not change.

**Тоҷикӣ**
Class-и `Vector`-ро бо coordinate-ҳои `x` ва `y` созед. `__add__()`-ро тавре амалӣ кунед, ки `vector1 + vector2` object-и нави `Vector`-ро бо суммаи coordinate-ҳои мувофиқ баргардонад. `__str__()` бояд шакли `(x, y)` диҳад. Ду vector-ро ҷамъ карда нишон диҳед, ки object-ҳои ибтидоӣ тағйир наёфтанд.

**Русский**
Создайте класс `Vector` с координатами `x` и `y`. Реализуйте `__add__()`, чтобы выражение `vector1 + vector2` возвращало новый объект `Vector` с суммами соответствующих координат. Реализуйте `__str__()` в формате `(x, y)`. Сложите два вектора и покажите, что исходные объекты не изменились.

**Input**

    2 5
    3 -1

**Output**

    Vector 1: (2, 5)
    Vector 2: (3, -1)
    Sum: (5, 4)
    Originals unchanged: (2, 5), (3, -1)
