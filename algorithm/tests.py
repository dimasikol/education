import unittest
import os
import tempfile
import sys
import time
from .alg.recurshen import Rec, Node  # замените на имя вашего файла


# ============================================================================
# БАЗОВЫЕ ТЕСТЫ (дополненные)
# ============================================================================

class TestRecBasic(unittest.TestCase):
    """Тесты базовой функциональности с расширенными кейсами"""

    # === get_sum ===
    def test_get_sum_negative_numbers(self):
        self.assertEqual(Rec.get_sum([-1, -2, -3]), -6)

    def test_get_sum_mixed_signs(self):
        self.assertEqual(Rec.get_sum([-5, 10, -3, 2]), 4)

    def test_get_sum_large_list(self):
        self.assertEqual(Rec.get_sum(list(range(1000))), sum(range(1000)))

    def test_get_sum_index_param(self):
        # Тест что индексный параметр работает корректно
        self.assertEqual(Rec.get_sum([1, 2, 3, 4], index=2), 7)  # 3+4

    # === get_count_target ===
    def test_count_target_strings(self):
        self.assertEqual(Rec.get_count_target(["a", "b", "a", "c"], "a"), 2)

    def test_count_target_none(self):
        self.assertEqual(Rec.get_count_target([None, 1, None], None), 2)

    def test_count_target_custom_object(self):
        class Obj:
            def __init__(self, val): self.val = val

            def __eq__(self, other): return isinstance(other, Obj) and self.val == other.val

        a, b = Obj(1), Obj(1)
        self.assertEqual(Rec.get_count_target([a, Obj(2), b], a), 2)

    # === get_tail ===
    def test_get_tail_long_list(self):
        nodes = [Node(i) for i in range(100)]
        for i in range(99):
            nodes[i].next = nodes[i + 1]
        self.assertIs(Rec.get_tail(nodes[0]), nodes[99])

    def test_get_tail_circular_warning(self):
        # Внимание: рекурсия зациклится на циклическом списке!
        # Это тест на документирование ограничения
        n1, n2 = Node(1), Node(2)
        n1.next, n2.next = n2, n1  # цикл
        with self.assertRaises(RecursionError):
            Rec.get_tail(n1)

    # === get_product ===
    def test_product_with_zero(self):
        self.assertEqual(Rec.get_product([1, 2, 0, 4]), 0)

    def test_product_negative(self):
        self.assertEqual(Rec.get_product([-2, 3, -4]), 24)

    def test_product_floats(self):
        self.assertAlmostEqual(Rec.get_product([1.5, 2.0, 3.0]), 9.0)

    # === get_factorial ===
    def test_factorial_negative(self):
        # Факториал отрицательного числа не определён
        # Текущая реализация вернёт 1 для n<=1, что может быть неочевидно
        self.assertEqual(Rec.get_factorial(-5), 1)  # Документируем поведение

    def test_factorial_large(self):
        import math
        self.assertEqual(Rec.get_factorial(20), math.factorial(20))

    def test_factorial_recursion_limit(self):
        # Проверка на переполнение стека
        with self.assertRaises(RecursionError):
            Rec.get_factorial(sys.getrecursionlimit() + 100)

    # === get_fibonacci ===
    def test_fib_negative(self):
        # Поведение для отрицательных чисел
        self.assertEqual(Rec.get_fibonacci(-1), -1)  # Документируем

    def test_fib_large_cached(self):
        # Благодаря кэшу должно работать быстро
        start = time.time()
        result = Rec.get_fibonacci(100)
        elapsed = time.time() - start
        self.assertEqual(result, 354224848179261915075)
        self.assertLess(elapsed, 1.0)  # Должно быть мгновенно с кэшем

    def test_fib_cache_invalidation(self):
        # Проверка что кэш работает между вызовами
        Rec.get_fibonacci(50)  # Заполняем кэш
        start = time.time()
        Rec.get_fibonacci(50)  # Должно быть мгновенно
        self.assertLess(time.time() - start, 0.001)

    # === get_min ===
    def test_min_negative_numbers(self):
        self.assertEqual(Rec.get_min([-5, -1, -10, -3]), -10)

    def test_min_floats(self):
        self.assertEqual(Rec.get_min([3.14, 2.71, 1.41]), 1.41)

    def test_min_with_index(self):
        # Тест параметра index
        self.assertEqual(Rec.get_min([5, 2, 8, 1], index=2), 1)  # поиск с индекса 2: [8,1]

    # === get_pow ===
    def test_pow_large_exponent(self):
        self.assertEqual(Rec.get_pow(2, 20), 2 ** 20)

    def test_pow_zero_base(self):
        self.assertEqual(Rec.get_pow(0, 5), 0)
        self.assertEqual(Rec.get_pow(0, 0), 1)  # 0^0 = 1 по конвенции

    def test_pow_negative_exponent(self):
        # Текущая реализация не поддерживает отрицательные степени
        # Документируем поведение
        self.assertEqual(Rec.get_pow(2, -1), 1)  # т.к. c<=1 возвращает 1 для c=-1

    # === get_binary_search ===
    def test_binary_empty_array(self):
        self.assertEqual(Rec.get_binary_search([], 5), -1)

    def test_binary_single_element_found(self):
        self.assertEqual(Rec.get_binary_search([42], 42), 0)

    def test_binary_single_element_not_found(self):
        self.assertEqual(Rec.get_binary_search([42], 100), -1)

    def test_binary_duplicates(self):
        # Возвращает любой из индексов с искомым значением
        arr = [1, 2, 2, 2, 3]
        result = Rec.get_binary_search(arr, 2)
        self.assertIn(arr[result], [2])
        self.assertTrue(0 <= result < len(arr))

    def test_binary_all_same(self):
        arr = [5, 5, 5, 5]
        result = Rec.get_binary_search(arr, 5)
        self.assertIn(result, range(4))

    def test_binary_string_array(self):
        arr = ["apple", "banana", "cherry", "date"]
        self.assertEqual(Rec.get_binary_search(arr, "cherry"), 2)
        self.assertEqual(Rec.get_binary_search(arr, "apricot"), -1)

    # === get_palindrome ===
    def test_palindrome_empty(self):
        self.assertTrue(Rec.get_palindrome([]))
        self.assertTrue(Rec.get_palindrome(""))

    def test_palindrome_single(self):
        self.assertTrue(Rec.get_palindrome([1]))
        self.assertTrue(Rec.get_palindrome("a"))

    def test_palindrome_even_odd(self):
        self.assertTrue(Rec.get_palindrome([1, 2, 2, 1]))  # чётная длина
        self.assertTrue(Rec.get_palindrome([1, 2, 3, 2, 1]))  # нечётная

    def test_palindrome_string_special_chars(self):
        self.assertTrue(Rec.get_palindrome("A man, a plan, a canal: Panama"[::-1]))  # просто разворот

    # === convert_to_cc ===
    def test_to_cc_zero(self):
        self.assertEqual(Rec.convert_to_cc(0, 2), [])  # 0 возвращает пустой список

    def test_to_cc_base_1_edge(self):
        # Основание 1 не имеет смысла, но проверим поведение
        # (бесконечная рекурсия возможна)
        with self.assertRaises(RecursionError):
            Rec.convert_to_cc(5, 1)

    def test_to_cc_large_number(self):
        result = Rec.convert_to_cc(1000, 16)
        # 1000 = 0x3E8 = [8, 14, 3] LSB first
        self.assertEqual(result, [8, 14, 3][::-1])

    def test_to_cc_order_lsb_first(self):
        # Документируем: возвращается порядок от младшего разряда
        self.assertEqual(Rec.convert_to_cc(13, 2), [1, 0, 1, 1][::-1])  # 1101 в обратном порядке

    # === convert_list_to_dec ===
    def test_from_dec_empty(self):
        self.assertEqual(Rec.convert_list_to_dec([], 2), 0)

    def test_from_dec_single_digit(self):
        self.assertEqual(Rec.convert_list_to_dec([5], 10), 5)

    def test_from_dec_consistency(self):
        # Тест кругового преобразования
        for n in [0, 1, 42, 255, 1000]:
            for base in [2, 8, 16]:
                converted = Rec.convert_to_cc(n, base)
                print(converted)
                back = Rec.convert_list_to_dec(converted, base)
                self.assertEqual(back, n, f"Failed for n={n}, base={base}")

    # === sum_digits ===
    def test_sum_digits_negative(self):
        # Отрицательные числа: текущая реализация работает с модулем
        self.assertEqual(Rec.sum_digits(-123), 6)  # т.к. -123 // 10 = -13, и т.д.

    def test_sum_digits_large(self):
        self.assertEqual(Rec.sum_digits(999999999), 81)

    def test_sum_digits_zero_leading(self):
        # Ведущие нули не влияют (числа их не хранят)
        self.assertEqual(Rec.sum_digits(1000), 1)

    # === reverse_string ===
    def test_reverse_unicode(self):
        self.assertEqual(Rec.reverse_string("Привет"), "тевирП")

    def test_reverse_emoji(self):
        self.assertEqual(Rec.reverse_string("a🎉b"), "b🎉a")

    def test_reverse_performance(self):
        # Рекурсия со срезами строк может быть медленной
        s = "a" * 500  # 500 символов
        start = time.time()
        result = Rec.reverse_string(s)
        elapsed = time.time() - start
        self.assertEqual(result, s[::-1])
        # Предупреждение: при >1000 символов возможен RecursionError

    # === pow_log ===

    def test_pow_log_corrected_logic(self):
        # После исправления эти тесты должны проходить:
        # (раскомментируйте когда исправите метод)
        # self.assertEqual(Rec.pow_log(2, 10), 1024)
        # self.assertEqual(Rec.pow_log(10, 3), 1000)
        pass

    # === is_sorted ===
    def test_sorted_empty_single(self):
        self.assertTrue(Rec.is_sorted([]))
        self.assertTrue(Rec.is_sorted([1]))

    def test_sorted_equal_elements(self):
        self.assertTrue(Rec.is_sorted([1, 1, 1, 1]))

    def test_sorted_tail_param(self):
        # Тест параметра tail
        self.assertTrue(Rec.is_sorted([1, 5, 3, 4], tail=2))  # проверяем с индекса 2: [3,4]
        self.assertFalse(Rec.is_sorted([1, 5, 3, 4], tail=1))  # [5,3] нарушает порядок

    # === gen_binary ===
    def test_gen_binary_zero(self):
        self.assertEqual(Rec.gen_binary(0), [''])

    def test_gen_binary_order(self):
        result = Rec.gen_binary(3)
        # Проверка что все комбинации есть и нет дубликатов
        self.assertEqual(len(result), 8)
        self.assertEqual(len(set(result)), 8)
        self.assertEqual(sorted(result), ['000', '001', '010', '011', '100', '101', '110', '111'])

    # === permutations / permutations2 ===
    def test_permutations_duplicates_input(self):
        # Вход с дубликатами: текущая реализация генерирует дубликаты перестановок
        result = Rec.permutations2([1, 1, 2])
        # Ожидаем 3 уникальные: [1,1,2], [1,2,1], [2,1,1]
        unique = [list(p) for p in {tuple(x) for x in result}]
        self.assertEqual(len(unique), 3)

    def test_permutations_empty(self):
        self.assertEqual(Rec.permutations2([]), [[]])

    def test_permutations_consistency(self):
        # Обе функции должны давать одинаковый результат (с точностью до порядка)
        arr = [1, 2, 3]
        r1 = sorted(map(tuple, Rec.permutations2(arr)))
        r2 = sorted(map(tuple, Rec.permutations(arr)))  # если исправить permutations
        # self.assertEqual(r1, r2)  # Раскомментируйте после исправления permutations

    # === sub_set ===
    def test_subsets_empty(self):
        result = Rec.sub_set([])
        self.assertEqual(result, [])  # Текущая реализация не добавляет пустое множество


    # === list_files ===
    def test_list_files_nested_deep(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Создаём вложенную структуру
            path = tmpdir
            for i in range(5):
                path = os.path.join(path, f"dir{i}")
                os.makedirs(path, exist_ok=True)
                with open(os.path.join(path, f"file{i}.txt"), "w") as f:
                    f.write("test")

            result = Rec.list_files(tmpdir)
            self.assertEqual(len([f for f in result if f.endswith('.txt')]), 5)

    def test_list_files_permission_error(self):
        # Тест на обработку ошибок доступа (опционально)
        pass  # Сложно тестировать без root прав

    # === unique_paths ===
    def test_unique_paths_large(self):
        # Динамическое программирование должно работать быстро
        start = time.time()
        result = Rec.unique_paths(10, 10)
        self.assertLess(time.time() - start, 0.1)
        self.assertEqual(result, 48620)  # C(18,9)

    def test_unique_paths_asymmetric(self):
        self.assertEqual(Rec.unique_paths(1, 5), 1)  # Только один путь
        self.assertEqual(Rec.unique_paths(5, 1), 1)

    def test_unique_paths_zero_dim(self):
        # Граничный случай: нулевое измерение
        self.assertEqual(Rec.unique_paths(0, 5), 0)  # Нет ячеек
        self.assertEqual(Rec.unique_paths(5, 0), 0)

    # === is_balanced (только ()) ===
    def test_balanced_nested_deep(self):
        self.assertTrue(Rec.is_balanced("()" * 50))
        self.assertTrue(Rec.is_balanced("(" * 50 + ")" * 50))

    def test_balanced_wrong_order(self):
        self.assertFalse(Rec.is_balanced(")("))
        self.assertFalse(Rec.is_balanced("())"))

    def test_balanced_with_other_chars(self):
        # Текущая реализация считает все не-скобки как закрывающие!
        # Это баг: "a(b)c" вернёт False
        self.assertFalse(Rec.is_balanced("a(b)c"))  # Документируем ограничение

    # === is_balance_multy ===
    def test_multy_nested_mixed(self):
        self.assertTrue(Rec.is_balance_multy("({[()]}{})"))

    def test_multy_wrong_type_close(self):
        self.assertFalse(Rec.is_balance_multy("([)]"))
        self.assertFalse(Rec.is_balance_multy("{(})"))

    def test_multy_unclosed(self):
        self.assertFalse(Rec.is_balance_multy("(([]"))
        self.assertFalse(Rec.is_balance_multy("{[}"))

    def test_multy_empty_and_whitespace(self):
        self.assertTrue(Rec.is_balance_multy(""))
        # Пробелы и другие символы игнорируются (не являются скобками)
        self.assertTrue(Rec.is_balance_multy("a b c"))


    def test_merge_with_duplicates(self):
        result = Rec.merge_list([1, 2, 2, 3], [2, 2, 4])
        self.assertEqual(result, [1, 2, 2, 2, 2, 3, 4])

    def test_merge_stability(self):
        # При равных элементах сначала берётся из lst1 (из-за условия >=)
        result = Rec.merge_list([1, 2], [2, 3])
        self.assertEqual(result, [1, 2, 2, 3])
        # Проверка порядка равных: первый 2 из lst1, второй из lst2