### Завдання 9 
В завданні команда ``` pytest tests/tests.py ``` вибивала помилку : 
```  
ERROR collecting tests/tests.py ________________________
ImportError while importing test module '/home/vitaliy/bygil/vitaliy_kuz_ik_31_bygil/lab2/tests/tests.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/tests.py:2: in <module>
    from app import main, my_good_fun, home_work
E   ImportError: cannot import name 'home_work' from 'app' (/home/vitaliy/bygil/vitaliy_kuz_ik_31_bygil/lab2/tests/app.py)
=========================== short test summary info ============================
ERROR tests/tests.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
```
В інтернеті я знайшов що треба видалити *__init__.py* це допомогло тому далі без нього
###Завдання 10
Додав результат виконання програми у кінець цього ж  файлу командою ```python app.py >> results.txt```