#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author   : cheer
# @Copyright: No FUCKING rights reserved.

_MAPPING = [
    '零', '一', '二', '三', '四', '五', '六', '七', '八', '九',
    '十', '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九'
]
_P0 = ['', '十', '百', '千']
_S4 = 10 ** 4


def to_chinese(number):
    assert 0 <= number < _S4

    if number < 20:
        return _MAPPING[number]

    lst = []
    while number >= 10:
        lst.append(number % 10)
        number = number / 10
    lst.append(number)
    c = len(lst)
    result = ''

    for idx, val in enumerate(lst):
        val = int(val)
        if val != 0:
            result += _P0[idx] + _MAPPING[val]
            if idx < c - 1 and lst[idx + 1] == 0:
                result += '零'
    return result[::-1]
