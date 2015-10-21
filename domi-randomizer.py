#!/usr/bin/env python

import random
import argparse

DATA_FILE = 'cards.dat'

class Group:
  def __init__(self, group_name):
    self.groupname = group_name
    self.group_cards = []

  def add_card(self, card_name):
    self.group_cards.append(card_name)

def input_value_check(assign_data):
  sum = 0
  for key, value in assign_data.iteritems():
    if type(value) == int:
      sum += value
  if sum > 10:
    raise ValueError("10 and less cards needed")

def read_data(filename):
  group_data = {}
  with open(filename) as file:
    for line in file:
      if line.strip()== '':
        continue
      if line.strip()[0] == "#":
        group_name = line.strip()[1:]
        group_data[group_name] = Group(line.strip()[1:])
        continue
      group_data[group_name].add_card(line.strip())
  return group_data

def pop_random_card(card_list):
  rand = random.random() * len(card_list)
  return card_list.pop(int(rand))

def pop_card_by_name(card_data, card_name):
  for group in card_data.itervalues():
    for i, v in enumerate(group.group_cards):
      if v == card_name:
        return group.group_cards.pop(i)
  raise ValueError("input correct card name")

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--alchemy", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include alchemy")
parser.add_argument("-b", "--base", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include base")
parser.add_argument("-c", "--cornucopia", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include cornucopia")
parser.add_argument("-i", "--intrigue", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include intrigue")
parser.add_argument("-p", "--prosperity", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include prosperity")
parser.add_argument("-n", "--hinterlands", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include hinterlands")
parser.add_argument("-d", "--darkages", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include darkages")
parser.add_argument("-g", "--guilds", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include guilds")
parser.add_argument("-a", "--adventures", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include adventures")
parser.add_argument("-s", "--seaside", const=True, default=False, nargs="?", type=int, choices=range(1,10), help="include seaside")
parser.add_argument("--omit", dest="omit_list",
                    type=str, nargs="+", help="you can omit the cards you want to do.")
parser.add_argument("--add", dest="add_list", type=str, nargs="+", help="if you specify a card, it never fail to be included")

args = parser.parse_args()

assign_data = {
  "base": args.base,
  "alchemy": args.alchemy,
  "cornucopia": args.cornucopia,
  "intrigue": args.intrigue,
  "prosperity": args.prosperity,
  "hinterlands": args.hinterlands,
  "darkages": args.darkages,
  "guilds": args.guilds,
  "adventures": args.adventures,
  "seaside": args.seaside
}

input_value_check(assign_data)

card_data = read_data(DATA_FILE)
use_card = []

if args.omit_list != None:
  for omit_card in args.omit_list:
    pop_card_by_name(card_data, omit_card)

if args.add_list != None:
  for add_card in args.add_list:
    use_card.append(
      pop_card_by_name(card_data, add_card)
    )

for group_name, n in assign_data.iteritems():
  if type(n) == int:
    while n > 0:
      n -= 1
      use_card.append(
        pop_random_card(
          card_data[group_name].group_cards
        )
      )
if len(use_card) < 10:
  candidate_card_list = []
  for group_name, n in assign_data.iteritems():
    if type(n) == bool and n:
      candidate_card_list.extend(card_data[group_name].group_cards)
  if len(candidate_card_list) == 0:
    print "Not specified extension pack is included."
    for group_name in assign_data:
      candidate_card_list.extend(card_data[group_name].group_cards)
  while len(use_card) < 10:
    use_card.append(
      pop_random_card(candidate_card_list)
    )

print use_card
