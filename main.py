
from action import form_pattern
from action import Filter, ContentMerger

SOURCE_PATH = 'source.txt'
RESULT_PATH = 'result.txt'


if __name__ == '__main__':
	with open(SOURCE_PATH, 'r') as source_file, open(RESULT_PATH, 'w+') as result_file:
		pattern = form_pattern(prefix="id=\"ext-gen\\d+\">", postfix="</span>")
		Filter.filter_line(source_file, result_file, pattern)

		# ContentMerger.merge(source_file, result_file)
