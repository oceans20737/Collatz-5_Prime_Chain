#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

"""
Verification Script for 5-adic Prime Chains
Author: Hiroshi Harada
Date: February 25, 2026
License: MIT

This script verifies the primality and structure of a 5-adic Collatz-like prime chain
starting from a given initial value n₀. It prints each step of the chain, the applied
constant c, and whether the number is prime.

Usage:
    python verify_5adic_chain.py
"""

import sympy

def get_next_5adic_custom(n):
    """
    Computes the next value in the extended 5-adic sequence.
    Returns the next number and the constant c used.
    """
    rem = n % 5
    if rem == 1: return (6 * n - 1) // 5, "-1"
    if rem == 2: return (6 * n + 3) // 5, "+3"
    if rem == 3: return (6 * n - 3) // 5, "-3"
    if rem == 4: return (6 * n + 1) // 5, "+1"
    return None, None  # Invalid case when n ≡ 0 mod 5

def verify_5adic_chain(n0, length=7):
    """
    Verifies the primality and sequence of a 5-adic prime chain starting from n0.
    Prints each step and returns the verified chain.
    """
    print(f"\n=== Verifying 5-adic Prime Chain from n₀ = {n0} ===")
    curr = n0
    chain = []

    for i in range(length):
        if sympy.isprime(curr):
            status = "PRIME"
            chain.append(curr)
        else:
            status = "COMPOSITE — Chain Broken"
            print(f"Step {i}: {curr} → {status}")
            break

        print(f"Step {i}: {curr} → {status}")

        if i < length - 1:
            nxt, c_used = get_next_5adic_custom(curr)
            if nxt is None:
                print(f"  [ Invalid step: n ≡ 0 mod 5 ]")
                break
            print(f"    [ Applied c = {c_used} → Next = {nxt} ]")
            curr = nxt

    print(f"\nFinal Result: Verified chain of length {len(chain)}")
    print(f"Chain: {chain}\n")
    return chain

if __name__ == "__main__":
    # Discovered L=7 prime chains by Hiroshi Harada
    discovery_1 = 19084201
    discovery_2 = 76933159

    verify_5adic_chain(discovery_1)
    verify_5adic_chain(discovery_2)


# In[ ]:




