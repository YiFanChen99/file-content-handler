
import re
from collections import defaultdict


def form_pattern(main='(.*?)', prefix='', postfix=''):
    prefix_ = "(?:" + prefix + ")" if prefix else ''
    postfix_ = "(?:" + postfix + ")" if postfix else ''
    return re.compile(prefix_ + main + postfix_)


class Filter():
    @staticmethod
    def filter_conetent(source_file, result_file, pattern):
        """ Filter content line-wise. """
        for content in source_file:
            for match in re.finditer(pattern, content):
                result_file.write('%s\n' % (match.group(1)))

    @staticmethod
    def filter_line(source_file, result_file, pattern):
        raise NotImplementedError  # using "grep -v" instead


class ContentMerger():
    @staticmethod
    def merge(source_file, result_file):
        result = defaultdict(lambda: 0)
        for content in source_file:
            result[content] += 1

        for key, value in result.items():
            if len(key) <= 1:  # empty
                continue

            key = key[:-1]  # remove char '\n'
            result_file.write('%s: %d\n' % (key, value))
