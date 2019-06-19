#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################
# Copyright:    Siyuan Sheng
# Date:         6/19/2019
# Description:  Mine association rules via A priori
#               algorithm
#################################################

import xlrd

filename = "medical_test.xlsx"

col_index = 7

sep = '、'

min_support = 0.5
min_confidence = 0.5

def read_xlsx(filepath):
    workbook = xlrd.open_workbook(filepath)
    book_sheet = workbook.sheet_by_name(u'肠易激')

    values = book_sheet.col_values(col_index)
    for i in range(len(values)):
        values[i] = values[i].encode('utf-8')
    del values[0]
    return values

def split_values(values):
    buckets = []
    for i in range(len(values)):
        items = values[i].split(sep)
        buckets.append(items)
    return buckets

# Get 1-frequent itemsets
def get_init_frequent_itemset(buckets):
    init_itemset = {}

    # Couting
    for i in range(len(buckets)):
        items = buckets[i]
        for item in items:
            item = (item, )
            if init_itemset.has_key(item):
                init_itemset[item] = init_itemset[item]+1
            else:
                init_itemset[item] = 1

    # Filtering
    min_count = min_support*len(buckets)
    for key, v in init_itemset.items():
        if v < min_count:
            del init_itemset[key]

    return init_itemset

def generate_candidate_itemset(items_list):
    tmp_size = len(items_list[0])

    items_list = list(items_list)
    for i in range(len(items_list)):
        items_list[i] = set(items_list[i])

    tmp_itemset = set()
    # Self-joining
    for i in range(len(items_list)):
        # i > j
        for j in range(i):
            items1 = items_list[i]
            items2 = items_list[j]
            items = items1.union(items2)
            if len(items) == tmp_size + 1:
                tmp_itemset.add(tuple(items))

    result = [] 
    # Pruning
    for tmp_items in tmp_itemset:
        # Make sure all of subsets are in items_list
        is_prune = False
        for i in range(tmp_size+1):
            tmp_subset = set(tmp_items[0:i])
            tmp_subset = tmp_subset.union(set(tmp_items[i+1:tmp_size+1]))
            if tmp_subset not in items_list:
                is_prune = True
                break
        if not is_prune:
            result.append(tmp_items)

    return result

def get_frequent_itemsets(buckets):
    init_frequent_itemset = get_init_frequent_itemset(buckets)
    
    # frequent_itemsets[i] indicates (i+1)-frequent itemset
    frequent_itemsets = [init_frequent_itemset]

    # Get other frequent itemsets
    k = 1
    while True:
        # Get (k+1)-frequent itemset
        tmp_frequent_itemset = {}

        # Generate candidate itemsets
        k_frequent_itemset = frequent_itemsets[k-1]
        candidate_itemset = generate_candidate_itemset(k_frequent_itemset.keys())

        for candidate_items in candidate_itemset:
            tmp_frequent_itemset[candidate_items] = 0

        # Counting
        for i in range(len(buckets)):
            items = buckets[i]
            for candidate_items in candidate_itemset:
                is_contain = True
                for item in candidate_items:
                    if item not in items:
                        is_contain = False
                        break
                if is_contain:
                    tmp_frequent_itemset[candidate_items] = tmp_frequent_itemset[candidate_items]+1

        # Filtering
        min_count = min_support*len(buckets)
        for key,v in tmp_frequent_itemset.items():
            if v < min_count:
                del tmp_frequent_itemset[key]
        
        if len(tmp_frequent_itemset) == 0:
            break
        frequent_itemsets.append(tmp_frequent_itemset)
        k = k+1
    return frequent_itemsets

# choose i numbers from k numbers in the range of [0, k-1] 
def get_combinations(k, i):
    if i > k or i < 0:
        return None

    if i == k:
        return [range(k)]

    if i == 1:
        result = []
        for m in range(k):
            result.append([m])
        return result

    if i == 0:
        return []

    result = []
    tmp_contain = get_combinations(k-1, i-1)
    tmp_not_contain = get_combinations(k-1, i)
    for tmp in tmp_contain:
        for m in range(len(tmp)):
            tmp[m] = tmp[m] + 1
        tmp.append(0)
        result.append(tmp)
    for tmp in tmp_not_contain:
        for m in range(len(tmp)):
            tmp[m] = tmp[m] + 1
        result.append(tmp)
    return result

def get_ruleset(frequent_itemsets, buckets):
    ruleset = {}
    for k in range(len(frequent_itemsets)):
        # There's no ruleset in 1-frequent itemset
        if k == 0:
            continue

        # For (k+1)-itemset
        itemset = frequent_itemsets[k]
        for items, count in itemset.items():
            length = len(items)
            for j in range(length):
                if j == 0:
                    continue

                # rule: j -> length-j
                combinations = get_combinations(length, j)
                for combination in combinations:
                    left_items = []
                    right_items = []
                    for m in range(len(items)):
                        if m in combination:
                            left_items.append(items[m])
                        else:
                            right_items.append(items[m])

                    # rule: left_items -> right_items
                    left_items = tuple(set(left_items))
                    right_items = tuple(set(right_items))
                    tmp_support = count / float(len(buckets))
                    tmp_confidence = frequent_itemsets[len(left_items)-1][left_items] / float(count)
                    if tmp_confidence >= min_confidence:
                        rule_key = (left_items, right_items)
                        rule_value = (tmp_support, tmp_confidence)
                        if ruleset.has_key(rule_key):
                            print("Error: Existed rule key: {}->{}".format(tuple_to_str(rule_key[0]), tuple_to_str(rule_key[1])))
                            exit()
                        ruleset[rule_key] = rule_value
    return ruleset

def tuple_to_str(items):
    result = ""
    size = len(items)
    for i in range(size):
        result = result + items[i]
        if i != size-1:
            result = result + sep
    return result

def display_ruleset(ruleset):
    print("Min support: {}".format(min_support))
    print("Min confidence: {}".format(min_confidence))
    print("Format: [index] [left item] -> [right item] #[support] #[confidence]")
    print("Here is our rule set")
    i = 1
    for key, value in ruleset.items():
        left_item_str = tuple_to_str(key[0])
        right_item_str = tuple_to_str(key[1])
        print("{} {} -> {} #{} #{}".format(i, left_item_str, right_item_str, value[0], value[1])) 
        i = i+1

def main():
    values = read_xlsx(filename)
    buckets = split_values(values)
    frequent_itemsets = get_frequent_itemsets(buckets)
    ruleset = get_ruleset(frequent_itemsets, buckets)
    display_ruleset(ruleset)

if __name__ == '__main__':
    main()
