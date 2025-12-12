# ----------------------------------------------------
# Copyright The IETF Trust 2018-9, All Rights Reserved
# ----------------------------------------------------

import io
import subprocess
import re
import os
import six
from xml2rfc import log
from rfclint.spell import which, RfcLintError

if six.PY3:
    unicode = str


class AbnfChecker(object):
    def __init__(self, config):
        program = config.get('abnf', 'program')
        self.dictionaries = config.getList('abnf', 'addrules')
        if program:
            if not which(program):
                raise RfcLintError("The program '{0}' does not exist or is not executable".
                                   format(program))
        else:
            # look on the path first
            look_for = "bap"
            if os.name == "nt":
                look_for = "bap.exe"
            program = which(look_for)

            if not program:
                raise RfcLintError("Install bap.")

        self.abnfProgram = program

    def validate(self, tree):
        stdin = io.StringIO()
        xtract = SourceExtracter(tree, "abnf")
        if not xtract.ExtractToFile(stdin):
            log.note("No ABNF to check")
            return False
        cmds = [self.abnfProgram, "-q"]

        if self.dictionaries:
            for dict in self.dictionaries:
                if not os.path.exists(dict):
                    raise RfcLintError("Additional ABNF rule file '{0}' does not exist".
                                       format(dict))
                cmds.append("-i")
                cmds.append(dict)

        p = subprocess.Popen(cmds, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        (stdout, stderr) = p.communicate(stdin.getvalue().encode('utf-8'))

        errs = stderr.decode('utf-8').splitlines()
        noError = True
        noWarn = True
        for err in errs:
            if err.strip() == "":
                continue

            m = re.match(r"(.+)\((\d+):(\d+)\): error: (.*)", err)
            if m:
                line = int(m.group(2))
                filename = m.group(1)
                if filename == 'stdin':
                    runningLine = 0
                    for xxx in xtract.lineOffsets:
                        if line < runningLine + xxx[2]:
                            log.error(m.group(4), file=xxx[0], line=xxx[1] + line - runningLine)
                            noError = False
                            break
                        runningLine += xxx[2] - 1
                else:
                    log.error(m.group(4), str(filename), str(line))
                    noError = False
            else:
                log.note(err)
                noWarn = False
        if noError and noWarn:
            log.note("ABNF checked with no warnings or errors")
        elif noError:
            log.note("ABNF checked with no errors")
        return True


class SourceExtracter(object):
    def __init__(self, tree, sourceType):
        self.tree = tree
        self.sourceType = sourceType

    def ExtractToFile(self, file):
        """
        Extract the code items to the provided file
        Return True if something was actually extracted
        """

        codeItems = self.tree.getroot().xpath("//sourcecode[@type='{0}']".format(self.sourceType))
        if len(codeItems) == 0:
            return False

        lineOffsets = []
        for item in codeItems:
            if six.PY2:
                file.write(unicode(item.text))
            else:
                file.write(item.text)
            lineCount = item.text.count('\n') + 1
            if len(item.text) > 0 and item.text[-1] != '\n':
                file.write(u'\n')
                lineCount += 1
            lineOffsets.append((item.base, item.sourceline, lineCount))

        self.lineOffsets = lineOffsets
        return True
