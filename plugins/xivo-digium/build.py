# -*- coding: UTF-8 -*-

from subprocess import check_call


@target('1.3.3.0', 'xivo-digium-1.3.3.0')
def build_1_3_3_0(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '1.3.3.0/', path])
