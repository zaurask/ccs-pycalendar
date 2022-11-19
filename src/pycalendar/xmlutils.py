##
#    Copyright (c) 2007-2013 Cyrus Daboo. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##

import xml.etree.ElementTree as XML


def makeTag(namespace, name):
    return "{%s}%s" % (namespace, name.lower(),)


def toString(root):

    data = """<?xml version="1.0" encoding="utf-8"?>\n"""

    INDENT = 2

    # Generate indentation
    def _indentNode(node, level=0):
        if node.text is not None and node.text.strip():
            return
        elif list(node):
            indent = "\n" + " " * (level + 1) * INDENT
            node.text = indent
            for child in list(node):
                child.tail = indent
                _indentNode(child, level + 1)
            if len(list(node)):
                list(node)[-1].tail = "\n" + " " * level * INDENT

    _indentNode(root, 0)
    data += XML.tostring(root).decode() + "\n"

    return data
