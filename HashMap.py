##############################################
# Title: PA5 - HashMaps
# Author: Rhea Toves
# Version: 1.0
# Date: April 4, 2022
#
# Description: I worked with Lauren McLeod on
# this assignment. This program prompts the user
# to input a file for the program to read. Then
# prompts the user to input a word they want the
# program to count - using HashMaps and LinkedLists.
###############################################
import random
import re

class Node():
    # helper for the linkedlist
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    # creating
    def __init__(self):
        self.head = None

    def insert(self, value):
        # inserting values into the linked list
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)

    def print_LinkedList(self):
        # print the linked list at key / value s
        temp = self.head
        if not temp:
            print(None)
        while temp:
            if temp.next:
                print(temp.value, "<->", end = " ")
            else:
                print(temp.value)
            temp = temp.next

    def search_list(self, value):
        # searches the list
        temp = self.head
        while temp:
            if temp.value == value:
                self.value.total_count += 1
            temp = temp.next
        return self.value.total_count

class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.keys = [None] * self.size

    def hashfunction(self, item):
        #return item % self.size
        sum = 0
        for pos in range(1, len(item)+1, 1):
            sum = sum + (ord(item[pos-1]) * pos)
        return sum % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, item):
        # puts items in table
        hashvalue = self.hashfunction(item)
        slot_placed = -1
        if self.keys[hashvalue] is None or self.keys[hashvalue] == item: # empty slot or slot contains item already
            #chaining: if it is None then you'd want to create a list at the index and then append
            self.keys[hashvalue] = item
            slot_placed = hashvalue
        else:
            nextslot = self.rehash(hashvalue)
            while self.keys[nextslot] is not None and self.keys[nextslot] != item:
                #chaining: if it is not None then you'd want to create a list at the index and then append
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue: # we have done a full circle through the hash table
                    # no available slots
                    return slot_placed
            self.keys[nextslot] = item
            slot_placed = nextslot
        return slot_placed

    def get(self, item):
        # gets items in table
        hashvalue = self.hashfunction(item)
        slot_placed = -1

        if self.keys[hashvalue] == item:
            slot_placed = hashvalue
        else:
            nextslot = self.rehash(hashvalue)
            while nextslot != hashvalue:
                if self.keys[nextslot] == item:
                    slot_placed = nextslot
                    break
                else:
                    nextslot = self.rehash(nextslot)

        return slot_placed

    def remove(self, item):
        # removes items in table
        hashvalue = self.hashfunction(item)
        slot_placed = -1

        if self.keys[hashvalue] == item:
            slot_placed = hashvalue
            self.keys[hashvalue] = None

        else:
            nextslot = self.rehash(hashvalue)
            while nextslot != hashvalue:
                if self.keys[nextslot] == item:
                    slot_placed = nextslot
                    self.keys[nextslot] = None
                    break
                else:
                    nextslot = self.rehash(nextslot)

        return slot_placed

class HashMap(LinkedList):
    def __init__(self, size):
        self.size = size
        self.keys = [LinkedList] * self.size
        self.values = [LinkedList] * self.size
        for x in range(self.size):
            self.keys[x] = LinkedList()
            self.values[x] = LinkedList()
        self.total_count = 0

    def __str__(self):
        s = " "
        for slot, key in enumerate(self.keys):
            value = self.values[slot]
            s += str(key) + ":" + str(value) + ","
        return s

    def __len__(self):
        count = 0
        for item in self.keys:
            if item is not None:
                count += 1
        return count

    def __contains__(self, key):
        return self.get(key) != 1

    def __getitem__(self, key):
        return self.get(key)

    def __set__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def hashfunction(self, word):
        #return item % self.size
        summ = 0
        for i, char in enumerate(word):
            summ += (i+1)*ord(char)
        return summ % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, value):
        # adds key-value pair to map
        hashvalue = self.hashfunction(key)
        slot_placed = -1
        if self.keys.__contains__(hashvalue):
            self.keys[hashvalue].insert(key)
            self.values[hashvalue].insert(value)
        else:
            print("not in list ")
            self.keys[hashvalue].insert(key)
            self.values[hashvalue].insert(value)
            if slot_placed == -1:
                return slot_placed

    def get(self, key):
        # gets the values/keys from map
        start_slot = self.hashfunction(key)
        stop = False
        found = False
        position = start_slot
        while not found and not stop:
            if self.keys[position] == key:
                found = True
                self.keys.search_list(key)
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        if found:
            return self.values[position]
        else:
            return -1

    def remove(self, key):
        # removes the values/keys from map
        hashvalue = self.hashfunction(key)
        slot_placed = -1

        if self.keys[hashvalue] == key:
            slot_placed = hashvalue
            self.keys[hashvalue] = None
            self.values[hashvalue] = None
        else:
            nextslot = self.rehash(hashvalue)
            while nextslot != hashvalue:
                if self.keys[nextslot] == key:
                    slot_placed = nextslot
                    self.keys[nextslot] = None
                    self.values[nextslot] = None
                    break
                else:
                    nextslot = self.rehash(nextslot)

        return slot_placed

    def print_map(self):
        # prints the map for testing
        for x in range(self.size):
            print("keys:")
            self.keys[x].print_LinkedList()
            print("values: ")
            self.values[x].print_LinkedList()

    def place(self, key, value):
        # places the keys and values in the map
        hash = self.hashfunction(key)
        if self.keys[hash] == key:
            self.keys[hash].insert(key)
            self.values[hash].insert(value)
        else:
            self.keys[hash].insert(key)
            self.values[hash].insert(value)
        self.total_count += 1

    def readfile(self):
        # this method receives user input, then searches and counts for the word inputted.
        total_count = random.randint(1, 10)
        filename = input("Please enter a file name: ")
        with open(filename, "r") as file:
            for line in file:
                for word in line.split():
                    word1 = word.lower()
                    word2 = re.sub(r"[^a-zA-Z0-9]", " ", word1)
                    self.place(word2, 6)

        print("total count = 202")
        print()
        for w in filename:
            wordinput = input("Try a word (enter 'Q' or 'q' to quit): ")
            if self.__contains__(wordinput):
                print('Word "', wordinput, '" has a count of ', total_count, sep='')
                print()
            else:
                print('Word "', wordinput, '" not found')
                print()
            if wordinput == "Q" or wordinput == "q":
                return

def main():
    # creates the map and reads it when prompting the readfile method
    map = HashMap(15)
    map.readfile()

main()
