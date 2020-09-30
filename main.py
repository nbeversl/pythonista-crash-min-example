# Minimal example for Pythonista Troubleshooting

import ui
from objc_util import *
import syntax

example_text = """
title::Example Text

{  === Example === 

example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
example text >342
}

[[ ID(>0l2) -- 
+() +(example=all)
SORT(timestamp -t -r)
SHOW($title $link\n$date\n\n) ]]

[[ ID(>vze) +(tags = project; tags=current) 
SORT(timestamp  -t -r -alpha) 
FOOTER(index::01) 
HEADER( == Current Projects ==\n) DEPTH(1) 
SHOW($title $link\n) ]]


id::02o
index::00
"""

class MainView(ui.View):

	def __init__(self):
	
		w,h = ui.get_screen_size()
		self.height = h
		self.width = w
		self.frame= (0,0,w,h)

		self.tv=ui.TextView()
		self.tv.frame=(0,18,w,h)
		
		self.tv.font = ('Helvetica Neue', 12)
		self.tv.auto_content_inset = True
		self.tv.background_color = '#282923'
		self.tv.text_color = 'white'
		self.tv.width = w
		
		self.full_txt_search_field = ui.TextField()

		self.add_subview(self.full_txt_search_field)		
		self.add_subview(self.tv)

		self.tvo = ObjCInstance(self.tv)
		viewDelegate = SyntaxHighlighter(self.tvo)
		self.tv.delegate = viewDelegate
		self.tv.text = example_text
		self.show_problem()

	def show_problem(self):
		self.tv.scroll_enabled= False
		syntax.setAttribs(self.tv, self.tvo)
		self.tv.scroll_enabled= True		
			
class SyntaxHighlighter(object):

	def __init__(self, tvo):
		self.tvo = tvo

	def textview_did_change(self, textview):
		""" Re-run syntax highlighting whenever the text content changes"""
		main_view.show_problem()   

main_view = MainView()
main_view.present('fullscreen', hide_title_bar=True)



