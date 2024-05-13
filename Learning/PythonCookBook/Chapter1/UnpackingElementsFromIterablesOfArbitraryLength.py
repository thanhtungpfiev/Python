# Created by Admin at 5/7/2022
def avg(middle):
    return sum(middle) / len(middle)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record


def avg_comparison(trailing_avg, current_qtr):
    pass


def record_compare(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return avg_comparison(trailing_avg, current_qtr)


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
record_name, *_, (*_, year) = record

items = [1, 10, 7, 4, 5, 9]


def sum_test(items_test):
    head, *tail = items_test
    return head + sum_test(tail) if tail else head


print(sum_test(items))
