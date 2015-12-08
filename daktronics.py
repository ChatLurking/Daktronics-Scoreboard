#!/usr/bin/python

import re, string, serial

s = serial.Serial(
	port = 'localhost',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	timeout = 0)


class daktronics:


	def recieving(s):
		buffer_string = ''
		while True:
			buffer_string = buffer_string + s.read(s.inWaiting())
			if '' in buffer_string:
				lines = buffer_string.split('')
				checksum(lines)


	def enum (**enums):
		return type ('Enum', (), enums)


	def calc_checksum(st):
	    return (sum(ord(x) for x in st) % 256) + 7


	def checksum ( buf ):
		p = re.compile('^(\d+)$')
		
		our_cksum = 0

		cksum_range = filter(lambda x: x in string.printable, buf)
		l = len(cksum_range)
		packet = enum(SYN = cksum_range[0:8], SOH = cksum_range[8:18], DATA = cksum_range[18:l-2], CKSUM = cksum_range[-2:l])
		cksum = int(packet.CKSUM, 16)

		our_cksum = calc_checksum(cksum_range)

		if (cksum != our_cksum % 256):
			print "warning: invalid checksum (ours %i theirs %i)" %(our_cksum, cksum)

		
		if hasattr(daktronics, "packet_%s" %(p.match(packet.SOH)) == True):
			send("packet_%s"(packet.DATA) %(packet.SOH))
		else:
			print ""
			print "----------UNKNOWN PACKET (%s)---------" %(packet.SOH)
			print ""


	# Parse main game clock
	def packet_0042100000(payload):
		tenths = -1

		# Tests to see if payload is Min:Sec
		prog = re.compile('^(([ \d]\d):(\d\d))')
		result = prog.match(payload[0:6])

		# Parse Payload as time in minutes:seconds
		#or seconds.tenths
		if (result != None):
			# Stuff so that time will be displayed as Min:Sec
			print result


		prog = re.compile('^(([\d]\d.(\d))')
		result = prog.match(payload[0:6])
		if (result != None):
			# Stuff so that time will be displayed as Sec.Tenths
			print result
		else:
			print "0042100000: don't understand clock format"

		if tentchs >= 0 :
			# Sync clock time


	# Parse home team score
	def packet_0042100107(payload):
		prog = re.compile('(\d+)')
		result = prog.match(payload)

		if(payload != None):
			print payload
			home_score = payload
			# sync score

	# Parse visiting team score
	def packet_0042100111 (payload):
		prog = re.compile('(\d+)')
		result = prog.match(payload)

		if(payload != None):
			print payload
			guest_score = payload
			# sync score

	#Parse ball-on message
	def packet_0042100219 (payload):
		# First feild is ball possition, second is down third is distance to go
		prog = re.compile('^([0-9 ]{2})(1ST|2ND|3RD|4TH)([0-9 ]{2})')
		result = prog.match(payload)

		if(result != None):
				#seperate out different fields

				#sync everything

		if (ballpos == to_go):
			#sync distance ("Goal")
		else:
			#sync_disctance(to_go)


	# Parse football down
	def packet_0042100221 (payload):
		prog = re.compile('(1st|2nd|3rd|4th)/i')
		result = prog.match(payload)

		if(result != None):
			print result
			#sync down


	# Parse yards to go
	def packet_0042100224 (payload):
		prog = re.compile('(\d+)')
		result = prog.match(payload)

		if (result != None):
			print result
			#sync distance to go

	# Parse play clock
	def packet_0042100200 (payload):
		prog = re.compile('(\d+)')
		result = prog.match(payload)

		if(result != None):
			print result
			# sync play clock

	# Parse home Possession
	#NEEDS TO BE WORKED ON
	def packet_0042100209 (payload):
		prog = re.compile('([<>])')
		result = prog.match(payload)
		print result

	# Parse guest Possession
	# NEEDS WORK
	def packet_0042100214 (payload):
		print result


recieving(s)