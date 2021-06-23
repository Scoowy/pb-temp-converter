#!/usr/bin/env python
# -*- coding: utf-8 -*-

from converters import F_to_K, C_to_F, C_to_R


def main():
    print('Nuevo modulo')
    print(round(F_to_K(64), 3))
    print(round(C_to_F(32), 3))
    print(round(C_to_R(100), 3))


if __name__ == "__main__":
    main()
