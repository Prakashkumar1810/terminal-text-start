import curses
import time

data1 = ["twostep_auth.sh",
	"Username:Prakashkumar1810",
	"password:********************",
	"Gaining access to System"]
data2 = ["strueedit.bui -r -s -unauth",
	"syslog = true",
	"struct group_info init_groups = .usage = ATOMIC_INIT(2)",
	"if(!grouinfo)",
	"	return NULL",
	"group_info->nblocks = nblocks;",
	"for(i=0;i<nblocks;i++){",
	"	gid_t*b;",
	"	b = (void*)__get_docRes(GFP_USER);",
	"}",
	"EXPORT $EDITOR=vim",
	"ftp.request(CALL_SSH);"
	"*stb = (void*)malloc(size_of(int));",
	"(__result==mat2)?return b_float:blocks_c;"
	"struct TrieNode {",
	"	struct TrieNode* children[ALPHABET_SIZE];",
	"	bool isEndOfWord;",
	"};",
	"int index = key[i] - 'a';",
	"if (!pCrawl->children[index])",
	"	pCrawl->children[index] = getNode();",
	"gquiz1.insert(pair<int, int>(1, 40));",
	"binary_search(startaddress, endaddress, valuetofind)",
	"	gquiz1.insert(pair<int, int>(3, 60));",
	"	gquiz1.insert(pair<int, int>(6, 50));",
	"ios_base::sync_with_stdio(false);",
	"cin.tie(NULL);",
	"#include <bits/stdc++.h>",
	"mask = ~((1 << i+1 ) - 1);",
	"x &= mask;",
	"void access(int[] a...){",
	"	A -> 01000001",
	"	B -> 01000010",
	"	C -> 01000011",
	"	ch = ‘A’ (01000001)",
	"}",
	"template <typename T>",
	"element_t<T> *next, *prev;"]
data3 = ["ACCESS GRANTED",
	"Version 3.2.6",
	"Intializing...",
	"Completing setup",
	"All done!!!!!!!!!!!!"]

def pre_text(stdscn):
	global i
	
	stdscn.attron(curses.color_pair(1))
	stdscn.attron(curses.A_BOLD)
	
	for data in data1:
		if i<h:
			for j,letter in enumerate(data):
				if j<w:
					stdscn.addstr(i,j,letter)
					stdscn.refresh()
					time.sleep(0.02)
				else:
					break
			i+=1
		else:
			stdscn.attroff(curses.color_pair(1))
			stdscn.attroff(curses.A_BOLD)
			break
	stdscn.attroff(curses.A_BOLD)
	stdscn.attroff(curses.color_pair(1))

def middle_text(stdscn):
	global i
	
	stdscn.attron(curses.color_pair(2))
	
	for data in data2:
		if i<h:
			stdscn.addstr(i,0,data)
			stdscn.refresh()
			time.sleep(0.05)
			i+=1
		else:
			stdscn.attroff(curses.color_pair(2))
			break
	stdscn.attroff(curses.color_pair(2))

def post_text(stdscn):
	
	stdscn.clear()
	stdscn.attron(curses.color_pair(3))
	stdscn.attron(curses.A_BOLD)
	
	i=0
	for data in data3:
		if i<h:
			stdscn.addstr(i,0,data)
			stdscn.refresh()
			time.sleep(0.2)
			i+=1
		else:
			stdscn.attroff(curses.A_BOLD)
			stdscn.attroff(curses.color_pair(3))
			break
	stdscn.attroff(curses.A_BOLD)
	stdscn.attroff(curses.color_pair(3))

def main(stdscn):
	curses.curs_set(False)
	
	curses.use_default_colors()
	curses.init_pair(1,curses.COLOR_YELLOW,-1)
	curses.init_pair(2,curses.COLOR_CYAN,-1)
	curses.init_pair(3,curses.COLOR_GREEN,-1)
	
	global h,w
	h,w = stdscn.getmaxyx()
	global i
	i=0
	
	pre_text(stdscn)
	
	middle_text(stdscn)
	
	post_text(stdscn)


curses.wrapper(main)
