def boyer_moore_search(string:str, target:str)->int:
    if target=='':
        return 0
    if len(target) == 1:
        return string.find(target)
    else: 
        _table = {}
        for i in range(len(target)):
            _table[target[i]] = max(1,len(target)-i-1)
        index = len(target)-1
        while index < len(string):
            if string[index] == target[-1]:
                k = 0 
                while k < len(target) and target[k] == string[index+k-len(target)+1]:
                    k+=1
                    if k == len(target)-1:
                        return index-len(target)+1
                else:
                    k = 0
                    while k < len(target)-1:
                        if string[index+k-len(target)-1] in _table:
                            index += _table[string[index+k-len(target)-1]]
                            break        
                        else:
                            k+=1
                    else:
                        index += _table[target[-1]]
            elif string[index] in _table:
                index += _table[string[index]]
            else:
                index += max(1,len(target)-1)
        return -1
def boyer_moore_search2(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return 0
    if n < m:
        return -1
    bad_char_shift = {}
    for i in range(m - 1):
        bad_char_shift[pattern[i]] = m - 1 - i
    
    # Начинаем сравнение с конца первого возможного окна
    idx = m - 1
    
    while idx < n:
        k = 0
        # 2. Сравнение справа налево
        # pattern[m-1-k] сравнивается с text[idx-k]
        while k < m and pattern[m - 1 - k] == text[idx - k]:
            k += 1
        
        if k == m:
            # Полное совпадение найдено
            return idx - m + 1
        
        # 3. Вычисление сдвига
        # Символ в тексте, который вызвал несовпадение (или выход за границы слева, если k=m, но мы уже вышли)
        mismatch_char = text[idx - k]
        
        # Получаем сдвиг из таблицы. Если символа нет, сдвигаем на всю длину шаблона (m)
        shift_from_table = bad_char_shift.get(mismatch_char, m)
        
        # Формула сдвига: (сдвиг из таблицы) - (сколько символов уже совпало с конца)
        # Гарантируем сдвиг минимум на 1
        shift = max(1, shift_from_table - k)
        
        idx += shift

    return -1

if __name__ == '__main__':
    print(boyer_moore_search('bdfyyhlvfwecppmaaxmfwpdafewgjtdhtxoihfxwqqaxlnknkorlmdgfwzpfwgmzvdwagmizothcfyhzmfz','txoihfx'))
    print(boyer_moore_search("abc", "abc"))
    print(boyer_moore_search("abxd", "abcd"))
# # if __name__ == '__main__':
#     import time
    
#     test_cases = [
#         {
#             "name": "1. Стена из 'A' (короткий шаблон)",
#             "text": "A" * 100000 + "B",
#             "pattern": "AAAAB"
#         },
#         {
#             "name": "2. Стена из 'A' (длинный шаблон)",
#             "text": "A" * 100000 + "B",
#             "pattern": "AAAAAAAAAAAAAAAB"
#         },
#         {
#             "name": "3. Периодический паттерн (короткий)",
#             "text": "AB" * 50000 + "C",
#             "pattern": "ABABAC"
#         },
#         {
#             "name": "4. Периодический паттерн (длинный)",
#             "text": "ABCD" * 25000 + "E",
#             "pattern": "ABCDABCDABCDABCE"
#         },
#         {
#             "name": "5. Одинаковые символы (короткий)",
#             "text": "X" * 100000 + "Y",
#             "pattern": "XXXXY"
#         },
#         {
#             "name": "6. Одинаковые символы (длинный)",
#             "text": "X" * 100000 + "Y",
#             "pattern": "XXXXXXXXXXXXXXX Y".replace(" ", "")
#         },
#         {
#             "name": "7. Частые совпадения хвоста (короткий)",
#             "text": "XYZXYZXYZ" * 10000 + "Q",
#             "pattern": "XYZPQ"
#         },
#         {
#             "name": "8. Частые совпадения хвоста (длинный)",
#             "text": "XYZXYZXYZ" * 10000 + "Q",
#             "pattern": "XYZXYZXYZPQ"
#         },
#         {
#             "name": "9. Единичный символ (краевой случай)",
#             "text": "HELLO WORLD",
#             "pattern": "W"
#         },
#         {
#             "name": "10. Шаблон длины 2",
#             "text": "HELLO WORLD",
#             "pattern": "WO"
#         },
#     ]

#     print("=" * 90)
#     print("ГЛУБОКИЙ ТЕСТ АЛГОРИТМА БОЙЕРА-МУРА (С ДЛИНОЙ ШАБЛОНА)")
#     print("=" * 90)

#     results = []

#     for i, case in enumerate(test_cases, 1):
#         text = case["text"]
#         pattern = case["pattern"]
#         pattern_len = len(pattern)
#         text_len = len(text)
        
#         # Ваш вариант
#         start = time.time()
#         r1 = boyer_moore_search(text, pattern)
#         t1 = time.time() - start
        
#         # Канонический вариант
#         start = time.time()
#         r2 = boyer_moore_search2(text, pattern)
#         t2 = time.time() - start
        
#         # Проверка корректности
#         correct = (r1 == r2)
#         ratio = t1 / t2 if t2 > 0 else float('inf')
        
#         results.append({
#             "name": case["name"],
#             "text_len": text_len,
#             "pattern_len": pattern_len,
#             "your_time": t1,
#             "canonical_time": t2,
#             "ratio": ratio,
#             "correct": correct,
#             "result": r1
#         })
        
#         status = "✅" if correct else "❌"
#         print(f"\nТест {i}: {case['name']}")
#         print(f"  {status} Результат: {r1} (канонический: {r2})")
#         print(f"  📏 Длина текста: {text_len:,} | Длина шаблона: {pattern_len}")
#         print(f"  ⏱ Ваш код:      {t1:.4f} сек")
#         print(f"  ⏱ Канонический: {t2:.4f} сек")
#         print(f"  📊 Разница:     {ratio:.2f}x {'(быстрее)' if ratio < 1 else '(медленнее)'}")

#     # ──────────────────────────────────────────────────────────
#     # СВОДНАЯ ТАБЛИЦА
#     # ──────────────────────────────────────────────────────────

#     print("\n" + "=" * 90)
#     print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ")
#     print("=" * 90)

#     print(f"\n{'Тест':<5} {'Дл. шаблона':<12} {'Корректно':<10} {'Ваш код':<12} {'Канонич.':<12} {'Разница':<10}")
#     print("-" * 90)

#     for i, r in enumerate(results, 1):
#         status = "✅" if r["correct"] else "❌"
#         print(f"{i:<5} {r['pattern_len']:<12} {status:<10} {r['your_time']:<12.4f} {r['canonical_time']:<12.4f} {r['ratio']:<10.2f}x")

#     # ──────────────────────────────────────────────────────────
#     # АНАЛИЗ ПО ДЛИНЕ ШАБЛОНА
#     # ──────────────────────────────────────────────────────────

#     print("\n" + "=" * 90)
#     print("АНАЛИЗ ПРОИЗВОДИТЕЛЬНОСТИ ПО ДЛИНЕ ШАБЛОНА")
#     print("=" * 90)

#     short_patterns = [r for r in results if r["pattern_len"] <= 6]
#     long_patterns = [r for r in results if r["pattern_len"] > 6]

#     if short_patterns:
#         avg_short = sum(r["ratio"] for r in short_patterns) / len(short_patterns)
#         print(f"\n  Короткие шаблоны (≤6):  Средняя разница {avg_short:.2f}x")
        
#     if long_patterns:
#         avg_long = sum(r["ratio"] for r in long_patterns) / len(long_patterns)
#         print(f"  Длинные шаблоны (>6):   Средняя разница {avg_long:.2f}x")

#     # ──────────────────────────────────────────────────────────
#     # ИТОГО
#     # ──────────────────────────────────────────────────────────

#     avg_ratio = sum(r["ratio"] for r in results) / len(results)
#     max_ratio = max(r["ratio"] for r in results)
#     min_ratio = min(r["ratio"] for r in results)
#     all_correct = all(r["correct"] for r in results)

#     print("\n" + "=" * 90)
#     print("ИТОГОВЫЕ ПОКАЗАТЕЛИ")
#     print("=" * 90)
#     print(f"  Средняя разница:     {avg_ratio:.2f}x")
#     print(f"  Минимальная разница: {min_ratio:.2f}x")
#     print(f"  Максимальная разница: {max_ratio:.2f}x")
#     print(f"  Все тесты пройдены:  {'✅ ДА' if all_correct else '❌ НЕТ'}")
#     print("=" * 90)