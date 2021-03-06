#
#  PikiTVAppDelegate.py
#  PikiTV
#
#  Created by Jesse Hammons on 8/5/08.
#  Copyright __MyCompanyName__ 2008. All rights reserved.
#

from Foundation import *
from AppKit import *

##class TTVMode(NSResponder):

class PikiTVAppDelegate(NSObject):
	numbersInput = objc.ivar(u"numbersInput")
	numbersResult = objc.ivar(u"numbersResult")
	
	def applicationDidFinishLaunching_(self, sender):
		#self.numbersResult.setIntValue_(7)
		NSLog("Application did finish launching.")
		NSLog("bundle %@", NSBundle.mainBundle().privateFrameworksPath())
		path = NSBundle.mainBundle().bundlePath() + u'/../VSDecoder.h'
		NSLog("path %@", path)
		NSLog("text %@", NSString.stringWithContentsOfFile_(NSBundle.mainBundle().bundlePath() + u'/../VSDecoder.h'))

	def awakeFromNib(self):
		#self.numbersResult.setIntValue_(5)
		pass

	def setNumbersInput_(self, value):
		self.numbersInput = value
		#self.numbersResult.setIntValue_(int(value)*2)
		NSLog(u"value is %@", value)
		self.numbersResult = int(value)*2