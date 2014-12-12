import glob
for filename in glob.glob('*.png'):
	with open('new/' + filename[:-3] + 'cursor', 'w') as f:
		if 'aero_working' in filename or 'aero_busy' in filename:
			continue
		select = 'aero_nwse aero_ns aero_nesw aero_ew up size no move cross busy'
		if any(word in filename for word in select.split()):
			print 'up size no move cross busy in', filename
			f.write('32 16 16 xcursorgen/' + filename)
		else:
			print 'NOT ', filename
			f.write('32 0 0 xcursorgen/' + filename)
