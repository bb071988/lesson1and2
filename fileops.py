# file ops
import locale
locale.setlocale(locale.LC_ALL, '')

total_count = 0
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    print(header)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
        	total_count += int(line[5])
        	tmp_cnt = int(line[5])
        	# print("Continent: {0:15}     Population: {1:>15}".format(line[0], line[5]))
        	print("Continent: {0:15}     Population: {1:>20,d}".format(line[0], tmp_cnt))
print("Grand Total: {0:,d}".format(total_count))

print(locale.format("%d", total_count,  grouping=True))
# '{:20,.2f}'.format(18446744073709551616.0)

# import locale
# >>> locale.setlocale( locale.LC_ALL, '' )
# 'English_United States.1252'
# >>> locale.currency( 188518982.18 )
# '$188518982.18'
# >>> locale.currency( 188518982.18, grouping=True )
# '$188,518,982.18'